i=0
a=0
global name
global pickup
global drop
global km
global ctype
import datetime
def mini(km):
  okm=10
  charges=okm*km
  return charges
def micro(km):
  okm=20
  charges=okm*km
  return charges
def suv(km):
  okm=30
  charges=okm*km
  return charges
def sedan(km):
  okm=40
  charges=okm*km
  return charges
name=raw_input()
nlist=['a','b','c','d','e']
if  name  not in nlist:
       print "your account is considered"
       nlist.append(name)
       
print "Enter the place from where to pick you up:"
pickup= raw_input()
print "Enter the drop point:"
drop=raw_input()
print"Enter the distance:"
km=int(raw_input())
if km<1:
  print"sorry cannot provide service"
print "Enter the type of car"
ctype=raw_input()
if ctype== 'mini':
      a=mini(km)
elif ctype=='micro':
      a=micro(km)
        
elif ctype=='suv':
      a=suv(km)
          
elif ctype=='sedan':
       a=sedan(km)
          
else:
   print"Enter correct car name!!"
fo=open("carfile.txt","r+")
fo.write (name)
fo.write("\n")
fo.write(str(km))
fo.write("\n")
fo.write(pickup)
fo.write("\n")
fo.write(drop)
fo.write("\n")
c=datetime.datetime.now()
fo.write(str(c))
fo.write("\n")
fo.write(str(a))
fo.write("\n")
    

