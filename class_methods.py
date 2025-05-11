class c203():
    course='python'
    cla_num='room_3'
    def __init__(self,name,roll_no,place):
        self.name=name
        self.roll_no=roll_no
        self.place=place
    @classmethod
    def m1(cls):
        print(cls)
    @classmethod
    def m2(cls):
        cls.course='java'
stu1=c203('megha',23,'bengaluru')
stu2=c203('varsha',44,'raichur')
stu3=c203('vamshika',22,'hyderabad')

#accesing class method by using class attribute
c203.m1()

#accesing class method by using object refe
stu1.m1()

#after modification we have to acces
c203.m2()
print(c203.course)
print(stu1.course)
