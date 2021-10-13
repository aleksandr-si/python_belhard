class donkey:
    def donkey_hight(self,hight):
        self.hight=hight
        return(self.hight)
class horse:
    def donkey_hight(self,hight):
        self.hight=hight+20
        return(self.hight)
    def horse_color(self,color):
        self.color=color


class mul(horse,donkey):
    def count(self,count):
        self.count=count

class mul2(donkey,horse):
    def count(self,count):
        self.count=count
a=mul()
a.count(12)
print(a.donkey_hight(12))

a1=mul2()
a1.count(12)
print(a1.donkey_hight(12))

# for att in dir(a):
#     print(att)
    