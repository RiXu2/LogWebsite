import os
import shutil
import time
root_dir = "/Users/liuxuri/Desktop/pythonTcpServer/TCPTestServer/TCPTestServer/onlyforUpload/client/share/"
desc_dir = "/Users/liuxuri/Desktop/pythonTcpServer/TCPTestServer/TCPTestServer/onlyforUpload/client/testfile/"

file_list=os.listdir(root_dir)
if len(file_list) > 0:
    for file in file_list:
        shutil.move(root_dir+file, desc_dir+file)
print('done')