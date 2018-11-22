# -*- coding: utf-8 -*-
import os
import sys
import subprocess
#print(sys.version,sys.platform,sys.path)
mds=sys.modules
keys=mds.keys()
for key in keys:
    print(key)
    print(mds[key])
project_path=r"D:\project\ffw\Python_WebCrawler"
file_path=r"D:\project\ffw\Python_WebCrawler\README.md"
print("os.curdir",os.getcwd())
print("目录分隔符",os.sep)
print("isdir:",os.path.isdir(project_path))
print("isfile",os.path.isfile(file_path))
print("split",os.path.split(file_path))
print("abspath",os.path.abspath(os.curdir))
print("大家好")
print("*************shell os.system  仅仅只是执行了shell命令*************************")
#os.system("dir .")
#os.system("type init.py")
print("*************shell os.popen 能连接到标准的输入输出流  返回对象自带迭代器*************************")
log_file_path="D:\project\ffw\Python_WebCrawler\log.txt"
o=os.popen("dir .")
for l in o:
    print(l)
print(o.read())
print("*************shell subprocess*************************")
#subprocess.call("python init.py",shell=True)
pip=subprocess.Popen("dir .",stdout=subprocess.PIPE,shell=True)
print(pip.communicate())
pip.wait()
print("*************shell startfile*************************")
#os.startfile("http://www.baidu.com")
