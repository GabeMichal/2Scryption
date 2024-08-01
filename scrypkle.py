import pickle
import socket


def picklificate(data):
    return pickle.dumps(data)+b'END'


def unpickle(conn):
    try:
        buffer = b''
        while True:
            data = conn.recv(1024)
            if not data:
                break
            buffer += data
            if b'END' in buffer:
                break
        buffer = buffer.replace(b'END', b'')
        #print("Buffer:", buffer)
        return pickle.loads(buffer)
    except EOFError as e:
        print(e)
    except socket.error as e:
        print(e)
    return None
