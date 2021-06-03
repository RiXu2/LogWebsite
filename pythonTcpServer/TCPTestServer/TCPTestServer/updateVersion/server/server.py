import socket
import struct
import json
import os

# 根据上传文件的路径进行改动 不是写死的
share_dir = r'/Users/liuxuri/Desktop/pythonTcpServer/TCPTestServer/TCPTestServer/updateVersion/server/share'


def upload(client):
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


def get(conn, cmds):
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


def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8913))
    server.listen(5)

    print('starting...')
    while True:
        conn, client_addr = server.accept()
        print(client_addr)

        while True:  # 通信循环
            try:
                res = conn.recv(8096)
                if not res:
                    break

                cmds = res.decode('utf-8').split()
                if cmds[0] == 'get':
                    get(conn, cmds)
                elif cmds[0] == 'upload':
                    #upload(server)
                    pass
                else:
                    continue

            except ConnectionResetError:
                break
        conn.close()

    server.close()


if __name__ == '__main__':
    run()
