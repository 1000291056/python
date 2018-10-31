import time
import calendar
print("hello the world!")
i=1;
if i>0:
    print("true")
else:
    print("false")
str="1111dfsfsfs_##$$%^^&&***"
print(str*2)

print(str[-1:-3])#????
list=["ab",1,2,"vv"]
print(list[-1:-4])
index=10;
nums=""
# while index>0:
#     nums+=index
#     index-=1
# print(nums)


print("时间处理：**********************************")
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
cal=calendar.month(2016,6)
print(cal)

def say(msg):
    print(msg)
    return None

say("test function")



