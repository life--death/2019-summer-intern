from multiprocessing.managers import BaseManager
import multiprocessing
import threading
import uuid
from multiprocessing import Queue
import os
import time

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

SERVER_CONFIG = {
    'address': '0.0.0.0',
    'port': 9998,
    'auth_key': b'A8rhWNHR2p',
}

queue_map = {}
request_queue = Queue()


def get_response_queue():
    response_queue = Queue()
    uid = uuid.uuid4()
    queue_map[uid] = response_queue
    response_queue.put(uid)
    return response_queue


class ServerManager(BaseManager):
    pass


ServerManager.register('get_request_queue', callable=lambda: request_queue)
ServerManager.register('get_response_queue', callable=get_response_queue)


def server_thread():
    m = ServerManager(address=(SERVER_CONFIG['address'], SERVER_CONFIG['port']), authkey=SERVER_CONFIG['auth_key'])
    s = m.get_server()
    s.serve_forever()


class ServerThread:
    inst = None

    def __init__(self):
        self._thread = threading.Thread(target=server_thread)
        self._thread.daemon = True
        self._thread.start()


def start_server():
    if ServerThread.inst is None:
        ServerThread.inst = ServerThread()


def get_request():
    return request_queue.get()


def put_response(uid, response):
    response_queue = queue_map.pop(uid)
    response_queue.put(response)




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

def runSubcmd(arg):
    # print("-------")
    # print(arg)
    os.system(arg)
def getCPUutil():
    with open('C:\\Users\\WDAGUtilityAccount\\Desktop\\2019-summer-intern\\cpu_util.txt', 'w') as f:
        pass
    while True:
        os.system('C:\\Users\\WDAGUtilityAccount\\Desktop\\2019-summer-intern\\dist\\getCpuUtil.exe')
        time.sleep(2)
def runrest():
    print("runtest")

if __name__ == '__main__':
    print('client running')
    import pprint

    # thispath=os.path.abspath('.')
    # print(thispath)
    # fip=open(f"{thispath}\serverip.txt")
    fip=open('C:\\Users\\WDAGUtilityAccount\\Desktop\\2019-summer-intern\\serverip.txt')
    server_ip=fip.readline().strip()
    fip.close()
    server_config = {'address': server_ip, 'port': 9999, 'auth_key': b'A8rhWNHR2p'}
    ip=get_host_ip()
    while True:
        resstr=send_request(server_config, {'request': ip, 'time': time.time()})
        if resstr:
            pprint.pprint(resstr)
            break
        time.sleep(0.5)


    print('sb server')
    import pprint
    import time
    import subprocess
    start_server()
    getcuputil = multiprocessing.Process(target=getCPUutil, args=())
    getcuputil.start()
    while True:
        req_uid, req = get_request()
        pprint.pprint(req)
        put_response(req_uid, {'response': 'ok', 'time': time.time()})
        import os
        cmd=req['request']
        if req['cmdType']=='2':
            cmd=f"C:\\Users\\WDAGUtilityAccount\\Desktop\\2019-summer-intern\\source\{cmd}"
            # print(cmd)
        elif req['cmdType']=='1':
            pass
        psub=multiprocessing.Process(target=runSubcmd, args=(cmd,))
        psub.start()

        # cmd=cmd.split(',')[0].split(':')[1]
        # with open("C:\\Users\\WDAGUtilityAccount\\Desktop\\summer_camp\\2019-summer-intern\\subrun.bat","w") as f:
        #     print(cmd)
        #     f.write(cmd)
        # os.system('C:\\Users\\WDAGUtilityAccount\\Desktop\\summer_camp\\2019-summer-intern\\subrun.bat')
