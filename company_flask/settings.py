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

# 创投资讯分类标签字典
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

# 数据地图各省份数据
map_dict = {
    'all': [{'name': '-', 'value': 2}, {'name': '上海', 'value': 28952}, {'name': '云南', 'value': 2105}, {'name': '内蒙古', 'value': 1023}, {'name': '北京', 'value': 49170}, {'name': '吉林', 'value': 2540}, {'name': '四川', 'value': 18894}, {'name': '天津', 'value': 15764}, {'name': '宁夏', 'value': 573}, {'name': '安徽', 'value': 19507}, {'name': '山东', 'value': 34796}, {'name': '山西', 'value': 11369}, {'name': '广东', 'value': 99934}, {'name': '广西', 'value': 3154}, {'name': '新疆', 'value': 1300}, {'name': '江苏', 'value': 68982}, {'name': '江西', 'value': 14340}, {'name': '河北', 'value': 9656}, {'name': '河南', 'value': 18804}, {'name': '浙江', 'value': 35509}, {'name': '海南', 'value': 794}, {'name': '湖北', 'value': 15865}, {'name': '湖南', 'value': 12467}, {'name': '甘肃', 'value': 1292}, {'name': '福建', 'value': 13387}, {'name': '西藏', 'value': 83}, {'name': '贵州', 'value': 1930}, {'name': '辽宁', 'value': 11732}, {'name': '重庆', 'value': 4857}, {'name': '陕西', 'value': 13034}, {'name': '青海', 'value': 247}, {'name': '黑龙江', 'value': 1583}],
    'gaoxin': [{'name': '香港', 'value': ''}, {'name': '澳门', 'value': ''}, {'name': '上海', 'value': 12669}, {'name': '云南', 'value': 1459}, {'name': '内蒙古', 'value': 897}, {'name': '北京', 'value': 26244}, {'name': '吉林', 'value': 1675}, {'name': '四川', 'value': 5640}, {'name': '天津', 'value': 6051}, {'name': '宁夏', 'value': 206}, {'name': '安徽', 'value': 6569}, {'name': '山东', 'value': 11445}, {'name': '山西', 'value': 2359}, {'name': '广东', 'value': 50224}, {'name': '广西', 'value': 2360}, {'name': '新疆', 'value': 661}, {'name': '江苏', 'value': 24972}, {'name': '江西', 'value': 5101}, {'name': '河北', 'value': 7669}, {'name': '河南', 'value': 4750}, {'name': '浙江', 'value': 16279}, {'name': '海南', 'value': 719}, {'name': '湖北', 'value': 6790}, {'name': '湖南', 'value': 6235}, {'name': '甘肃', 'value': 1029}, {'name': '福建', 'value': 4765}, {'name': '西藏', 'value': 68}, {'name': '贵州', 'value': 1603}, {'name': '辽宁', 'value': 5091}, {'name': '重庆', 'value': 3117}, {'name': '陕西', 'value': 4309}, {'name': '青海', 'value': 183}, {'name': '黑龙江', 'value': 1212}],
    'kj_xing': [{'name': '-', 'value': 1}, {'name': '上海', 'value': 11237}, {'name': '云南', 'value': 1}, {'name': '内蒙古', 'value': 1}, {'name': '北京', 'value': 10741}, {'name': '四川', 'value': 12515}, {'name': '天津', 'value': 8885}, {'name': '安徽', 'value': 7619}, {'name': '山东', 'value': 15818}, {'name': '山西', 'value': 8480}, {'name': '广东', 'value': 42952}, {'name': '江苏', 'value': 38795}, {'name': '江西', 'value': 7593}, {'name': '河南', 'value': 12050}, {'name': '浙江', 'value': 15573}, {'name': '海南', 'value': 1}, {'name': '湖北', 'value': 5671}, {'name': '湖南', 'value': 5079}, {'name': '福建', 'value': 6221}, {'name': '辽宁', 'value': 5257}, {'name': '重庆', 'value': 1}, {'name': '陕西', 'value': 7760}],
    'dujiaoshou': [{'name': '上海', 'value': 79}, {'name': '北京', 'value': 146}, {'name': '四川', 'value': 4}, {'name': '天津', 'value': 7}, {'name': '宁夏', 'value': 1}, {'name': '安徽', 'value': 5}, {'name': '山东', 'value': 24}, {'name': '广东', 'value': 72}, {'name': '新疆', 'value': 1}, {'name': '江苏', 'value': 135}, {'name': '江西', 'value': 5}, {'name': '浙江', 'value': 36}, {'name': '湖北', 'value': 8}, {'name': '湖南', 'value': 1}, {'name': '福建', 'value': 23}, {'name': '贵州', 'value': 2}, {'name': '辽宁', 'value': 1}, {'name': '重庆', 'value': 1}, {'name': '陕西', 'value': 5}],
    'js_xianjin': [{'name': '上海', 'value': 216}, {'name': '云南', 'value': 3}, {'name': '北京', 'value': 131}, {'name': '吉林', 'value': 13}, {'name': '四川', 'value': 36}, {'name': '天津', 'value': 23}, {'name': '安徽', 'value': 7}, {'name': '山东', 'value': 24}, {'name': '广东', 'value': 67}, {'name': '广西', 'value': 1}, {'name': '江苏', 'value': 127}, {'name': '河北', 'value': 3}, {'name': '河南', 'value': 3}, {'name': '浙江', 'value': 29}, {'name': '海南', 'value': 4}, {'name': '湖北', 'value': 47}, {'name': '湖南', 'value': 1}, {'name': '福建', 'value': 7}, {'name': '贵州', 'value': 1}, {'name': '重庆', 'value': 2}, {'name': '陕西', 'value': 19}, {'name': '黑龙江', 'value': 5}],
    'dengling': [{'name': '上海', 'value': 541}, {'name': '云南', 'value': 17}, {'name': '内蒙古', 'value': 25}, {'name': '北京', 'value': 10757}, {'name': '吉林', 'value': 47}, {'name': '四川', 'value': 228}, {'name': '天津', 'value': 375}, {'name': '宁夏', 'value': 11}, {'name': '安徽', 'value': 305}, {'name': '山东', 'value': 1013}, {'name': '山西', 'value': 28}, {'name': '广东', 'value': 1249}, {'name': '广西', 'value': 206}, {'name': '新疆', 'value': 23}, {'name': '江苏', 'value': 1469}, {'name': '江西', 'value': 234}, {'name': '河北', 'value': 88}, {'name': '河南', 'value': 252}, {'name': '浙江', 'value': 605}, {'name': '海南', 'value': 11}, {'name': '湖北', 'value': 1314}, {'name': '湖南', 'value': 280}, {'name': '甘肃', 'value': 24}, {'name': '福建', 'value': 236}, {'name': '西藏', 'value': 9}, {'name': '贵州', 'value': 33}, {'name': '辽宁', 'value': 212}, {'name': '重庆', 'value': 197}, {'name': '陕西', 'value': 177}, {'name': '青海', 'value': 6}, {'name': '黑龙江', 'value': 40}],
    'chuangxin': [{'name': '北京', 'value': 28}, {'name': '广东', 'value': 6}],
    'kj_xiao': [{'name': '上海', 'value': 396}, {'name': '云南', 'value': 12}, {'name': '内蒙古', 'value': 22}, {'name': '北京', 'value': 20}, {'name': '吉林', 'value': 608}, {'name': '四川', 'value': 19}, {'name': '天津', 'value': 14}, {'name': '宁夏', 'value': 63}, {'name': '安徽', 'value': 475}, {'name': '山东', 'value': 86}, {'name': '山西', 'value': 23}, {'name': '广东', 'value': 1976}, {'name': '广西', 'value': 5}, {'name': '新疆', 'value': 35}, {'name': '江苏', 'value': 198}, {'name': '江西', 'value': 7}, {'name': '河北', 'value': 281}, {'name': '河南', 'value': 89}, {'name': '浙江', 'value': 37}, {'name': '海南', 'value': 11}, {'name': '湖北', 'value': 1220}, {'name': '湖南', 'value': 351}, {'name': '甘肃', 'value': 17}, {'name': '福建', 'value': 977}, {'name': '贵州', 'value': 11}, {'name': '辽宁', 'value': 25}, {'name': '重庆', 'value': 30}, {'name': '陕西', 'value': 65}, {'name': '青海', 'value': 2}, {'name': '黑龙江', 'value': 3}],
    'zhaunjing': [{'name': '上海', 'value': 2982}, {'name': '云南', 'value': 8}, {'name': '内蒙古', 'value': 10}, {'name': '北京', 'value': 11}, {'name': '吉林', 'value': 100}, {'name': '四川', 'value': 14}, {'name': '天津', 'value': 17}, {'name': '宁夏', 'value': 220}, {'name': '安徽', 'value': 2793}, {'name': '山东', 'value': 3969}, {'name': '山西', 'value': 326}, {'name': '广东', 'value': 1501}, {'name': '新疆', 'value': 440}, {'name': '江苏', 'value': 1380}, {'name': '江西', 'value': 1161}, {'name': '河北', 'value': 1022}, {'name': '河南', 'value': 669}, {'name': '浙江', 'value': 87}, {'name': '海南', 'value': 1}, {'name': '湖北', 'value': 11}, {'name': '湖南', 'value': 14}, {'name': '甘肃', 'value': 83}, {'name': '福建', 'value': 733}, {'name': '西藏', 'value': 1}, {'name': '辽宁', 'value': 222}, {'name': '重庆', 'value': 507}, {'name': '陕西', 'value': 430}, {'name': '青海', 'value': 20}, {'name': '黑龙江', 'value': 2}],
    'chuying': [{'name': '上海', 'value': 1}, {'name': '北京', 'value': 478}, {'name': '天津', 'value': 1}, {'name': '广东', 'value': 3}, {'name': '江苏', 'value': 794}, {'name': '江西', 'value': 1}, {'name': '河南', 'value': 515}, {'name': '浙江', 'value': 524}, {'name': '海南', 'value': 1}, {'name': '重庆', 'value': 1}],
    'js_qiye': [{'name': '上海', 'value': 621}, {'name': '云南', 'value': 506}, {'name': '内蒙古', 'value': 4}, {'name': '北京', 'value': 313}, {'name': '吉林', 'value': 31}, {'name': '四川', 'value': 166}, {'name': '天津', 'value': 228}, {'name': '宁夏', 'value': 29}, {'name': '安徽', 'value': 1382}, {'name': '山东', 'value': 1164}, {'name': '山西', 'value': 11}, {'name': '广东', 'value': 1381}, {'name': '广西', 'value': 403}, {'name': '新疆', 'value': 36}, {'name': '江苏', 'value': 434}, {'name': '江西', 'value': 116}, {'name': '河北', 'value': 168}, {'name': '河南', 'value': 139}, {'name': '浙江', 'value': 869}, {'name': '海南', 'value': 1}, {'name': '湖北', 'value': 533}, {'name': '湖南', 'value': 337}, {'name': '甘肃', 'value': 13}, {'name': '福建', 'value': 211}, {'name': '贵州', 'value': 204}, {'name': '辽宁', 'value': 788}, {'name': '重庆', 'value': 17}, {'name': '陕西', 'value': 79}, {'name': '青海', 'value': 12}, {'name': '黑龙江', 'value': 71}],
    'fuhuaqi': [{'name': '上海', 'value': 29}, {'name': '云南', 'value': 26}, {'name': '内蒙古', 'value': 4}, {'name': '北京', 'value': 24}, {'name': '吉林', 'value': 26}, {'name': '四川', 'value': 91}, {'name': '天津', 'value': 35}, {'name': '宁夏', 'value': 11}, {'name': '安徽', 'value': 56}, {'name': '山东', 'value': 196}, {'name': '山西', 'value': 44}, {'name': '广东', 'value': 95}, {'name': '广西', 'value': 29}, {'name': '新疆', 'value': 28}, {'name': '江苏', 'value': 265}, {'name': '江西', 'value': 34}, {'name': '河北', 'value': 97}, {'name': '河南', 'value': 73}, {'name': '浙江', 'value': 114}, {'name': '海南', 'value': 24}, {'name': '湖北', 'value': 128}, {'name': '湖南', 'value': 31}, {'name': '甘肃', 'value': 27}, {'name': '福建', 'value': 21}, {'name': '贵州', 'value': 6}, {'name': '辽宁', 'value': 7}, {'name': '重庆', 'value': 30}, {'name': '陕西', 'value': 57}, {'name': '青海', 'value': 8}, {'name': '黑龙江', 'value': 143}],
    'js_chuangxin': [{'name': '上海', 'value': 27}, {'name': '云南', 'value': 10}, {'name': '内蒙古', 'value': 11}, {'name': '北京', 'value': 40}, {'name': '吉林', 'value': 9}, {'name': '四川', 'value': 62}, {'name': '天津', 'value': 22}, {'name': '宁夏', 'value': 7}, {'name': '安徽', 'value': 180}, {'name': '山东', 'value': 241}, {'name': '山西', 'value': 9}, {'name': '广东', 'value': 53}, {'name': '广西', 'value': 99}, {'name': '新疆', 'value': 24}, {'name': '江苏', 'value': 47}, {'name': '江西', 'value': 10}, {'name': '河北', 'value': 142}, {'name': '河南', 'value': 144}, {'name': '浙江', 'value': 73}, {'name': '海南', 'value': 2}, {'name': '湖北', 'value': 28}, {'name': '湖南', 'value': 31}, {'name': '甘肃', 'value': 39}, {'name': '福建', 'value': 28}, {'name': '西藏', 'value': 1}, {'name': '贵州', 'value': 38}, {'name': '辽宁', 'value': 21}, {'name': '重庆', 'value': 156}, {'name': '陕西', 'value': 22}, {'name': '青海', 'value': 1}, {'name': '黑龙江', 'value': 60}],
    'zhongchuang': [{'name': '上海', 'value': 85}, {'name': '云南', 'value': 30}, {'name': '内蒙古', 'value': 36}, {'name': '北京', 'value': 155}, {'name': '吉林', 'value': 16}, {'name': '四川', 'value': 56}, {'name': '天津', 'value': 73}, {'name': '宁夏', 'value': 6}, {'name': '安徽', 'value': 47}, {'name': '山东', 'value': 188}, {'name': '山西', 'value': 43}, {'name': '广东', 'value': 221}, {'name': '广西', 'value': 25}, {'name': '新疆', 'value': 34}, {'name': '江苏', 'value': 204}, {'name': '江西', 'value': 39}, {'name': '河北', 'value': 94}, {'name': '河南', 'value': 44}, {'name': '浙江', 'value': 134}, {'name': '海南', 'value': 7}, {'name': '湖北', 'value': 67}, {'name': '湖南', 'value': 41}, {'name': '甘肃', 'value': 28}, {'name': '福建', 'value': 62}, {'name': '西藏', 'value': 4}, {'name': '贵州', 'value': 17}, {'name': '辽宁', 'value': 52}, {'name': '重庆', 'value': 41}, {'name': '陕西', 'value': 66}, {'name': '青海', 'value': 6}, {'name': '黑龙江', 'value': 30}],
    'yinxing': [{'name': '山东', 'value': 514}, {'name': '江苏', 'value': 28}, {'name': '浙江', 'value': 1004}, {'name': '重庆', 'value': 20}],
    'minying': [{'name': '上海', 'value': 2}, {'name': '天津', 'value': 1}, {'name': '宁夏', 'value': 1}, {'name': '安徽', 'value': 2}, {'name': '山东', 'value': 2}, {'name': '山西', 'value': 781}, {'name': '广东', 'value': 4}, {'name': '江苏', 'value': 21424}, {'name': '河北', 'value': 1}, {'name': '浙江', 'value': 3}],
    'niuling': [{'name': '重庆', 'value': 680}],
    'zhaunjing_xiao': [{'name': '上海', 'value': 69}, {'name': '云南', 'value': 33}, {'name': '内蒙古', 'value': 13}, {'name': '北京', 'value': 82}, {'name': '吉林', 'value': 15}, {'name': '四川', 'value': 63}, {'name': '天津', 'value': 33}, {'name': '宁夏', 'value': 19}, {'name': '安徽', 'value': 69}, {'name': '山东', 'value': 114}, {'name': '山西', 'value': 46}, {'name': '广东', 'value': 134}, {'name': '广西', 'value': 26}, {'name': '新疆', 'value': 18}, {'name': '江苏', 'value': 134}, {'name': '江西', 'value': 39}, {'name': '河北', 'value': 92}, {'name': '河南', 'value': 76}, {'name': '浙江', 'value': 145}, {'name': '海南', 'value': 12}, {'name': '湖北', 'value': 48}, {'name': '湖南', 'value': 66}, {'name': '甘肃', 'value': 32}, {'name': '福建', 'value': 103}, {'name': '贵州', 'value': 15}, {'name': '辽宁', 'value': 56}, {'name': '重庆', 'value': 57}, {'name': '陕西', 'value': 45}, {'name': '青海', 'value': 9}, {'name': '黑龙江', 'value': 17}],
}