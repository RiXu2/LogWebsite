import socket
import struct
import subprocess
import sys
import json
import os

# 根据上传文件的路径进行改动 不是写死的
share_dir = r'/Users/liuxuri/Desktop/pythonTcpServer/TCPTestServer/TCPTestServer/simpledownlaod/server/share'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8912))
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

        except ConnectionResetError:
            break
    conn.close()

server.close()
