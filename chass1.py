
class k():
 

    def sides(self):
        pass
 
class l(k):
 
    # overriding abstract method
    def sides(self):
        print("I have 3 sides")

class T(): 
     def type(self): 
       print("Vegetable") 
    
class A(): 
     def type(self): 
       print("Fruit") 
    
      
def func(obj): 
       obj.type() 
     
        
obj_t = T() 
obj_a = A() 
func(obj_t) 
func(obj_a)



class Base:
    def init(self):
        self.a = "GeeksforGeeks"
        self.c = "GeeksforGeeks"



class a:
 __name= None
 __age= None
 gender= "male"
 

 def __init(self):
        self.name = "nabeel"
        self.__age = 123
 def __del(self):
    None



class b(a):
    
 def _init_(self,num,age):
    self.num=num
    self.age=age
 def _fun(num,age):
     print(f"{num} {age}")
def __fun2(num,age):
     print(f"{num} {age}")


class c(a):
 num="ali"
 

class d(b):
 pass
