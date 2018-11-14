from django.http import HttpResponse
from django.shortcuts import render
import utils.mysql_DBUtils
from utils.mysql_DBUtils import MyPymysqlPool
from utils.encoder import MyEncoder
import json


mysql = MyPymysqlPool("dbMysql")


def main(request):
    sql = "SELECT id,title FROM novel LIMIT 10;"
    result = mysql.getAll(sql)
    result = json.dumps(result, cls=MyEncoder, ensure_ascii=False, indent=4)
    result = json.loads(result)
    context = {'novel_list': result}
    return render(request, 'novel_list.html',  context)


# def chapter(request):
#     id = request.GET['id']
#     sql = "SELECT content FROM novel where id = %(id)s;"
#     param = {"id": id}
#     result = mysql.getOne(sql, param)
#     result['content'] = result['content'].decode('utf-8')
#     context = {}
#     context["content"] =  result['content']
#     return render(request, 'novel.html', context)


def chapter(request, novel_id):
    sql = "SELECT title,content FROM novel where id = %(id)s;"
    param = {"id": novel_id}
    result = mysql.getOne(sql, param)
    result['title'] = result['title'].decode('utf-8')
    result['content'] = result['content'].decode('utf-8')
    context = {'novel': result}
    return render(request, 'novel.html', context)