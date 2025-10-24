import math
#----------------------polymophism----------------------
class shape:
    def perimeter(self):
        pass

class rectangular(shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def perimeter(self):
        return 2*(self.height + self.width)
    
class circle(shape):
    def __init__(self,radious):
        self.radious=radious
        
    def perimeter(self):
        return 2*math.pi * self.radious
class triangle(shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        return self.a + self.b + self.c

def area_perimeter(shape):
    return shape.perimeter()
Rectangular=rectangular(6,5)
Triangle=triangle(3,4,5)
Circle=circle(5)



print("area of triangle ",area_perimeter(Triangle))
print("area of circle ",area_perimeter(Circle))
print("area of rectangulare ",area_perimeter(Rectangular))
#-----------------iterator---------------
class counter:
    def __init__(self,max):
        self.max=max
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.current < self.max):
            self.current +=1
            return self.current
        
        raise StopIteration
print('starting count:')
for num in counter(3):
    print(num)
#___________________________
my_list=[10,20,30]
my_iterator=iter(my_list)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
#___________________________
for item in my_list:
    print(item)
print('------------------')
#___________________________
class counter_down:
    def __init__(self,value):
        self.current=value
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
           num= self.current
           self.current-=1
           return num
print('starting counter:')
for number in counter_down(4):
    print(number)
print('------------------')
    #-------------------generator function_----------
def count_up_to(max):
    count=1
    while count<=max:
        yield count
        count+=1
counter=count_up_to(10)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
#------------------
print('------------------')
square_generator=(x*x for x in range(3))

print(next(square_generator))
print(next(square_generator))
print(next(square_generator))
print('------------------')
#___________________________


