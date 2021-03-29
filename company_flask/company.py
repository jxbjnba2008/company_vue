import records
from settings import *

class company(object):

    def __init__(self):
        self.db = records.Database('mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB))

    def search_infos_by_key(self, key):
        """
            搜索栏，支持模糊查询
        """
        sql = "select * from qcc_keji_company where company_name like '%{}%' limit 10".format(key)
        rows = self.db.query(sql)
        data = []
        for row in rows:
            data.append(row.as_dict())
        # print(data)
        return data


    def get_home_info(self, key):
        """
            获取首页上市信息、融资信息、快讯信息
        """
        data_list = []
        if key == 'shangshi':
            sql = 'select * from qcc_ipodynamics order by time desc limit 5'
        elif key == 'rongzi':
            sql = "select * from itjuzi_touzi where event_type='投资事件' order by event_time desc limit 5"
        else:
            sql = 'select * from iyiou_briefing order by time desc limit 10'
        rows = self.db.query(sql)
        for row in rows:
            data_list.append(row.as_dict())
        # print(data_list)
        return data_list

    def get_company_cates(self, company_type):
        """
            获取对应企业类型的企业列表
        """
        em = {
            'company_type': company_type
        }
        company_list = []
        sql = 'select * from qcc_keji_company where company_type=:company_type limit 10'
        rows = self.db.query(sql, **em)
        for row in rows:
            company_list.append(row.as_dict())
        # print(company_list)
        return company_list

    def get_companys_page(self, company_type, pageNo, pageSize):
        """
            公司列表翻页
        """
        data = []
        emp = {
            'company_type': company_type,
        }
        sql = "SELECT * from qcc_keji_company where company_type=:company_type limit {},{} ".format((pageNo-1)*pageSize, pageSize)
        sql_num = "SELECT count(*) from qcc_keji_company where company_type=:company_type"

        rows = self.db.query(sql, **emp)
        num = self.db.query(sql_num, **emp)
        num = num[0]['count(*)']

        for row in rows:
            data.append(row.as_dict())
        # print(data)
        if data:
            return data, num
        else:
            return None

    def get_info_page(self, pageNo, pageSize):
        """
            快讯翻页
        """
        data = []
        sql = "SELECT * from iyiou_briefing order by time desc limit {},{} ".format((pageNo-1)*pageSize, pageSize)
        rows = self.db.query(sql)
        for row in rows:
            data.append(row.as_dict())
        # print(data)
        if data:
            return data
        else:
            return None

    def get_ipo_page(self, pageNo, pageSize):
        """
            IPO翻页
        """
        data = []
        sql = "SELECT * from qcc_ipodynamics order by time desc limit {},{} ".format((pageNo-1)*pageSize, pageSize)
        rows = self.db.query(sql)
        for row in rows:
            data.append(row.as_dict())
        # print(data)
        if data:
            return data
        else:
            return None

    def get_hangye_page(self, pageNo, pageSize):
        """
            行业翻页
        """
        data = []
        sql = "SELECT * from iyiou_analysis order by time desc limit {},{} ".format((pageNo-1)*pageSize, pageSize)
        rows = self.db.query(sql)
        for row in rows:
            data.append(row.as_dict())
        # print(data)
        if data:
            return data
        else:
            return None

    def get_hangye_detail(self, id):
        """
            获取行业详细内容
        """
        sql = "SELECT * from iyiou_analysis where url='{}'".format('https://www.iyiou.com/analysis/{}'.format(id))
        row = self.db.query(sql)
        data = row.as_dict()
        # print(data)
        if data:
            return data[0]
        else:
            return None

    def get_death_page(self, pageNo, pageSize):
        """
            获取死亡公司列表
        """
        data = []
        sql = "SELECT * from itjuzi_death order by death_time desc limit {},{} ".format((pageNo-1)*pageSize, pageSize)
        rows = self.db.query(sql)
        for row in rows:
            data.append(row.as_dict())
        # print(data)
        if data:
            return data
        else:
            return None

    def get_rongzi_page(self, pageNo, pageSize):
        """
            创投翻页
        """
        data = []
        sql = "SELECT * from itjuzi_touzi order by event_time desc limit {},{} ".format((pageNo-1)*pageSize, pageSize)
        rows = self.db.query(sql)
        for row in rows:
            data.append(row.as_dict())
        # print(data)
        if data:
            return data
        else:
            return None

    def get_rongzi_fenlei(self, pageNo, pageSize, tag):
        """
            创投分类
        """
        data = []
        event_type = TAG.get(tag)
        print(event_type)
        if event_type == '不限':
            sql_num = "SELECT count(*) from itjuzi_touzi"
            sql = "SELECT * from itjuzi_touzi order by event_time desc limit {},{} ".format((pageNo-1)*pageSize, pageSize)
        else:
            sql_num = "SELECT count(*) from itjuzi_touzi where event_type='{}'".format(event_type)
            sql = "SELECT * from itjuzi_touzi where event_type='{}' order by event_time desc limit {},{} ".format(event_type, (pageNo - 1) * pageSize, pageSize)
        rows = self.db.query(sql)
        num = self.db.query(sql_num)
        num = num[0]['count(*)']
        for row in rows:
            data.append(row.as_dict())
        # print(data)
        if data:
            return data, num
        else:
            return None

    def get_company_detail(self, company, key):
        """
            获取企业详细信息
        """
        data = []
        type_list = []

        em = {
            'company_name': company,
        }
        if key == 'base':
            sql = "SELECT * from jx_qcc_base where company_name=:company_name"
        elif key == 'change':
            sql = "SELECT * from jx_qcc_change where company_name=:company_name"
        else:
            sql = "SELECT * from jx_qcc_partner where company_name=:company_name"

        rows = self.db.query(sql, **em)
        for row in rows:
            data.append(row.as_dict())

        if data and key == 'base':
            type_list = [da.get('company_type') for da in data]
            return data[0], type_list
        elif data and key != 'base':
            return data, type_list
        else:
            return None

    def get_map_detail(self, map_type, key):
        """
            获取地图数据
        """
        return '高新技术企业', [{'name': '香港', 'value': 100}, {'name': '澳门', 'value': 10}, {'name': '上海', 'value': 12669}, {'name': '云南', 'value': 1459}, {'name': '内蒙古', 'value': 897}, {'name': '北京', 'value': 26244}, {'name': '吉林', 'value': 1675}, {'name': '四川', 'value': 5640}, {'name': '天津', 'value': 6051}, {'name': '宁夏', 'value': 206}, {'name': '安徽', 'value': 6569}, {'name': '山东', 'value': 11445}, {'name': '山西', 'value': 2359}, {'name': '广东', 'value': 50224}, {'name': '广西', 'value': 2360}, {'name': '新疆', 'value': 661}, {'name': '江苏', 'value': 24972}, {'name': '江西', 'value': 5101}, {'name': '河北', 'value': 7669}, {'name': '河南', 'value': 4750}, {'name': '浙江', 'value': 16279}, {'name': '海南', 'value': 719}, {'name': '湖北', 'value': 6790}, {'name': '湖南', 'value': 6235}, {'name': '甘肃', 'value': 1029}, {'name': '福建', 'value': 4765}, {'name': '西藏', 'value': 68}, {'name': '贵州', 'value': 1603}, {'name': '辽宁', 'value': 5091}, {'name': '重庆', 'value': 3117}, {'name': '陕西', 'value': 4309}, {'name': '青海', 'value': 183}, {'name': '黑龙江', 'value': 1212}]

if __name__ == '__main__':
    company = company()
    # books.get_books_page('xuanhuan', 0, 10)
    # company.search_infos_by_key('蚂蚁')
    sql = "SELECT area as name, count(company_name) as value from jx_qcc_base where company_type='高新技术企业' GROUP BY area"
    rows = company.db.query(sql)
    data = []
    for row in rows:
        data.append(row.as_dict())
    print(data)