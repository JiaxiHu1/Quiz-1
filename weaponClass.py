import random

'''
Create a Weapon Class definition according to the following specs:

Attributes:

name - user supplied
bullets - random number between 10 and 100000
speed - user supplied
range - user supplied
status - 'Active' (this attribute should be changed to 'Inactive' if bullets 
                    run out.)

Methods:

Create accessor methods for each attribute.

Create a method named 'fire_bullet' that will simulate
firing a bullet. This is accomplished by decreasing the number of bullets by 1 
every time the method is called. When the bullet count reaches zero, it should change
the attribute 'status' to 'Inactive'

'''
class Weapon:
    def __init__(self,name,b,speed,r,sta):
        self.__name = name 
        self.__bullets = b
        self.__speed = speed 
        self.__range = r 
        self.__status = sta
    
    def accessor_name(self):
        self.__name
    
    def accessor_bullets(self):
        self.__bullets
    
    def accessor_speed(self):
        self.__speed
    
    def accessor_range(self):
        self.__range 

    def accessor_status(self):
        self.__status 
    
    def fire_bullet(self,b,sta):
        self.__bullets -= 1 
        if self.__bullets == 0:
            self.__status == "Inactivate"

    def get_name(self):
        return self.__name
    
    def get_bullets(self):
        return self.__bullets
    
    def get_speed(self):
        return self.__speed
    
    def get_range(self):
        return self.__range
    
    def get_status(self):
        return self.__status 










