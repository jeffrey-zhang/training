import zmq


def run():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:6666")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    print('client1')

    while True:
        msg = socket.recv()
        print('msg:%s' % msg)


if __name__ == '__main__':
    run()
