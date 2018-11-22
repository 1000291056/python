import sys
from tkinter import * 

#----------------------------------------------------------------------
def onclick(msg):
    """点击事件"""
    print(msg,"我被点击了！")
    sys.exit(0)
    

root=Tk()
text=Label(root,text="Hello the world!")
text.pack(side=TOP,fill=BOTH,expand=YES)
Button(root,text="按钮",command=(lambda:onclick("Hello"))).pack(side=LEFT)
root.mainloop()