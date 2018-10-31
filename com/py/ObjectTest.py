class Person:
    "构建人类对象"
    name=""
    age=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say(self):
        print("my name is "+ self.name+"  and i am "+str(self.age)+" years old!")


p=Person("小明",5)
p.say()
