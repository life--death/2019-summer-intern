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
    fip=open("c:/summer_camp/code/clientip.txt")
    server_ip=fip.readline().strip()
    fip.close()
    server_config = {'address': server_ip, 'port': 9998, 'auth_key': b'A8rhWNHR2p'}
    ip=get_host_ip()
    while True:
        exefile = 'chrome'
        url = "https://www.google.com"
        cmd = f"start {exefile} --new-windows {url}"
        resstr=send_request(server_config, {'request': cmd, 'time': time.time()})
        if resstr:
            pprint.pprint(resstr)
            break
        time.sleep(0.5)


