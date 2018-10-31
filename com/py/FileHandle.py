import os

# str=input("请输入：")
# print("您已输入："+str)
path = "C:\\Users\\temp\\Desktop\\pythonfile.txt"

path1 = "C:\\Users\\temp\\Desktop\\pythonfile1.txt"
def testFile(path):
    if path == None:
        return
    fileObject = open(path, "r+")  # 打开文件
    pass
    fileObject.write("aaa")  # 写数据
    pass
    print(fileObject.readline())  # 读数据
    fileObject.close()
    return


testFile(path)
os.rename(path,path1)

try:
    print("try")
except BaseException:
    print("except")
else:
    print("")
finally:
    print("finally")