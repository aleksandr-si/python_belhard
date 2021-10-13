from abc import abstractclassmethod


class human:
    def __init__(self):
        self.__name=''
    @abstractclassmethod
    def set_name(self, name):
        self.__name=name+'++'
    def get_name(self):
        return self.__name
    name=property(get_name, set_name)
    def set_age(self, age):
        self.__age=age
    def get_age(self):
        return self.__age
    age=property(get_age, set_age)
    
    def set_hight(self, hight):
        self.__hight=hight
    def get_hight(self):
        return self.__hight
    profession=property(get_hight, set_hight)

    def weight(self,weight):
        self.weight=weight
        return self.weight


class manager(human):
    def __init__(self):
        self.profession='Manager'
    def set_name(self, name):
        self.__name=name+' '+self.profession
    def get_name(self):
        return self.__name
    name=property(get_name, set_name)
    def set_age(self, age):
        self.__age=self.profession+' '+str(age)
    def get_age(self):
        return self.__age
    age=property(get_age, set_age)
    
    def set_hight(self, hight):
        self.__hight=self.profession+' '+str(hight)
    def get_hight(self):
        return self.__hight
    hight=property(get_hight, set_hight)

    def weight(self,weight):
        self.weight='the weight is '+str(weight)
        return self.weight




class programmer(human):
    def __init__(self):
        self.profession='Programmer'
    def set_name(self, name):
        self.__name=name+' '+self.profession
    def get_name(self):
        return self.__name
    name=property(get_name, set_name)
    def set_age(self, age):
        self.__age=self.profession+' '+str(age)
    def get_age(self):
        return self.__age
    age=property(get_age, set_age)
    
    def set_hight(self, hight):
        self.__hight=self.profession+' '+str(hight)
    def get_hight(self):
        return self.__hight
    hight=property(get_hight, set_hight)

    def weight(self,weight):
        self.weight='the weight is '+str(weight)
        return self.weight


p1=manager()
p1.name="Ruslan"
p1.weight(200)
print(p1.name)
print(p1.weight)
p2=programmer()
p2.name="Egor"
p2.hight=100
p2.hight
p2.weight(200)
print(p2.name)
print(p2.hight)
print(p2.weight)
for att in dir(p1):
    print(att)
# p1=human()
# print(p1.name)
# p1.name="Steve"
# print(p1.name)
# p1.age=21
# p1.weight(200)
# print(p1.weight)