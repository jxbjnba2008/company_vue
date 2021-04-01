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
        data = map_dict.get(map_type)
        if map_type == 'all':
            return '总企业数', data
        if map_type == 'gaoxin':
            return '高新技术企业', data
        if map_type == 'kj_xing':
            return '科技型中小企业', data
        if map_type == 'js_xianjin':
            return '技术先进型服务企业', data
        if map_type == 'dujiaoshou':
            return '独角兽企业', data
        if map_type == 'dengling':
            return '瞪羚企业', data
        if map_type == 'chuangxin':
            return '创新型企业', data
        if map_type == 'kj_xiao':
            return '科技小巨人企业', data
        if map_type == 'zhaunjing':
            return '专精特新企业', data
        if map_type == 'chuying':
            return '雏鹰企业', data
        if map_type == 'js_qiye':
            return '企业技术中心', data
        if map_type == 'fuhuaqi':
            return '科技企业孵化器', data
        if map_type == 'js_chuangxin':
            return '技术创新示范企业', data
        if map_type == 'zhongchuang':
            return '众创空间', data
        if map_type == 'yinxing':
            return '隐形冠军企业', data
        if map_type == 'minying':
            return '民营科技企业', data
        if map_type == 'niuling':
            return '牛羚企业', data
        if map_type == 'zhaunjing_xiao':
            return '专精特新小巨人企业', data

if __name__ == '__main__':
    company = company()
    # books.get_books_page('xuanhuan', 0, 10)
    # company.search_infos_by_key('蚂蚁')
    sql = "SELECT area as name, count(company_name) as value from jx_qcc_base where company_type='民营科技企业' GROUP BY area"
    rows = company.db.query(sql)
    data = []
    for row in rows:
        data.append(row.as_dict())
    print(data)