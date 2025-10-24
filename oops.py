#3--------------------------___________-_-----Encapsulation in Python------------------------
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_details(self):
        print(f"age:{self.name},name: {self.age}")

s1=Employee('hiba',23)
s1.display_details()
#_________________public________________________
class Employee1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_method(self):
        print({self.name},{self.age})
  
a1=Employee('hiba',23)
print(a1.name,a1.age)
#-------------------protected-------------------
class Person:
    def __init__(self,name,place):
        self.name=name
        self._place=place
    def dispaly(self):
        return self._place
    
a2=Person('ammu',"karuvarankund")
print(a2.dispaly())
print(a2.name)
#_________________private___________
class person2:
    def __init__(self,name,address):
        self.name=name
        self.__address=address
    def display(self):
        print( self.__address) #✅ Modify address safely using setter
    def set_adderss(self,adderss):
        if isinstance(adderss,str):
            self.__address=adderss
        else:
            print('invalide address')
           

q1=person2('cvdgc','cgfbchbj')
q1.display()
q1.set_adderss('dcfvbn')

q1.display()

#------------Using Protected Members-- Encapsulation in Python----
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

class AddFeatures(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.__battery = battery

    def show_details(self):
        print(f"brand: {self.get_brand()}, model: {self.get_model()} - battery {self.__battery} kWh")

s1 = AddFeatures("Tesla", "Model 3", 75)
s1.show_details()

#------------Using private Members-- Encapsulation in Python-----------------------------
class car2:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model

    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
class add_features(car2):
    def __init__(self, brand, model,battery):
        super().__init__(brand, model)
        self.__battery=battery

    def show_details(self):
        print(f"brand: {self.get_brand()},model: {self.get_model()}-battery{self.__battery}kWh")
        print(f"brand: {self.get_brand()}, model: {self.get_model()} - battery {self.__battery} kWh")
s1=add_features("Tesla", "Model 3", 75)
s1.show_details()
#---------------------------inheritance------
# ----------sinle inheritance-------
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

#--------------------------multiple-inheritance------
class animal:
    def __init__(self,name):
       self.name=name
    def speak(self):
        print(f'{self.name} animal speaks')
class dog(animal):
    def bark(self):
        print(f'{self.name} the dog can bark')
d=dog('tommy')
d.speak()
class cat(dog):
    def run(self):
        print(f'{self.name} they also can walk')
e=cat('pappi')
e.speak()
e.run()
e.bark()
#-------------multiple inheritance------
class mother:
    def __init__(self,eyes):
        self.eyes=eyes
class father:
    def __init__(self,hair):
        self.hair=hair
class child(father,mother):
    def __init__(self, hair,eyes,name):
        father.__init__(self,hair)
        mother.__init__(self,eyes)
        self.name=name
    def charactor(self):
        print(f'the {self.name} has {self.eyes} eyes and {self.hair} hair')
child2=child('brown','blue',"manu")
child2.charactor()
#-------------hirarchical---inheritance________
class parent:
    def beauti(self):
        print('they are so beauty')
class child1(parent):
    pass
class child2(parent):
    pass
ch1=child1()
ch2=child2()
ch1.beauti()
ch2.beauti()
#--------------------------
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass #_--------output "class b"

d = D()
d.show()
#________________'overriding"______
class animal:
    def speak(self):
        print('the animal was making code')
class dog(animal):
    def speak(self):
        print('dog making bark')

f=dog()
f.speak()
#-------------can access the parent method ------
class animal:
    def speak(self):
        print('the animal was making code')
class dog(animal):
    def speak(self):
        super().speak()
        print('dog making bark')

f=dog()
f.speak()
 
    


