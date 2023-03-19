# -*- coding: utf-8 -*-
# @File   : routes
# @Time   : 2022/3/28 16:50 
# @Author : 张福强

demo_route = '/user_center/get_user'

"""
    公共分类
"""
login_route = "https://sso.test.metadl.com/proxy/backend/login/local"
# 用户登录信息:
user_info_route = "/proxy/backend/user_info"
# socket信息整理:
socket_msg_route = "/proxy/backend/socket/msg"
# 仪表盘项目/数据集统计:
personal_dashboard_route = "/proxy/backend/personal/dashboard"
# 仪表盘项目/最近访问项目:
recent_projects_route = "/proxy/backend/recent/projects"
# 仪表盘项目/统计信息:
projects_stats_route = "/proxy/backend/projects/stats"
# 消息:
message_route = "/proxy/backend/message"
# 特征选择-数据EDA:
project_features_selection_route = "/proxy/backend/project/features/selection"
# 生成对外数据更新API:
gen_dataset_update_api_route = "/proxy/backend/gen_dataset_update_api"
# 数据统计:
dataset_state_route = "/proxy/backend/dataset/state"
# 数据集文本处理:
dataset_deal_settings_route = "/proxy/backend/dataset/deal/settings"
# 读消息:
message_read_route = "/proxy/backend/message/read"
# 场景标签列表:
scene_route = "/proxy/backend/scene"

"""
    数据集接口
"""

# 查询/删除dataset列表
dataset_list_route = "/proxy/backend/datawarehouse/datasets"
# 数据文件预览
dataset_file_preview_route = "/proxy/backend/file/preview"
# 数据源表预览
dataset_connection_table_preview_route = "/proxy/backend/connection/table/preview"
# 更新天机标注数据(LS)
dataset_ls_update_label_route = "/proxy/backend/dataset/ls/update/label"
# 生成数据集下载文件
dataset_generate_download_file_route = "/proxy/backend/generate/download/file"
# 脚本上传
dataset_script_upload_route = "/proxy/backend/dataset/script/upload"
# 数据集新增时间列格式
dataset_time_schema_route = "/proxy/backend/time/schema"
# 数据集更新API
dataset_update_api_route = "/proxy/backend/dataset/update/control_api"
# 数据集打开自动更新
dataset_automatic_update_route = "/proxy/backend/dataset/automatic/update"
# 数据集自动更新API
dataset_automatic_update_api_route = "/proxy/backend/dataset/automatic/update/control_api"
# 算子库算子列表
dataset_operator_model_route = "/proxy/backend/operator/model"
# 外链表预览
dataset_external_chain_table_review_route = "/proxy/backend/external/chain/table/review"
# 数据集项目关联
predict_relation_route = "/proxy/backend/dataset/project/relation"
# 数据源导入
dataset_connection_submit_route = "/proxy/backend/connection/submit"
# 数据库配置信息获取/新增/修改/删除
dataset_db_config_route = "/proxy/backend/db/config"
# 数据集标签-新增/查询/修改/删除标签
dataset_scene_route = "/proxy/backend/dataset/scene"
# 数据集标签修改
dataset_labels_route = "/proxy/backend/dataset/labels"
# 数据预处理异步
dataset_pretreatments_route = "/proxy/backend/dataset/pretreatments"
# 获取项目删除时可删除数据集列表
dataset_project_delete_dataset_route = "/proxy/backend/project/delete/dataset"
# 数据准备
dataset_prepare_route = "/proxy/backend/dataset/prepare"
# 数据断点上传
dataset_file_upload_route = "/proxy/backend/file/upload"
# 数据上传
dataset_upload_route = "/proxy/backend/dataset/upload"
# 数据集详情
datawarehouse_dataset_info_route = "/proxy/backend/datawarehouse/dataset/info"
# 获取/修改EDA
dataset_eda_route = "/proxy/backend/dataset/eda"
# 标注平台-获取/提交/弃用标注数据
datawarehouse_labelplatform_route = "/proxy/backend/datawarehouse/labelplatform"
# 数据预览
dataset_preview_route = "/proxy/backend/dataset/preview"
# 获取/修改数据集信息
datawarehouse_dataset_route = "/proxy/backend/datawarehouse/dataset"
# 预测数据上传
dataset_predict_dataset_upload_route = "/proxy/backend/predict/dataset/upload"
# 数据集更新设置
datawarehouse_dataset_settings_route = "/proxy/backend/datawarehouse/dataset/settings"
# 获取数据集列表
project_dataset_route = "/proxy/backend/project/dataset"
# 数据集复制
datawarehouse_dataset_copy_route = "/proxy/backend/datawarehouse/dataset/copy"
# 数据源表获取/连接
dataset_connection_test_route = "/proxy/backend/connection/test"
# 第三方数据集上传
thirdparty_dataset_upload_route = "/proxy/backend/thirdparty/dataset/upload"
# 数据集下载
datawarehouse_dataset_download_route = "/proxy/backend/datawarehouse/dataset/download"
# 数据集更新
autotable_dataset_upload_route = "/proxy/backend/autotable/dataset/update"
# 数据预处理
dataset_pretreatment_route = "/proxy/backend/dataset/pretreatment"
# 数据eda单列可视化
dataset_eda_column_route = "/proxy/backend/dataset/eda/column"
# 生成数据集下载资源
dataset_resources_generate_route = "/proxy/backend/generate/download/file"

