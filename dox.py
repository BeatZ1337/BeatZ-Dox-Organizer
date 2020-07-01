#BeatZ#1337 Dox Organizer

import os, time, requests

print("BeatZ DOX Organizer")
time.sleep(1)
os.system("cls")
reason = input("Reason For Dox ")
author = input("Author Of Dox: ")
#Main Victims Details
fname = input("First Name: ")
lname = input("Last Name : ")
addyy = input("Address.   : ")
phone = input("Phone Number.: ")
#IP Address
ip = input("IP Addresses: ")
#Social Media
social1 = input("Social Media 1: ")
social2 = input("Social Media 2: ")
social3 = input("Social Media 3: ")
#Aliases
alias1 = input("Username1 : ")
alias2 = input("Username2 : ")
alias3 = input("Username3 : ")
#Parents
#Parents
mom1 = input("Moms First Name: ")
mom2 = input("Moms Last Name: ")
dad1 = input("Dads First Name: ")
dad2 = input("Dads Last Name: ")
extra = input("Any Other Shit You Wanna Add?: ")


with open("dox.txt", "a+") as f:
   f.write('Reason: '+reason+'\n')
   f.write('Dox Author: '+author+'\n')
   f.write('\n')
   f.write('First Name: '+fname+'\n')
   f.write('Last Name : '+lname+'\n')
   f.write('Address   : '+addyy+'\n')
   f.write('Phone Num.: '+phone+'\n')
   f.write('\n')
   f.write('IP Address : '+ip+'\n')
   f.write('\n')
   f.write('Social Media 1 : '+social1+'\n')
   f.write('Social Media 2 : '+social2+'\n')
   f.write('Social Media 3 : '+social3+'\n')
   f.write('\n')
   f.write('Username1 : '+alias1+'\n')
   f.write('Username2 : '+alias2+'\n')
   f.write('Username3 : '+alias3+'\n')
   f.write('\n')
   f.write('Moms First Name : '+mom1+'\n')
   f.write('Moms Last Name : '+mom2+'\n')
   f.write('Dads First Name : '+dad1+'\n')
   f.write('Dads Last Name : '+dad2+'\n')
   f.write('\n')
   f.write('Extra Info : '+extra+'\n')
   print('Organizing Dox...')
   time.sleep(1)
   print('Dox Finished.')
   
