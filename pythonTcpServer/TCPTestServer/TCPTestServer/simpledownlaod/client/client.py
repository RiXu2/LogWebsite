import socket
import struct
import subprocess
import sys
import json
import os

share_dir = r'/Users/liuxuri/Desktop/pythonTcpServer/TCPTestServer/TCPTestServer/simpledownlaod/client/share'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8912))

while True:
    cmd = input('>>: ').strip()  # get file_name.后缀
    # get 跟文件名，不跟path
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))

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
            print('总大小：%s 已下载大小：%s'%(total_size, recv_size))

client.close()
