# API_AUTO

#### pytest+requests+allure框架，api自动化测试框架

## 框架阅读：
目录结构
 - api_base 驱动层目录
   - base_http.py 封装http请求方法，建议接口封装时继承该类
   - kwargs_model.py 接口参数模板在base_http.py中初始化，也可以单独调用
 - api_object 接口对象目录，存放接口封装
 - business_flow 业务流程目录，存放接口调用实现业务流
 - cases 测试用例目录
 - config 配置文件目录
   - debug 开发环境
     - config.yaml 配置文件
   - prod 生产环境
     - config.yaml 配置文件
   - test 测试环境
     - config.yaml 配置文件
   - config.yaml 全局配置文件
   - routes.py 接口路由管理
 - files 项目文件目录
 - logs 日志文件目录（不提交gitlab）
 - result 测试报告目录（不提交gitlab）
 - test_data 测试数据目录
 - tools 工具模块目录
   - allure_result.py 统计allure数据
   - Assertions.py 自定义断言
   - cache.py 缓存工具
   - db_operate.py 数据库封装
   - env_instance.py 环境创建
   - json_test.py json封装
   - Logger.py 日志封装
   - mitm.py mitmproxy代理抓包工具
   - result.py 结果校验封装
   - utils.py 其他模块
   - yaml_driver.py yaml驱动
 - conftest.py 自定义全局插件及hook函数配置，业务相关插件请定义到cases中的conftest.py中
 - const.py 项目目录管理
 - pytest.ini pytest配置
 - run_case.py 项目执行入口

使用说明
1. 接口封装步骤
   1. 创建接口类继承HttpRequest类
   2. 创建基础请求方法
   3. 调用self._request_model填写模板参数，模板填写参考api_demo.py，以及kwargs_model.py中的参数说明和使用示例
   4. 添加日志只需调用self.logger即可
   5. 调用built_dict方法转换模板为字典并发起请求
   6. 根据具体环境中config.yaml的need_log字段判断是否打印接口响应信息日志
   7. 标准接口封装中只进行响应码、结果信息等基础字段断言
2. 调用接口封装业务
   1. 为了简化接口的调用流程，可以在接口类中封装接口的特殊调用场景，并补充断言
   2. 统一在business_flow目录下封装业务流程
   3. 每个业务流程最好添加一个步骤说明 with allure.step("步骤说明"):
   4. 粒度：一个流程一个方法，一个方法一个step
   5. 业务流程中不进行断言，将最终数据返回给用例层
3. 用例编写规范
   1. suite上方添加@allure.feature('模块名称')
   2. 用例上方添加@allure.story('模块-功能点')
   3. 参数化时建议中文填写ids参数给用例标识，方便阅读
   4. 用例层根据业务流程返回数据进行断言
4. 编码规范
   1. https://deepwisdom.feishu.cn/wiki/wikcnMHi0xzQ6ek7hfeLHfzRhTP

## 全局
1. 目前项目加了gitlab_ci，如果不想自动调用CI，在commit时备注写上[skip ci]

