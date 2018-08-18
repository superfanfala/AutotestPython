#-*-coding:utf-8 -*-
from basic_function.login_server import LoginServer
from config import basic_config
from basic_function.oprate_server import OprateServer


class CheckServer:
    def __init__(self):
        ip=basic_config.server_ip
        port=basic_config.server_port
        username=basic_config.username
        passwd=basic_config.password
        self.ssh=LoginServer().login(server_ip=ip,server_port=port,username=username,password=passwd)
        self.oserver=OprateServer(self.ssh)

    def checkserver(self):
        result=self.oserver.execute_cmd('servermgr status all')
        result_str=result.split(' ')
        result_list=list(result_str)
        print(result_list)
        last_result=[]
        for i in result_list:
            last_result=last_result+i.split('\n')
        result_dict=dict(zip(last_result[0::2],last_result[1::2]))

        for i in result_dict.keys():
            print(i)
            print(type(i))

        # if result_dict['configservice']=='Running':
        #     print('*******')
        # else:
        #     print('xxxxxxx')


if __name__ == '__main__':
    CheckServer().checkserver()