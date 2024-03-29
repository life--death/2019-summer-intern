#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from multiprocessing.managers import BaseManager
import threading
import uuid
from multiprocessing import Queue

class ServerManager(BaseManager):
    pass


ServerManager.register('get_request_queue')
ServerManager.register('get_response_queue')


def send_request(config, req):
    server = ServerManager(address=(config['address'], config['port']), authkey=config['auth_key'])
    server.connect()
    response_queue = server.get_response_queue()
    uid = response_queue.get()
    request_queue = server.get_request_queue()
    request_queue.put((uid, req))
    return response_queue.get()

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

if __name__ == '__main__':

    print('unit test')
    import pprint
    import time
    import os,shutil
    import sys

    s = "C:\\Users\\ztp\\Desktop\\Shadowsocks-4.1.6\\Shadowsocks.exe"
    # s = str(sys.argv[1])
    # print(s)
    ss = s.strip().split("\\")[-1]
    if os.path.exists(s):
        res = shutil.copy(s, f'C:\summer_camp\source\\{ss}')
    thispath=os.path.abspath('.')
    fip=open("C:\summer_camp\code\clientip.txt")
    server_ip=fip.readline().strip()
    fip.close()
    server_config = {'address': server_ip, 'port': 9998, 'auth_key': b'A8rhWNHR2p'}
    ip=get_host_ip()
    while True:
        cmdType='2'# 1:open url; 2:run a exe; 3
        exefile = 'microsoft-edge:'
        url = "https://www.google.com"
        cmd = f"start microsoft-edge:{url}"  # chrome
        # cmd = f"start chrome --new-windows {url}" #chrome
        # exestr="C:\summer_camp\source\\ChromeSetup.exe /silent /install"
        # cmd=ss
        cmd="ChromeSetup.exe /silent /install"
        resstr=send_request(server_config, {'cmdType': cmdType, 'request': cmd, 'time': time.time()})
        if resstr:
            pprint.pprint(resstr)
            break
        time.sleep(0.5)

