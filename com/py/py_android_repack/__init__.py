import os
import sys
import shutil
apk_Decompile_path=r"C:\Users\temp\Desktop"
#apk_path=r"C:\Users\temp\Desktop\lhj_new.apk"
apk_path=input("亲输入源apk路径：")
#获取apk文件名
apk_path_spl=os.path.split(apk_path)
apk_name=os.path.splitext(apk_path_spl[1])[0]
print(apk_name)
#反编译路径
apk_Decompile_path=apk_Decompile_path+os.sep+apk_name
#反编译
Decompile_cmd="apktool -r d "+apk_path+" -o "+apk_Decompile_path
os.system(Decompile_cmd)
#替换so 
#so_path=r"D:\Document\Tencent\QQ\820804517\FileRecv\黑鲨\libwzweavingarm32.so"
so_path=input("请输入so路径：")
so_name=(os.path.split(so_path)[1])
so_target_path=apk_Decompile_path+os.sep+"lib"+os.sep+"armeabi-v7a"+os.sep+so_name
print("so拷贝至：",shutil.copyfile(so_path,so_target_path))

#打包apk
print("开始重新打包.....................")
package_cmd="apktool b "+apk_Decompile_path
os.system(package_cmd)