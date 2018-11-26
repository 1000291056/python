# -*- coding: utf-8 -*-
import os
import sys
import shutil
import subprocess
import locale
from tkinter import *
import tkinter.filedialog
from PIL import Image
import pickle
import tkinter.font as tkFont
########################################################################
config_path=r"config.txt"
conf_dict={"apk_path":"","so_path":"","keystore_path":"","pwd":""}
#----------------------------------------------------------------------
def saveConfig():
    """保存选择过的文件位置"""
    if len(conf_dict)>0:
        conf_file=open(config_path,"wb+")
        pickle.dump(conf_dict,file=conf_file)
        conf_file.close()
#----------------------------------------------------------------------
def loadConfig():
    """加载配置"""
    conf_dict.clear()
    conf_file = open(config_path,'rb')  
    data1 = pickle.load(conf_file) 
    #print(data1)  
    conf_dict.update(data1)
    print("配置文件：",str(conf_dict))  
    
class ReplaceSo:
    """替换apk中的so文件"""
    base_path=r"C:\Users\temp\Desktop"
    apk_name=""
    apk_path_spl=()
    apk_path=r"C:\Users\temp\Desktop\lhj_new.apk"#UI中设置
    so_path=r"D:\Document\Tencent\QQ\820804517\FileRecv\黑鲨\libwzweavingarm32.so"#UI中设置
    keystore_path=r"D:\Document\ffw\key\key.jks"#UI中设置
    pwd="111111"#UI中设置
    #----------------------------------------------------------------------
    def setPath(self,apk_path,so_path,keystore_path,pwd):
        """"""
        if apk_path!=None and (not apk_path.isspace()):
            self.apk_path=apk_path
        else:
            return
         
        if so_path!=None and (not so_path.isspace()):
            self.so_path=so_path
        else:
            return        
        if keystore_path!=None and (not keystore_path.isspace()):
            self.keystore_path=keystore_path
        else:
            return        
        if pwd!=None and (not pwd.isspace()):
            self.pwd=pwd
        else:
            return
        conf_dict.update({"apk_path":apk_path,"so_path":so_path,"keystore_path":keystore_path,"pwd":pwd})
        saveConfig()
        self.start()
        
        
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
    #----------------------------------------------------------------------
    def getApkName(self):
        """获取apk文件名"""
        self.apk_path_spl=os.path.split(self.apk_path)
        self.apk_name=os.path.splitext(self.apk_path_spl[1])[0]
        print(self.apk_name)
        return self.apk_name
        
    #----------------------------------------------------------------------
    def getApkDecompilePath(self):
        """获取反编译路径"""
        self.apk_Decompile_path=self.base_path+os.sep+self.apk_name
    
    #----------------------------------------------------------------------
    def invokeDecompile(self):
        """反编译"""
        Decompile_cmd="apktool -r d "+self.apk_path+" -o "+self.apk_Decompile_path
        #pip=subprocess.Popen(Decompile_cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        #print(pip.stdout.read().decode(locale.getdefaultlocale()[1]))
        os.system(Decompile_cmd) 
    # ----------------------------------------------------------------------
    def replaceSo(self):
        """替换so"""
        so_name=(os.path.split(self.so_path)[1])
        so_target_path=self.apk_Decompile_path+os.sep+"lib"+os.sep+"armeabi-v7a"+os.sep+so_name
        print("so拷贝至：",shutil.copyfile(self.so_path,so_target_path))
    #----------------------------------------------------------------------
    def package(self):
        """打包apk"""
        print("开始重新打包.....................")
        package_cmd="apktool b "+self.apk_Decompile_path
        os.system(package_cmd)
        
    
    #----------------------------------------------------------------------
    def signApk(self):
        """签名 
           命令：jarsigner -verbose -keystore keystore文件路径 -signedjar 签名后生成的apk路径 待签名的apk路径 别名
           """
        new_unsigned_apk_path=self.apk_Decompile_path+os.sep+"dist"
        signed_apk_path=new_unsigned_apk_path+os.sep+self.apk_name+"_signed"+".apk"
        #apktool 打包apk时 取名与原先apk名称一致
        no_signed_apk_path=new_unsigned_apk_path+os.sep+self.apk_path_spl[1]
        
        sign_cmd="jarsigner -verbose -keystore %(keystore_path)s -storepass %(pwd)s -signedjar %(signed_apk_path)s %(no_signed_apk_path)s key0"\
                %{'keystore_path':self.keystore_path,'signed_apk_path':signed_apk_path,'no_signed_apk_path':no_signed_apk_path,'pwd':self.pwd}
                
        print("执行签名............")
        pipe=subprocess.Popen(sign_cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        print(pipe.stdout.read().decode(locale.getdefaultlocale()[1]))
        print("完成........")
        os.startfile(new_unsigned_apk_path)
    #----------------------------------------------------------------------
    def start(self):
        """"""
        self.getApkName()
        self.getApkDecompilePath()
        self.invokeDecompile()
        self.replaceSo()
        self.package()
        self.signApk()
        
########################################################################
class FileUtil:
    """选择文件操作类"""
    replaceSo=None
    root=None
    progress_lable=None
    #----------------------------------------------------------------------
    def __init__(self,replaceSo):
        """Constructor"""
        self.replaceSo=replaceSo
    #----------------------------------------------------------------------
    def operateSurface(self):
        """显示操作界面"""
        loadConfig()
        self.root=Tk(screenName="替换APKso文件")
        title=Label(self.root,text="替换so")
        title.config(fg="red",font=tkFont.Font(size=20))
        title.grid(row=0,column=1)
        #第一行
        Label(self.root,text="原apk路径：").grid(row=1,column=0)
        old_apk_path_entry=Entry(self.root,width=50,textvariable=conf_dict["apk_path"])
        old_apk_path_entry.insert(0,conf_dict["apk_path"])
        old_apk_path_entry.grid(row=1,column=1)
        choose_old_apk_btn=Button(self.root,text="选择文件",command=(lambda:(old_apk_path_entry.insert(0,self.chooseFiles()))))
        #choose_old_apk_btn.bind("<Button-1>",lambda:self.chooseFiles(self.CHOOSE_APK))
        choose_old_apk_btn.grid(row=1,column=2)
        #第二行
        Label(self.root,text="keyStore路径：").grid(row=2,column=0)
        keystore_entry=Entry(self.root,width=50,textvariable=conf_dict["keystore_path"])
        keystore_entry.insert(0,conf_dict["keystore_path"])
        keystore_entry.grid(row=2,column=1)
        Button(self.root,text="选择文件",command=(lambda:(keystore_entry.insert(0,self.chooseFiles())))).grid(row=2,column=2)
        #第三行
        Label(self.root,text="so路径：").grid(row=3,column=0)
        so_path_entry=Entry(self.root,width=50,textvariable=conf_dict["so_path"])
        so_path_entry.insert(0,conf_dict["so_path"])
        so_path_entry.grid(row=3,column=1)
        Button(self.root,text="选择文件",command=(lambda:(so_path_entry.insert(0,self.chooseFiles())))).grid(row=3,column=2)
        #第四行
        Label(self.root,text="keyStore密码：").grid(row=4,column=0)
        keystore_passwd_entry=Entry(self.root,textvariable=conf_dict["pwd"], show='*',width=50)
        keystore_passwd_entry.insert(0,conf_dict["pwd"])
        keystore_passwd_entry.grid(row=4,column=1)
        Label(self.root,text="*",fg = 'red').grid(row=4,column=2)
        #第五行
        #self.progress_lable=Entry(self.root,text="")
        #self.progress_lable.grid(row=5,column=0)
        #第六行
        #image_bg=Image.open(r"D:\project\ffw\python\img\t.jpg")
        Button(self.root,text="确定",bd=2,width=25,bg="green",command=(lambda:self.exitUiAndStart(old_apk_path_entry.get(),so_path_entry.get(),keystore_entry.get(),keystore_passwd_entry.get()))).grid(row=6,column=1)
        pass
        self.root.mainloop()
    #----------------------------------------------------------------------
    def progress(self,progress):
        """显示进度打印替换过程中的信息"""
        self.progress_lable.insert(progress)
    #----------------------------------------------------------------------
    def exitUiAndStart(self,apk_path,so_path,keystore_path,pwd):
        """ui操作界面退出，开始替换工作"""
        self.root.destroy()
        self.replaceSo.setPath(apk_path,so_path,keystore_path,pwd)
        
    #----------------------------------------------------------------------
    CHOOSE_APK=1
    CHOOSE_SO=2
    CHOOSE_KEYSTORE=2
    def chooseFiles(self):
        """选择文件"""
        files=tkinter.filedialog.askopenfilename()
        print(type(files))  
        return files
          
        
        
    
    
#----------------------------------------------------------------------
def startwork():
    """"""
    work=ReplaceSo()
    fileUtil=FileUtil(work)
    fileUtil.operateSurface()    
    
startwork()









