import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123123aa~@10.0.9.18:3306/audit?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

# conn = pymysql.connect(host="10.0.9.18", user="root", passwd="123123aa~", db="audit")
# cursor = conn.cursor()
# conn._write_timeout = 10000
#
#
# def userAddChat(user_name, email, name_cn, outer_id):  #加入
#     sql = "insert into octopus_user (user_name,email,name_cn,outer_id) values(%s,%s,%s,%s)"
#     conn.ping(reconnect=True)
#     cursor.execute(sql, (user_name, email, name_cn, outer_id))
#     conn.commit()
#     conn.close()
# def userLeaveOrg(userid):  #离职
#     sql = "update octopus_user set is_del =1 where outer_id = %s"
#     conn.ping(reconnect=True)
#     cursor.execute(sql, userid)
#     conn.commit()
#     conn.close()
#
# def userQuitChat(userid): #退出群组会话
#     sql = "update octopus_user set is_del =1 where outer_id = %s"
#     conn.ping(reconnect=True)
#     cursor.execute(sql, userid)
#     conn.commit()
#     conn.close()
#
# def userNormal(userid):
#     sql = "update octopus_user set is_del =0 where outer_id = %s"
#     conn.ping(reconnect=True)
#     cursor.execute(sql, userid)
#     conn.commit()
#     conn.close()
#
# def userExist(userid):  #判断是否在数据库里（加入到对应部门才写库）
#     sql = "select * from octopus_user where outer_id = %s"
#     conn.ping(reconnect=True)
#     result = cursor.execute(sql, userid)
#     conn.commit()
#     conn.close()
#     return result
#
# def userDel(userid):  #判断是否在数据库里（加入到对应部门才写库）
#     sql = "select * from octopus_user where is_del =1 and outer_id = %s"
#     conn.ping(reconnect=True)
#     result = cursor.execute(sql, userid)
#     conn.commit()
#     conn.close()
#     return result
#
# def addWorkOrder(initiator, applytype, country, profession):  # 加入
#     sql = "insert into examine_approve (initiator,applytype,country,profession) values(%s,%s,%s,%s)"
#     conn.ping(reconnect=True)
#     cursor.execute(sql, (initiator, applytype, country, profession))
#     conn.commit()
#     conn.close()