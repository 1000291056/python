"""
并发编程
"""
import os
import sys
def children():
    print("I am children ",str(os.getpid()))
    exit(0)
#----------------------------------------------------------------------
def parent():
    """父进程"""
    if not sys.platform.find("win")==-1:
        print("window 平台不支持！")
        return
    
    while True:
        id=os.fork()
        if(id==0):#子进程
            children()
        else:
            print("主进程:",str(os.getpid()),"开辟子进程：",str(id))
        c=input("退出？")
        if c=="q":
            break
parent()
    