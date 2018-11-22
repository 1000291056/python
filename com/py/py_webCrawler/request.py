# -*- coding: utf-8 -*-
import requests
import os
from pypinyin import lazy_pinyin

from bs4 import BeautifulSoup 
from bs4 import  SoupStrainer
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
def getAllNamesForGirls(url):
    namesForGirls=set()
    r= requests.get(url)
    r.encoding="gb2312"
    content=r.text
    #print(content)
    #only_tag=SoupStrainer("div",class_="i_cont_s")
    bs=BeautifulSoup(content,"html.parser")
    divs= bs.findAll("div",class_="i_cont_s")
   
    for div_ in divs:
        tag_as=div_.findAll("a")
        #print(tag_as)
        for a in tag_as:
            if a.has_attr("title"):
                name=a["title"]
                #print(name)
                #try:
                name_list=lazy_pinyin(name)
                name_pinyin=""
                for name_ in name_list:
                    name_pinyin=name_pinyin+name_
                    
                if name_pinyin.strip():
                   namesForGirls.add(name_pinyin)
                   
            
    return namesForGirls
#图片列表地址
def gernerateUrls(namesForGrils):
    #for name in namesForGrils:
        #print("gernerateUrls:",name)
    urls=set()
    for name_gril in namesForGrils:
        urls.add ("http://www.win4000.com/mt/"+name_gril+".html")
    return urls
#图片下载地址
def gernerateImageUrls(urls):
    imageurls=set()
    #for url in urls:
        #print("gernerateImageUrls:",url)    
    for url in urls:
        r=requests.get(url)
        r.encoding="utf-8"
        content=r.text
        bs=BeautifulSoup(content,"html.parser")
        imgTags=bs.findAll("img")
        for imgTag in imgTags:
            #print("tag:",imgTag)
            if imgTag.has_attr("src"):
                src=imgTag["src"]
                if src.strip() and src.startswith("http://"):
                    imageurls.add(src)
            pass
    return imageurls
    
#开启下载
def downLoad(imgs):
    #for img in imgs:
        #print("downLoad:",img)
   
    if(imgs=="None"):
        return
    if len(imgs)<=0:
        print("no volid url")
    else:
        print("start download..........................................")
        #del_file(basePATH)
    while len(imgs)>0:
       img_temp=imgs.pop()
       print(img_temp)
       r_img= requests.get(img_temp)
       img_temp_frag=img_temp.split("/")
       file_name=img_temp_frag[len(img_temp_frag)-1]
       path=basePATH+os.sep+file_name
       print(path)
       fo=open(path,"wb+")
       fo.write(r_img.content)
       fo.close()
       pass    
url="http://www.win4000.com/mt/zhaoliying.html"
url_names="http://www.manmankan.com/dy2013/mingxing/neidi/nvmingxing.shtml"
basePATH="C:\\Users\\temp\\Desktop\\image"

downLoad(gernerateImageUrls(gernerateUrls(getAllNamesForGirls(url_names))))
#get all tag:img
#for img in bs.findAll("img"):
   

#r_weathor=requests.get(url_json)
#print(r_weathor.json())