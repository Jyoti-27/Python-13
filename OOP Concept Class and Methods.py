#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Create a class called DataFolkz
# and Defne some attributes any two then create two instances of it.

class DataFolkz:
    def __init__(self,Certification,Job):
        self.Certification = Certification
        self.Job = Job
        
PCDA = DataFolkz('DataAnalytics','DataAnalyst')
PCDS = DataFolkz('DataScience','DataScientist')

print(PCDA.Certification)
print(PCDA.Job)
print(PCDS.Certification)
print(PCDS.Job)


# In[24]:


class DataFolkz:
    def __init__(self,Course,Duration):
        self.Course = Course
        self.Duration = Duration
Course1 = DataFolkz('PCDS',4)
Course2 = DataFolkz('PCDA',6)
print(Course1.Course)
print(Course1.Duration)
print(Course2.Course)
print(Course2.Duration)


# - Creare a class Cars
# - When it comes to any car there are some basic facilities such as engine,color,steering...
# - so any car will have above features which can be considered as the class features.
# - But in addition to this we can also
# 

# - If you want to call the instance attributes,those can be called only with the help of the instances.
# - But the class attributes can be called either using the class or using the instances.

# In[36]:


class Cars:
      # class variables
        no_of_wheels = 4

      # Instance Variables
        def __init__(self,color,steering):
            self.color = color
            self.steering = steering
            
midlayer = Cars("White","Automatic")
basic = Cars("Red","Manual")
print("midlayer cars",midlayer.color,midlayer.no_of_wheels,midlayer.steering)
print("basic cars",basic.color,basic.no_of_wheels,basic.steering)


# In[84]:


class Dogs:
    #class variables
    species = "mammals"
    
     #instance variables
    def __init__(self,breed):
        self.breed = breed
   
 # Create an instance of it
Snoopy = Dogs('pomerian')
Snoopy.breed
Snoopy.species
Dogs.species


# In[ ]:


class Dog
     #Initializae / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# In[19]:


class Dog:
    # Class Attribute
    species = 'Mammal'
    
    # Initializer / Instance Attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
# Instantiating the object for the class Dog
Malli = Dog("Malli",6)
Snoopy = Dog("Snoopy",7)

# Aceess the instance attributes
print("{} is {} and {} is {}.".format(Malli.name,Malli.age,Snoopy.name,Snoopy.age))
print(Malli.species)
print(Malli.name)
print(Malli.age)


# ## Methods in Python OOPS
# - 1. Class Methods
# - 2. Instance Methods
# - 3. Static Methods 

# - Create class of Cubes then create the instance attributes length,width and height then create instance method to find the volume of the cube then create some instance/object of the class Cubes and find the volume.

# In[46]:


class Cubes:
    
    # Initializer / Instance Attribute
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
   
   # Instance Methods
    def volume(self):
        return self.length*self.width*self.height
    
# Object or instances with length,width,height
Cube1 = Cubes(3,5,6)   
Cube1.volume()    # Object


# In[47]:


# TO calculate the volume of a box.
class Vol_box:
    def __init__(self):
        self.Length = float(input("Enter Length ="))
        self.Breadth = float(input("Enter Breadth ="))
        self.Height = float(input("Enter Height ="))
        #print(self.Length)
    def volume(self):
        Volume = self.Length*self.Breadth*self.Height
        print("Volume = ", Volume) 
Vol = Vol_box()
Vol.volume()
        


# -  FInd a class of Rectangles 
# - then create two instance attributes length and width
# - then create instance method to find the area
# - then create another instance method to find the primeter
# - then create two objects of the class rectangles and find the area and perimeter.
# - but please do it using the input method i.e. dynamic methods

# In[55]:


# To calculate the volume of rectangle
class Vol_rectangle:
    def __init__(self):
        self.Length = float(input("Enter Length ="))
        self.Breadth = float(input("Enter Width ="))
    def area(self):
        area = self.Length*self.Breadth
    def perimeter(self):
        Perimeter = 2*(self.Length + self.Breadth)
        print("Perimeter = ",Perimeter)
        
Vol = Vol_rectangle()
Vol.area()
Vol.perimeter()


# In[83]:


# TO calculate the area and perimeter of Rectangle.

class Rectangle:
    def __init__(self):
        self.Length = int(input("Enter Length ="))
        self.Width = int(input("Enter Width ="))
    def area(self):
        area = self.Length*self.Width
        print("Area",area)
    def perimeter(self):
        perimeter = 2*(self.Length + self.Width)
        print("Perimeter = ",perimeter)
        
rectangle1 = Rectangle()
rectangle1.area()
rectangle1.perimeter()


# - Create a class of Students - then create three instance variables math,science and social
# - then create a instance method to find the average of marks score in maths
# - then create an object of the class students and find the average

# In[77]:


class Students:
    def __init__(self):
        self.math = float(input("Enter marks scored"))
        self.science = float(input("Enter marks scored"))
        self.social = float(input("Enter marks scored"))
    def avg(self):
        avg = (self.math + self.science + self.social)/3
        print("Average mark is:",avg)
Student1 = Students()
Student1.avg()


# In[79]:


class Students:
    def __init__(self):
        self.math = float(input("Enter marks scored"))
        self.science = float(input("Enter marks scored"))
        self.social = float(input("Enter marks scored"))
    def avg(self):
        Average = (self.math + self.science + self.social)/3
        print("Average mark is:",Average)
Average = Students()
Average.avg()


# In[66]:


class Dog:
    
   # Class Attribute
     species = 'mammal'
   # Initializer / Instance Attributes
     def __init__(self,name,age):
        self.name = name
        self.age = age
        
    # Instance Method
     def description(self):
        return"{} is {} years old".format(self.name,self.age)
    
    # Instance Method
     def speak(self,sound):
        return "{} says {}".format(self.name,sound)
    
# Instantiate the dog object
Ruby = Dog("Ruby",8)

# Call our Instance Methods
print(Ruby.description())
print(Ruby.speak("Gruff Gruff"))
Ruby.name


# In[ ]:





# In[ ]:





# In[ ]:




