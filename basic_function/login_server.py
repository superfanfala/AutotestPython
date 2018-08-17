#-*-coding:utf-8 -*-

import paramiko
import selenium



class LoginServer:
    def login(self,server_ip,server_port,username,password):
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 把要连接的机器添加到known_hosts文件中
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=server_ip,port=server_port,username=username,password=password)
        return ssh

class LoginWeb:
    def loginweb(self,url,webuser,webpasswd):
        pass
