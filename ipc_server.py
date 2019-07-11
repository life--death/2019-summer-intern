import threading
import uuid
from multiprocessing import Queue
from multiprocessing.managers import BaseManager


SERVER_CONFIG = {
    'address': '0.0.0.0',
    'port': 9999,
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


if __name__ == '__main__':
    print('unit test')
    import pprint
    import time
    start_server()
    while True:
        req_uid, req = get_request()
        pprint.pprint(req)
        put_response(req_uid, {'response': 'test_response', 'time': time.time()})
