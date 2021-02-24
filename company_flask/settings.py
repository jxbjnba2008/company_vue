# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Settings
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Mysql configurations
MYSQL_HOST = '218.94.82.249'
MYSQL_PORT = 8015
MYSQL_USER = 'rhino'
MYSQL_PASSWORD = 'rhino'
MYSQL_DB = 'OceanSpider_Base'

# 企业字典
TEC = {
'gaoxin': '高新技术企业',
'kj_xing': '科技型中小企业',
'dujiaoshou': '独角兽企业',
'js_xianjin': '技术先进型服务企业',
'dengling': '瞪羚企业',
'chuangxin': '创新型企业',
'kj_xiao': '科技小巨人企业',
'zhaunjing': '专精特新企业',
'chuying': '雏鹰企业',
'js_qiye': '企业技术中心',
'fuhuaqi': '科技企业孵化器',
'js_chuangxin': '技术创新示范企业',
'zhongchuang': '众创空间',
'yinxing': '隐形冠军企业',
'minying': '民营科技企业',
'niuling': '牛羚企业',
'zhaunjing_xiao': '专精特新小巨人企业',
}

# 分类标签字典
TAG = {
    'all': '不限',
    'ipo': 'IPO排队',
    'tz': '投资事件',
    'rs': '人事变动',
    'sg': '收购事件',
    'ss': '上市事件',
    'tc': '退出事件',
    'hx': '坏消息',
    'cp': '产品发布',
    'ts': '退市事件',
    'jg': '机构要闻',
    'mz': '募资事件',
    'vc': 'VC洞见',
    'hb': '合并事件',
}