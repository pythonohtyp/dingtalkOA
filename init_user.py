import pymysql
from maneger import *

conn = pymysql.connect(host="10.0.9.18", user="root", passwd="123123aa~", db="audit")
cursor = conn.cursor()

def initUserList():
    userid_list = getAllUserId()
    for userid in userid_list:
        userinfo = getUserInfo(userid)
        sql = "insert into octopus_user (user_name,email,name_cn,outer_id) values(%s,%s,%s,%s)"
        conn.ping(reconnect=True)
        cursor.execute(sql, (userinfo['mobile'], userinfo['email'], userinfo['name'], userinfo['userid']))
    conn.commit()
    conn.close()

initUserList()