"""
    项目模块
"""

# 新建项目、仪表盘项目列表、修改项目
projects_route = "/proxy/backend/projects"
# 获取项目列表
get_project_list_route = "/proxy/backend/projects/model"
# 最优搜索空间
best_trial_ss_route = "/proxy/backend/project/best/trial/ss"
# 项目详情页
project_detail_route = "/proxy/backend/project"
# 获取项目搜索空间
project_ss_route = "/proxy/backend/basic/searchspace/project/ss"
# 树可视化
tree_model_route = "/proxy/backend/tree/model"
# tensorboard
tensorboard_route = "/proxy/backend/tensorboard"
# 跳转Grafana服务监控
grafana_service_route = "/proxy/backend/grafana"
# badcase分析:
badcase_get_route = "/proxy/backend/badcase/get"
# badcase文件下载:
badcase_download_route = "/proxy/backend/badcase/download"
# 获取、修改项目高级设置
project_advance_settings_route = "/proxy/backend/project/advance_settings"
# 获取模态任务搜索空间
modal_task_ss_route = "/proxy/backend/basic/searchspace/modal/task/ss"
# 迭代效果
iterative_effect_route = "/proxy/backend/project/iterative/effect"
# 图像实验详情，特征与模型理解, cv_model_list
cv_model_list_route = "/proxy/backend/cv/model/list"
# 图像实验详情，特征与模型理解, cv_model_images
cv_model_image_route = "/proxy/backend/cv/model/image"
# 文本实验详情，特征与模型理解 attention_model_list
attention_model_list_route = "/proxy/backend/attention/model/list"
# 文本实验详情，特征与模型理解 attention_model
attention_model_route = "/proxy/backend/attention/model"
# 最优跑测结果
best_runntest_result_route = "/proxy/backend/project/model/optimal"
# 帕累托曲线
pareto_route = "/proxy/backend/project/trial/pareto"
# 预测列选择
predict_label_route = "/proxy/backend/project/predict/label"
# 项目收藏
project_collect_route = "/proxy/backend/project"
# 查询项目的方案
project_trial_scheme_route = "/proxy/backend/project/trial/scheme"
# 项目详情-模型应用-模型选择
predict_scheme_select_route = "/proxy/backend/project/model/select"
# 项目资源占用
monitor_pod_resource_route = "/proxy/backend/monitor/pod/resource"
# 项目训练GPU占用查询
monitor_train_resource_gpu_route = "/proxy/backend/monitor/train/resource/gpu"
# GPU资源收集补偿接口
monitor_train_resource_gpu_compensate_route = "/proxy/backend/monitor/train/resource/gpu/compensate"
# 项目主辅表关系获取、保存、修改
project_table_relation_route = "/proxy/backend/project/table/relationship"
# 项目详情-项目训练效果-模型详情
project_model_route = "/proxy/backend/project/model"
# 项目训练日志
project_train_log_route = "/proxy/backend/project/train/log"
# 项目实验日志
project_trial_log_route = "/proxy/backend/project/trial/log"
# 项目主辅表自动关联
table_autorelate_route = "/proxy/backend/project/table/autorelate"
# 预测训练数据集任务类型
predict_dataset_task_route = "/proxy/backend/predict/dataset/task"
# 项目训练数据集检测
project_train_dataset_route = "/proxy/backend/project/train/dataset"
# 目标列选择
project_col_selection_route = "/proxy/backend/project/col/selection"
# 模型下载
project_model_download_route = "/proxy/backend/project/model/download"
# 项目内数据集下载
project_dataset_download_route = "/proxy/backend/project/dataset/download"
# 迭代效果
project_iterative_model_route = "/proxy/backend/project/iterative/model"
# 测试集训练结果
project_testset_result_route = "/proxy/backend/project/testset/result"
# 项目详情-模型列表
project_models_route = "/proxy/backend/project/models"
# 项目训练
project_train_route = "/proxy/backend/project/train"
# 增加实验
project_add_train_route = "/proxy/backend/project/continue/train"
# 终止实验
project_terminate_train_route = "/proxy/backend/project/terminate/train"
# 项目周期自动训练
project_iteration_train_route = "/proxy/backend/project/iteration/train"
# 堆积图
stacking_chart_route = "/proxy/backend/stacking/chart"
# 特征与模型理解
feature_model_understanding_route = "/proxy/backend/feature/model/understanding"
# 应用-保存资源组
flow_op_setting_edit_route = "/proxy/backend/flow_op_setting/edit"

