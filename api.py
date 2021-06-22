from flask import request, Flask, make_response  # flask模块
import json
from DingCallbackCrypto import DingCallbackCrypto3  #通知加解密
from maneger import *
# from sql import *   # 使用pymysql方式
from models import *    # 使用orm方式
from flask_sqlalchemy import SQLAlchemy

# Flask通用配置
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123123aa~@10.0.9.18:3306/audit?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/getcallback', methods=['POST'])
def callback():
    dingCrypto = DingCallbackCrypto3('XXXXXXXXXX',  # token
                                     'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','dingrf8kqdohfr7nm3su')  # aeskey,key
    response = make_response(dingCrypto.getEncryptedMap('success'))
    response.headers["Content-Type"] = "application/json"
    postdata = request.get_data()  # 获取POST请求的原始数据
    jsondata = json.loads(postdata.decode())
    arg = request.args
    decryptMsg = dingCrypto.getDecryptMsg(arg['msg_signature'], arg['timestamp'], arg['nonce'], jsondata['encrypt'])
    print(postdata)
    decryptMsg = json.loads(decryptMsg)
    print(decryptMsg)
    if decryptMsg['EventType'] == 'user_leave_org':  # 离职通知
        for i in decryptMsg['UserId']:
            # if userExist(i) >= 1 and userDel(i) == 0:
            if userExist(i) and not userDel(i):
                userLeaveOrg(i)
            else:
                print('no this people')
    elif decryptMsg['EventType'] == 'chat_add_member':  # 加入群组通知
        if decryptMsg['ChatId'] == getChatId():
            for i in decryptMsg['UserId']:
                # if userExist(i) == 0 and userDel(i) == 0:
                if not userExist(i) and not userDel(i):
                    userinfo = getUserInfo(i)
                    userAddChat(userinfo['mobile'], userinfo['email'], userinfo['name'], userinfo['userid'])
                # elif userDel(i) >= 1:
                elif userDel(i):
                    userNormal(i)
    elif decryptMsg['EventType'] == 'user_modify_org':  # 修改通知
        for i in decryptMsg['UserId']:
            # if userExist(i) >= 1 and userDel(i) == 0:
            if userExist(i) and not userDel(i):
                if i not in getAllUserId():
                    userQuitChat(i)
    elif decryptMsg['EventType'] == 'bpms_instance_change' and decryptMsg['type'] == 'start':
        for i in getExamineAndApprove():
            if i['instance_id'] == decryptMsg['processInstanceId']:
                if re.search('外卖', i['title']):
                    if re.search('bug', i['forms'][0]['content'], flags=re.I) or \
                            re.search('hotfix', i['forms'][0]['content'], flags=re.I) or \
                            re.search('bugfix', i['forms'][0]['content'], flags=re.I) or \
                            re.search('fix', i['forms'][0]['content'], flags=re.I):
                        if re.search('需求', i['forms'][0]['content']):
                            addWorkOrder(re.split('提交', i['title'])[0], '需求和补丁', i['forms'][1]['content'],
                                         i['forms'][2]['content'])
                        else:
                            addWorkOrder(re.split('提交', i['title'])[0], '补丁', i['forms'][1]['content'],
                                         i['forms'][2]['content'])
                    else:
                        addWorkOrder(re.split('提交', i['title'])[0], '需求', i['forms'][1]['content'],
                                     i['forms'][2]['content'])
    return response

@app.route('/api/corp/message', methods=['POST'])
def send_corp_message():
    try:
        data = request.get_data().decode()
        jsondata = json.loads(data)
        userid_list = str(','.join(jsondata["userid_list"]))
        content = jsondata["content"]
        print(userid_list, content)
        sendCorpMessage(userid_list, content)
        return "OK"
    except:
        return "ERROR"

if __name__ == '__main__':
    app.run(debug=False, host='10.0.3.189', port=8280)