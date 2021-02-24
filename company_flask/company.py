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
            获取首页上市信息、融资信息
        """
        data_list = []
        if key == 'shangshi':
            sql = 'select * from qcc_ipodynamics order by time desc limit 5'
        else:
            sql = "select * from itjuzi_touzi where event_type='投资事件' order by event_time desc limit 5"
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
        data = []
        emp = {
            'company_type': company_type,
        }
        sql = "SELECT * from qcc_keji_company where company_type=:company_type limit {},{} ".format((pageNo-1)*pageSize, pageSize)
        rows = self.db.query(sql, **emp)
        for row in rows:
            data.append(row.as_dict())
        # print(data)
        if data:
            return data
        else:
            return None

    def get_ipo_page(self, pageNo, pageSize):
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

    def get_rongzi_page(self, pageNo, pageSize):
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
        """融资分类"""
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
        data = []

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
        # print(data)
        if data and key == 'base':
            return data[0]
        elif data and key != 'base':
            return data
        else:
            return None


if __name__ == '__main__':
    company = company()
    # books.get_books_page('xuanhuan', 0, 10)
    company.search_infos_by_key('蚂蚁')