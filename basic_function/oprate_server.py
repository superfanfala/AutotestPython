#-*-coding:utf-8 -*-

class OprateServer:
    def __init__(self,ssh):
        self.ssh=ssh
    def execute_cmd(self,cmd):
        stdin , stdout ,stderr =self.ssh.exec_command(cmd)
        result=stdout.read()
        if not result:
            result=stderr.read()

        return result.decode()