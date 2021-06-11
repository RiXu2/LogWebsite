import socket
import struct
import subprocess
import sys
import json
import os

# 根据上传文件的路径进行改动 不是写死的
share_dir = r'/Users/liuxuri/Desktop/LogWebsite/logServer/tempsavesite/tempsave/tempsave/tempUpload'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8917))  # 端口被占 就换别的
server.listen(5)

print('starting...')
while True:
    conn, client_addr = server.accept()
    print(client_addr)

    while True:  # 通信循环
        try:
            obj = conn.recv(4)
            if not obj:
                print('break here')
                break
            header_size = struct.unpack('i', obj)[0]

            header_bytes = conn.recv(header_size)
            header_json = header_bytes.decode('utf-8')
            header_dic = json.loads(header_json)
            print(header_dic)
            total_size = header_dic['file_size']
            filename = header_dic['filename']

            print('start recv file')
            with open('%s/%s' % (share_dir, filename), 'wb') as f:
                recv_size = 0
                while recv_size < total_size:
                    line = conn.recv(1024)
                    f.write(line)
                    recv_size += len(line)
            print('done')

        except ConnectionResetError:
            break
    conn.close()

server.close()
