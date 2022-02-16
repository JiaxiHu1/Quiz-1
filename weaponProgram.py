import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, 
HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# create a file object to open the file in read mode
infile = open('weapon.txt','r')
readfile = infile.read()


# create a csv object from the file object
outfile = open("weaponResult.csv","w")



#skip the header row
next(readfile)    




#create an empty dictionary named 'weapons_dict'
weapons_dict = {"Name":{"Bullets"}} 



#use a for loop to iterate through every row of the csv file

    #use variables for name,speed and range (optional)
for record in readfile:
    outfile.writerow((record[0], record[1], record[2]))


    

    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
    

    # append the name and bullet count to 'weapons_dict'
    


    # print out the name of the weapon using the appropriate method of the object 
    
    # print out the speed of the weapon using the appropriate method of the object
    
    # print out the range of the weapon using the appropriate method of the object
    
    # print out the number of bullets of the weapon using the appropriate method of the object
    

    #use an input statement to halt the program and wait for the user - 
    input("Press any key to fire the weapon")
    

    # use an appropriate loop to keep firing the weapon until all bullets run out
    
        # call the appropriate method to fire a bullet
my_bullet = w.Weapon(name,b,speed,r,sta)


       
        # print out the bullet count every time the weapon is fired
my_bullet.fire_bullet(b,sta)
print("the number of bullet will be:",mybullet.get_bullets(b))

    


#using a loop print out the name and number of bullets from the dictionary
for b in range(10):
    my_bullet.fire_bullet(b,sta)
    print("the number of bullet will be:",mybullet.get_bullets(b))



print(weapons_dict)

outfile.close()



    


    



