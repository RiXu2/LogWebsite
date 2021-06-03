import socket
import struct
import json
import os

share_dir = r'/Users/liuxuri/Desktop/pythonTcpServer/TCPTestServer/TCPTestServer/onlyforUpload/client/share'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8917))

while True:
    cmd = input('>>: ').strip()  # upload file_name.后缀
    # upload 跟文件名，不跟path
    if not cmd:
        continue

    cmds = cmd.split()
    filename = cmds[1]
    header_dic = {
        'filename': filename,
        'md5': 'xxdxxx',
        'file_size': os.path.getsize('%s/%s' % (share_dir, filename))
    }
    print('star send')
    header_json = json.dumps(header_dic)
    header_bytes = header_json.encode('utf-8')
    client.send(struct.pack('i', len(header_bytes)))
    client.send(header_bytes)

    try:
        with open('%s/%s' % (share_dir, filename), 'rb') as f:
            for line in f:
                client.send(line)
    except NameError:
        print("Can't open file. Check what you have entered.")

client.close()
