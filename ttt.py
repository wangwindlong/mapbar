import os


def search(path, name):
    for root, dirs, files in os.walk(path):  # path 为根目录
        if name in dirs or name in files:
            flag = 1  # 判断是否找到文件
            root = str(root)
            dirs = str(dirs)
            return root + '\\' + name
    return -1


path = search('C:\\', '360se.exe')
if path == -1:
    print("未找到360浏览器")
else:
    print("找到360浏览器")
