class c203():
    course='python'
    cla_num='room_3'
    def __init__(self,name,roll_no,place):
        self.name=name
        self.roll_no=roll_no
        self.place=place
    def details(self):
        print(f'name ={self.name}')
        print(f'roll ={self.roll_no}')
        print(f'place ={self.place}')
    def modify(self):
        self.name='sri'
stu1=c203('megha',23,'bengaluru')
stu2=c203('varsha',44,'raichur')
stu3=c203('vamshika',22,'hyderabad')

#accesing object method by using class refe
c203.details(stu1)
print()
#accesing object method by using obj refe
stu1.details()

#by using object method we can modify object attributes only
stu1.modify()
print()
#accesing after modification
stu1.details()
