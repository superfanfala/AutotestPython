#-*-coding:utf-8 -*-
from basic_function.login_server import LoginServer
from config import basic_config
from basic_function.oprate_server import OprateServer
import re

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
        last_result=[]
        for i in result_list:
            last_result=last_result+i.split('\n')
        l_list=map(str,last_result)
        print(l_list)
        for j in l_list:
            reg = re.compile(r"(?<=xlb[.*m).*")
            match = reg.search('abc123')
            print match.group(0)
        # result_dict=dict(zip(l_list[0::2],l_list[1::2]))
        # print(result_dict)


        # print(result_dict)
        # for i in result_dict.keys():
        #     k=result_dict[i]
        #     str_k=str(k)
        #     print(result_dict[i])
        #     v=result_dict[str_k]
        #     if result_dict[str_k] == 'Running':
        #         print(result_dict[i])
        #         print(type(result_dict[i]))
        #         print('aaaa')




if __name__ == '__main__':
    CheckServer().checkserver()