"""
    行业模板
"""

# 行业模版列表:
admin_industry_templates_route = "/proxy/backend/admin/industry/templates"
# 模板数据集匹配:
template_dataset_match_route = "/proxy/backend/template/dataset/match"
# 行业模版详情:
admin_industry_template_route = "/proxy/backend/admin/industry/template"
# 数据集自动匹配:
template_dataset_automatch_route = "/proxy/backend/template/dataset/automatch"

"""
    服务监控
"""
# 服务详情24小时统计
monitor_data_route = "/proxy/backend/monitor/data"
# 服务详情耗时按天统计
monitor_graph_responsetime_route = "/proxy/backend/monitor/graph/responsetime"
# 按天统计：服务调用量+项目离线验证
monitor_service_info_route = "/proxy/backend/monitor/service/info"

"""
    静态文件
"""

# 数据集文件下载:
static_datasets_route = "/proxy/backend/static/datasets/{path}/{filename}"

"""
    SDK
"""

# 创建应用:
sdk_createapp_route = "/proxy/backend/sdk/createapp"
# 获取Access Token:
appmng_token_route = "/proxy/backend/appmng/token"

"""
    数据处理
"""

# 数据预处理:
livy_spark_dev_route = "/proxy/backend/livy_spark_dev"
# livy_eda_hive:
livy_eda_hive_route = "/proxy/backend/livy_eda_hive"
# 数据集异常检测:
dataset_anomaly_detection_route = "/proxy/backend/dataset/anomaly/detection"
# hive db table 获取:
get_hive_db_info_route = "/proxy/backend/db_info/get_hive_db_info"

"""
    第三方应用 - 格物钛
"""

# 获取格物钛数据集信息:
graviti_dataset_route = "/proxy/backend/graviti/dataset"
# 多个文件同步格物钛数据集及标注信息到天机:
graviti_dataset_upload_route = "/proxy/backend/graviti/dataset/upload"
# 获取格物钛数是否登录:
graviti_user_route = "/proxy/backend/graviti/user"

"""
    数据集区分操作
"""

# 数据集增加分区:
dataset_add_partition_route = "/proxy/backend/dataset/add/partition"

"""
    模板
"""

# 取得所有模板:
project_template_get_all_route = "/proxy/backend/project_template/get_all"
# 取得指定模板:
project_template_get_route = "/proxy/backend/project_template/get"

"""
    FLOW
"""
# 编译 flow
flow_compile_deploy_route = "/control_api/v1/flow/compile/deploy"
# 部署 flow
flow_run_deploy_route = "/control_api/v1/flow/run/deploy"
# 取得指定项目的 flow
flow_config_get_route = "/proxy/backend/flow_config/get"
# 运行 flow
flow_run_route = "/control_api/v1/flow/run"
# 获取 flow 运行状态
flow_get_route = "/control_api/v1/flow/get"
# flow 编辑
flow_edit_flow_route = "/proxy/backend/flow_config/edit_flow"
# flow 新增
flow_add_flow_route = "/proxy/backend/flow_config/add_flow"
# 新增自定义算子
flow_config_custom_operator_add_route = "/control_api/v1/flow_config/custom_operator_add"
# 取得自定义算子
flow_custom_operator_get_route = "/control_api/v1/flow_config/custom_operator_get"
# 获取 flow_config 信息
internal_project_flow_config_route = "http://172.16.0.23:32001/internal/project/flow_config"
# flow 注册
register_flow_route = "http://172.16.0.23:32001/internal/flow/add"
# 获取 solver 列表
flow_config_solvers_route = "/control_api/v1/flow_config/solvers"
# 清除运行中的 flow
flow_delete_route = "/control_api/v1/flow/delete"
# FS 算子预览
fsApi_feature_store_preview_route = "/fsApi/feature_store/preview"
# flow dag 保存
flow_dag_route = "flow/dag"

