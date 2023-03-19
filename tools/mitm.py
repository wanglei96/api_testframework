# -*- coding: utf-8 -*-
# @File   : mitm
# @Time   : 2022/3/31 10:47 
# @Author : 张福强
import mitmproxy.http
from mitmproxy import ctx, http
import os, json
import base64


class PacketSaver:
    def __init__(self, filter_url: str):
        # 过滤的域名
        self.filter_url = filter_url.strip()

        # 文件存放路径
        root_dir = os.path.abspath(os.path.join(os.getcwd()))
        self.mitm_path = root_dir + '/mitmproxy_temp'
        if not os.path.exists(self.mitm_path):
            os.makedirs(self.mitm_path)

        # 需要过滤的url
        self.black_mime = [
            'webp', 'jpg', 'jpeg', 'png', 'js', 'css', 'mp3', 'mp4', 'gif', 'ico', 'm3u8', 'woff', 'ttf'
        ]

        # 整理接收回来的格式
        self.infos = {}

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
        :param flow:
        :return:
        """

        # 定义全局接收格式
        self.infos['url'] = flow.request.url.split('?')[0]
        self.infos['code'] = flow.response.status_code

        # 过滤URL
        if self.filter_url not in self.infos['url']:
            return
        if not self.infos['url'].startswith('http') or not self.infos['url'].startswith('https'):
            return
        for e in self.black_mime:
            if self.infos['url'].endswith('.' + e):
                return
        # filter url end

        self.infos['method'] = flow.request.method.lower()
        if self.infos['method'] != 'get' and self.infos['method'] != 'post' and self.infos['method'] != 'delete' and \
                self.infos['method'] != 'patch':
            ctx.log.error('non-support ' + flow.request.method)
            return

        self.infos['params'] = {name: value for name, value in flow.request.query.fields}
        self.infos['cookies'] = {name: value for name, value in flow.request.cookies.fields}
        # remove cookies from header
        self.infos['headers'] = {name.lower(): value for name, value in flow.request.headers.items() if
                                 name.lower() != 'cookie'}

        body = {}
        typess = ''
        if self.infos['method'] == 'get':
            typess = 'get'
            body = {}
        elif 'content-type' in self.infos['headers'] and self.infos['headers']['content-type'].find(
                'multipart/form-data') != -1:
            ctx.log.error('multipart  ' + self.infos['headers']['content-type'] + self.infos['url'])
            typess = 'multipart'
            for name, value in flow.request.multipart_form.fields:
                # only try decode with utf-8
                try:
                    n = name.decode('utf-8')
                except Exception as e:
                    continue
                try:
                    v = value.decode('utf-8')
                    if len(v) > 2048:
                        ctx.log.error('multipart  possible file content' + n)
                        v = v[:2048]
                    body[n] = v
                except Exception as e:
                    pass

        else:
            body = {}
            try:
                # decoded with both content-encoding header (e.g. gzip) and content-type header charset.
                c = flow.request.get_text().strip()
            except Exception as e:
                c = 'error'
                ctx.log.error('get_text error ' + self.infos['url'] + str(self.infos['headers']))

            # body with nothing
            if c == '':
                typess = 'form'
                body = {}

            # json: list and map
            elif (c.startswith('{') and c.endswith('}')) or (c.startswith('[') and c.endswith(']')):
                typess = 'json'
                try:
                    c = json.loads(c)
                    if isinstance(c, dict):
                        body = c
                    elif isinstance(c, list):
                        # simplify
                        for i in c:
                            if isinstance(i, dict):
                                body = {**body, **i}
                except Exception as e:
                    ctx.log.error('json error ' + e + self.infos['url'])
                    body = {'plain': c}
                    typess = 'plain'

            # application/x-www-form-urlencoded
            elif c.find('=') != -1 and not c.endswith('='):
                typess = 'form'
                c = c.rstrip('&')
                tp = c.split('&')
                for p in tp:
                    q = p.split('=')
                    if len(q) == 2:
                        body[q[0]] = q[1]
                    else:
                        ctx.log.error('form error ' + self.infos['url'])
                        body = {'plain': c}
                        typess = 'plain'
                        break

            else:
                try:
                    # base64(json)
                    cc = base64.b64decode(c)
                    cc = cc.decode('utf-8')
                    if (cc.startswith('{') and cc.endswith('}')) or (cc.startswith('[') and cc.endswith(']')):
                        typess = 'jsonb64'
                        cc = json.loads(cc)
                        if isinstance(cc, list):
                            for i in cc:
                                if isinstance(i, dict):
                                    body = {**body, **i}
                        elif isinstance(cc, dict):
                            body = cc
                    else:
                        body = {'plain': c}
                        typess = 'plain'
                        ctx.log.error('plain ' + self.infos['url'])
                except Exception as e:
                    body = {'plain': c}
                    typess = 'plain'
                    ctx.log.error('plain ' + self.infos['url'])

        self.infos['type'] = typess
        self.infos['data'] = body

        # save to file
        self.construction_py()

    def construction_py(self):
        """
            构造PY文件
        """
        # 删除域名
        url = self.infos['url'].replace(self.filter_url, "")
        filename = "test_" + self.infos['url'].split('/')[-2] + '_' + self.infos['url'].split('/')[-1]
        template = """import allure
from config.routes import *


@allure.feature("登录")
class Test%s(object):
    @allure.story("首页列表")
    def test_%s(self, env, common_client):
        http, common_api = common_client
        request_data = {
            "method": "%s",
            "route": "%s",
            "RequestData": {
                "params": %s,
                "data": %s
            },
            "Validate": {
                "expect_code": %s,
                "result_check": '"code": 200'
                    }
            }
    
        http.send_request(**request_data)
    """ % (
            (filename.title()).replace("_", ""), filename, self.infos['method'], url, self.infos['params'],
            self.infos['data'],
            self.infos['code'])

        # save file
        filename = self.mitm_path + '/' + filename + '.py'
        ctx.log.info("filename:{}".format(filename))
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(template)

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        pass


addons = [
    PacketSaver(filter_url="https://act.test.metadl.com")
    # PacketSaver(filter_url="https://act.test.metadl.com")
]

# 控制台执行
# mitmdump -s ./tools/mitm.py
