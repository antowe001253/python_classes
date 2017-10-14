class fraction (object):
    def __init__(self,num,denom):
        self.num=num
        self.denom=denom

    # Here we have the getters
    def getNum(self):
        return self.num
    def getDenom(self):
        return self.denom

    def convert(self):#c=fraction(4,5)
        return (self.num/self.denom)

    def __str__ (self):#print(c)
        return "< "+str(self.num)+"/"+str(self.denom)+" >"

    def __add__(self,other):#c+d  with d=fraction(6,5)
        top=(self.num*other.denom)+(self.denom*other.num)
        return fraction(top,self.denom*other.denom)

class Living(object):
    tag=1# class variable which migh chane when Lving,tag is called when having Living.tag+=1
    def __init__ (self,age):
        self.age=age
        self.name=None
        Living.tag+=1# at every instance created, Living.tag will incearse

        # getter
    def setName(self,name):
        self.name=name
    def setAge(self,age):
        self.age=age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def __str__(self):
        return "< Tag -> "+str(Living.tag)+" Name -> "+self.name+" Age -> "+str(self.age)+" >"

class Cat(Living):# is is getting all properties and behaviors of Living
    def speak(self):
        print("MIOW")

    def __str__(self):# this method is overwittern
        return "< CAT | Name: "+self.name+" Age: "+str(self.age)+" >"

class Person(Living):
        def __init__ (self,name,age,height):
            Living.__init__(self,age)# getting constructor from Living
            Living.setName(self,name)# getting constructor from Living
            self.friends=[]# new parameter
            self.height=height# New paramater

        def setHeight(self,height):
            self.height=height
        def setFriends(self,friends):
            self.friends.append(friends)

        def getHeight(self):
            return self.height

        def getFriends(self):
            return self.friends

        def __str__(self):
            return "< Person/Tag -> "+str(Living.tag)+" Name -> "+self.name+" Age -> "+str(self.age)+" Height -> "+str(self.height)+" Friends -> "+str(self.friends)+" >"
