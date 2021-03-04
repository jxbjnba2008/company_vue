from flask import Flask
from flask_cors import CORS
from flask import jsonify, request
from company import company
import json
# from flask_cache import Cache
from gevent import monkey
from gevent.pywsgi import WSGIServer
from settings import TEC


monkey.patch_all()

app = Flask(__name__)
CORS(app)
# cache = Cache(app, config={'CACHE_TYPE': 'simple'})


# def make_cache_key(*args, **kwargs):
#     """缓存key值"""
#     path = request.path
#     args = str(hash(frozenset(request.args.items())))
#     return (path + args).encode('utf-8')

@app.route('/<string:company_cate>', methods=['GET'])
# @cache.cached(timeout=50)
def get_cates_infos(company_cate):
    """企业类型"""
    company_type = TEC.get(company_cate)

    if request.method == 'GET':
        print("company_type", company_type)

        companys = company()
        sql_data = companys.get_company_cates(company_type)
        resData = {
            "resCode": 0, # 非0即错误 1
            "data": sql_data,# 数据位置，一般为数组
            "message": '获取{}企业'.format(company_type)
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

# 搜索接口
@app.route('/search', methods=['POST'])
def search_infos():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']

        companys = company()
        search_data = companys.search_infos_by_key(key)
        if len(search_data) == 0:
            resData = {
                "resCode": 0, # 非0即错误 1
                "data": [],# 数据位置，一般为数组
                "message": '数据为空'
            }
            return jsonify(resData)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": search_data,# 数据位置，一般为数组
            "message": '搜索结果'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

@app.route('/', methods=['POST'])
# @cache.cached(timeout=20, key_prefix=make_cache_key)
def home_info():
    """主页上市、融资信息"""
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']

        companys = company()
        sql_data = companys.get_home_info(key)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": sql_data,# 数据位置，一般为数组
            "message": '搜索结果'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

@app.route('/<string:company_cate>/page', methods=['POST'])
def page_info(company_cate):
    """公司列表翻页"""
    if request.method == 'POST':
        company_type = TEC.get(company_cate)
        get_data = json.loads(request.get_data(as_text=True))
        pageNo = get_data['pageNo']
        pageSize = get_data['pageSize']
        # key = request.form.get('key')
        print('-----pageNo-----{}'.format(pageNo))

        companys = company()
        search_data = companys.get_companys_page(company_type, pageNo, pageSize)
        # print(search_data)
        if len(search_data) == 0:
            resData = {
                "resCode": 0, # 非0即错误 1
                "data": [],# 数据位置，一般为数组
                "message": '数据为空'
            }
            return jsonify(resData)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": search_data,# 数据位置，一般为数组
            "message": '搜索结果'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

@app.route('/info_more/shangshi/page', methods=['POST'])
def page_ipo_info():
    """上市信息列表翻页"""
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        pageNo = get_data['pageNo']
        pageSize = get_data['pageSize']
        # key = request.form.get('key')
        print('-----pageNo-----{}'.format(pageNo))

        companys = company()
        search_data = companys.get_ipo_page(pageNo, pageSize)
        # print(search_data)
        if len(search_data) == 0:
            resData = {
                "resCode": 0, # 非0即错误 1
                "data": [],# 数据位置，一般为数组
                "message": '数据为空'
            }
            return jsonify(resData)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": search_data,# 数据位置，一般为数组
            "message": '搜索结果'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

@app.route('/info_more/hangye/page', methods=['POST'])
def page_hangye_info():
    """行业分析列表翻页"""
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        pageNo = get_data['pageNo']
        pageSize = get_data['pageSize']
        # key = request.form.get('key')
        print('-----pageNo-----{}'.format(pageNo))

        companys = company()
        search_data = companys.get_hangye_page(pageNo, pageSize)
        # print(search_data)
        if len(search_data) == 0:
            resData = {
                "resCode": 0, # 非0即错误 1
                "data": [],# 数据位置，一般为数组
                "message": '数据为空'
            }
            return jsonify(resData)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": search_data,# 数据位置，一般为数组
            "message": '搜索结果'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

@app.route('/info_more/hangye/<string:id>', methods=['GET'])
def hangye_detail(id):
    """行业分析详细内容"""
    if request.method == 'GET':
        companys = company()
        search_data = companys.get_hangye_detail(id)
        # 处理图片显示大小问题
        search_data['html_content'] = search_data['html_content'].replace('<img', '<img style=\'height: auto;max-width: 100%;\'')

        if len(search_data) == 0:
            resData = {
                "resCode": 0, # 非0即错误 1
                "data": [],# 数据位置，一般为数组
                "message": '数据为空'
            }
            return jsonify(resData)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": search_data,# 数据位置，一般为数组
            "message": '搜索结果'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

@app.route('/info_more/death/page', methods=['POST'])
def page_death_info():
    """死亡公司列表翻页"""
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        pageNo = get_data['pageNo']
        pageSize = get_data['pageSize']
        # key = request.form.get('key')
        print('-----pageNo-----{}'.format(pageNo))

        companys = company()
        search_data = companys.get_death_page(pageNo, pageSize)
        # print(search_data)
        if len(search_data) == 0:
            resData = {
                "resCode": 0, # 非0即错误 1
                "data": [],# 数据位置，一般为数组
                "message": '数据为空'
            }
            return jsonify(resData)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": search_data,# 数据位置，一般为数组
            "message": '搜索结果'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

@app.route('/info_more/rongzi/page', methods=['POST'])
def page_rongzi_info():
    """融资信息列表翻页"""
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        pageNo = get_data['pageNo']
        pageSize = get_data['pageSize']
        # key = request.form.get('key')
        print('-----pageNo-----{}'.format(pageNo))

        companys = company()
        search_data = companys.get_rongzi_page(pageNo, pageSize)
        # print(search_data)
        if len(search_data) == 0:
            resData = {
                "resCode": 0, # 非0即错误 1
                "data": [],# 数据位置，一般为数组
                "message": '数据为空'
            }
            return jsonify(resData)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": search_data,# 数据位置，一般为数组
            "message": '搜索结果'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

@app.route('/<string:tag>/fenlei/page', methods=['POST'])
def page_rongzi_feilei(tag):
    """融资信息分类列表翻页"""
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        pageNo = get_data['pageNo']
        pageSize = get_data['pageSize']
        # key = request.form.get('key')
        print('-----pageNo-----{}'.format(pageNo))

        companys = company()
        search_data, num = companys.get_rongzi_fenlei(pageNo, pageSize, tag)
        # print(search_data)
        if len(search_data) == 0:
            resData = {
                "resCode": 0, # 非0即错误 1
                "data": [],# 数据位置，一般为数组
                "message": '数据为空'
            }
            return jsonify(resData)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": search_data, # 数据位置，一般为数组
            "message": '搜索结果',
            "num": int(num / 10) if num % 10 == 0 else int(num / 10) + 1 # 数据量
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

@app.route('/company_detail/<string:company_name>', methods=['POST'])
# @cache.cached(timeout=50, key_prefix=make_cache_key)
def company_detail_info(company_name):
    """企业工商信息页"""
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']

        companys = company()
        sql_data = companys.get_company_detail(company_name, key)

        resData = {
            "resCode": 0, # 非0即错误 1
            "data": sql_data,# 数据位置，一般为数组
            "message": '搜索结果'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)

if __name__ == '__main__':
    # print(app.url_map)
    # http_server = WSGIServer(('127.0.0.1', int(5000)), app)
    # http_server.serve_forever()
    # app.run(threaded=True)
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    http_server = WSGIServer(('127.0.0.1', int(5000)), app)
    http_server.serve_forever()
    # app.run()