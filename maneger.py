# -*- coding: utf-8 -*-
import dingtalk.api
import re


def getToken():
	req = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
	req.appkey = "XXXXXXXXXXXXXXX"
	req.appsecret = "XXXXXXXXXXXXXXXXXXXXXXXXX"
	try:
		resp = req.getResponse()
		return resp["access_token"]
	except Exception as e:
		return e

def getUserInfo(userid):
	req = dingtalk.api.OapiUserGetRequest("https://oapi.dingtalk.com/user/get")
	access_token = getToken()
	req.userid = userid
	try:
		resp = req.getResponse(access_token)
		return resp
	except Exception as e:
		return e

def getAllUserId():
	req = dingtalk.api.OapiUserListidRequest("https://oapi.dingtalk.com/topapi/user/listid")
	access_token = getToken()
	req.dept_id = getDepartmentId()
	try:
		resp = req.getResponse(access_token)
		return resp['result']['userid_list']
	except Exception as e:
		return e

def getDepartmentId():
	req = dingtalk.api.OapiDepartmentListRequest("https://oapi.dingtalk.com/department/list")
	access_token = getToken()
	try:
		resp = req.getResponse(access_token)
		for i in resp['department']:
			if i['name'] == '装逼小分队':
				return i['id']
	except Exception as e:
		return e

def getChatId():
	req = dingtalk.api.OapiDepartmentGetRequest("https://oapi.dingtalk.com/department/get")
	access_token = getToken()
	department_id = getDepartmentId()
	req.id = department_id
	try:
		resp = req.getResponse(access_token)
		return resp['deptGroupChatId']
	except Exception as e:
		return e


def sendCorpMessage(userid_list, content):
	req = dingtalk.api.OapiMessageCorpconversationAsyncsendV2Request(
		"https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2")
	access_token = getToken()
	req.userid_list = userid_list    # 'manager5091,0249254106878253'
	req.agent_id = '1199429018'     # 应用agentid
	req.to_all_user = 'false'
	msg = {"msgtype": "text", "text": {"content": content}}
	req.msg = msg

	try:
		resp = req.getResponse(access_token)
		print(resp)
	except Exception as e:
		print(e)

def getExamineAndApprove():
	req = dingtalk.api.OapiProcessWorkrecordTaskQueryRequest(
		"https://oapi.dingtalk.com/topapi/process/workrecord/task/query")
	req.userid = 'manager5091'
	req.offset = 0
	req.count = 15
	req.status = 0
	try:
		access_token = getToken()
		resp = req.getResponse(access_token)
		# print(resp['result']['list'])
		return resp['result']['list']

	except Exception as e:
		print(e)

# sendCorpMessage('manager5091,0249254106878253','请4尽快审批')

