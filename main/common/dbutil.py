import pymysql

# def opendb():
#     # 打开数据库连接
#     db = pymysql.Connect(host='10.113.147.82',
#                          port=13306,
#                          user='broadcast_svc',
#                          passwd='vmfhwlqps14#2',
#                          db='broadcast_cms_dl',
#                          charset='utf8')
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # 使用 execute()  方法执行 SQL 查询
#     cursor.execute("SELECT VERSION()")
#     # 使用 fetchone() 方法获取单条数据.
#     data = cursor.fetchone()
#     print ("Database version : %s " % data)
#     # 关闭数据库连接
#     db.close()

global db


def getCursor():
    # 打开数据库连接
    global db
    db = pymysql.Connect(host='10.113.147.82',
                         port=13306,
                         user='broadcast_svc',
                         passwd='vmfhwlqps14#2',
                         db='broadcast_cms_dl',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    return cursor


def closeDB():
    db.close()


def getVersion(cursor):
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print ("Database version : %s " % data)


# cursor = getCursor();
# getVersion(cursor);
# closeDB()