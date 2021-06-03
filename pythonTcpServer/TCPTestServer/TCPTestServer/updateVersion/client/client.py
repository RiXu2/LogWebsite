import socket
import struct
import json
import os

share_dir = r'/Users/liuxuri/Desktop/pythonTcpServer/TCPTestServer/TCPTestServer/updateVersion/client/share'


def upload(conn, cmds):
    filename = cmds[1]
    header_dic = {
        'filename': filename,
        'md5': 'xxdxxx',
        'file_size': os.path.getsize('%s/%s' % (share_dir, filename))
    }

    header_json = json.dumps(header_dic)
    header_bytes = header_json.encode('utf-8')

    # 先发长度 再发内容
    conn.send(struct.pack('i', len(header_bytes)))
    conn.send(header_bytes)

    with open('%s/%s' % (share_dir, filename), 'rb') as f:
        for line in f:
            conn.send(line)


def get(client):
    obj = client.recv(4)
    header_size = struct.unpack('i', obj)[0]

    header_bytes = client.recv(header_size)
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    print(header_dic)
    total_size = header_dic['file_size']
    filename = header_dic['filename']

    with open('%s/%s' % (share_dir, filename), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            line = client.recv(1024)
            f.write(line)
            recv_size += len(line)
            print('总大小：%s 已下载大小：%s' % (total_size, recv_size))


def run():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8913))

    while True:

        inp = input('>>: ').strip()  # get file_name.后缀
        # get 跟文件名，不跟path
        if not inp:
            continue
        client.send(inp.encode('utf-8'))
        cmds = inp.split()
        if cmds[0] == 'get':
            get(client)
        elif cmds[1] == 'upload':
            #upload(client, cmds)
            pass
        else:
            continue

    client.close()


if __name__ == '__main__':
    run()