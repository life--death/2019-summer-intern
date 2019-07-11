from multiprocessing.managers import BaseManager


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


if __name__ == '__main__':
    print('unit test')
    import pprint
    import time
    server_config = {'address': 'localhost', 'port': 9999, 'auth_key': b'A8rhWNHR2p'}
    while True:
        pprint.pprint(send_request(server_config, {'request': 'test_request:', 'time': time.time()}))
        time.sleep(0.5)