"""
    服务管理
"""
# 项目服务列表
projects_service_route = "/proxy/backend/projects/service"
# 新建/修改/删除服务
service_route = "/proxy/backend/project/infer"
# 项目服务失败日志
service_infer_log_route = "/proxy/backend/project/infer/log"
# 服务详情
# 触发条件：列表是滚动加载的，同时url上可能会传服务 id，比如第一次加载了 20 条数据，
# 但是这 20 条数据里面没有 url 上的服务 id 对应的那条记录，这个时候就调用了这个接口传服务 id 去查服务详情
services_info_route = "/proxy/backend/test_services/info"
# 服务API获取
service_api_route = "/proxy/backend/project/service/api"
# 推理服务常驻修改
service_operation_route = "/proxy/backend/project/service/operation"
# 测试
service_test_route = "/proxy/backend/projects/test"

"""
    信息页面
"""
# 模态识别
get_modal_file_types_route = "/proxy/backend/basic/directory/getModalFileTypes"


#

"""
    参与者管理
"""

# 取得指定项目的参与者:
participant_management_get_route = "/proxy/backend/participant_management/get"

"""
    solver
"""

# solver实验结果:
solver_get_solver_lab_route = "/proxy/backend/solver/get_solver_lab"
# solver实验结果:
project_op_solver_train_route = "/proxy/backend/project/op/solver/train"
# solver实验结果: "/proxy/backend/"

"""
    标签管理
"""

# 取得所有选中标签:
label_management_get_all_selected_label_route = "/proxy/backend/label_management/get_all_selected_label"
# 标签批量新增:
label_management_batch_add_route = "/proxy/backend/label_management/batch_add"
# 取得指定 modal_type 下的所有默认标签:
label_management_get_all_default_label_route = "/proxy/backend/label_management/get_all_default_label"
# 取得所有标签名称:
label_management_get_all_label_name_route = "/proxy/backend/label_management/get_all_label_name"

"""
    流数据接入
"""

# 创建流数据集:
datawarehouse_dataset_streams_route = "/proxy/backend/datawarehouse/dataset/streams"
# json-schema生成:
jsonschema_convert_route = "/proxy/backend/jsonschema/convert"
# 用户流数据推送API获取:
datawarehouse_dataset_stream_api_route = "/proxy/backend/datawarehouse/dataset/stream/control_api"
# 更新流数据集更新方式:
datawarehouse_dataset_stream_switch_route = "/proxy/backend/datawarehouse/dataset/stream/switch"
# 增量落盘数据定时合并:
dataset_regular_update_route = "/proxy/backend/dataset/regular/update"

"""
    离线验证
"""
# 离线验证-预测数据集列表选择
dataset_predict_datasets_route = "/proxy/backend/predict/datasets"
# 离线预测详情/批量删除:
project_eval_route = "/proxy/backend/project/eval"
# 项目预测报告下载:
project_eval_zip_download_route = "/proxy/backend/project/eval/zip/download"
# 项目离线预测列表:
project_evals_route = "/proxy/backend/project/evals"
# 预测数据集下载:
project_eval_download_route = "/proxy/backend/project/eval/download"
# 离线验证滚动预测约束:
rolling_forecast_constraint_route = "/proxy/backend/rolling/forecast/constraint"

"""
    数据aPaas
"""

# 获取表格数据内容:
apaas_dataset_route = "/proxy/backend/apaas/dataset"
# 生成aPaaS数据下载:
apaas_download_file_route = "/proxy/backend/apaas/download/file"

"""
    Publish算子
"""

# 下载接口:
publish_download_file_route = "/proxy/backend/publish/download/file"
# publish算子静态文件地址查询:
publish_get_route = "/proxy/backend/publish/get"

"""
    CT项目接口
"""

# 取得自定义算子: "control_api/v1/flow_config/custom_operator_get"
# 新增自定义算子: "/control_api/v1/flow_config/custom_operator_add"
# 获取 solver 列表: "/control_api/v1/flow_config/solvers"
# 清除运行中的 flow: "/control_api/v1/flow/delete"
# 编译 flow: "/control_api/v1/flow/compile"
# 获取 flow 运行状态: "/control_api/v1/flow/get"
# 运行 flow: "/control_api/v1/flow/run"
# flow 注册: "/internal/flow/add"

"""
    访问控制
"""
# 用户权限
user_permission_route = "/proxy/backend/permission/resource/user/permission"

"""
    资源管理
"""
resource_pools_route = "/proxy/backend/compute_resource/pool"
resource_group_route = "/proxy/backend/compute_resource_group/create"
resource_group_list_route = "/proxy/backend/compute_resource_group/detail_list"
resource_group_edit_route = "/proxy/backend/compute_resource_group/edit"
