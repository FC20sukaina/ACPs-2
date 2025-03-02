class Robot:

   species ="robot"

   def __init__(self,name,age):
         self.name= name
         self.age= age

Bolt= Robot("Bolt",20)
Quantam= Robot(" Quantam",2)

print("Bolt is a {}".format(Bolt.species))
print("Quantam is also a {}".format(Quantam.species))

print("{} is {} years old".format( Bolt.name, Bolt.age))
print("{} is {} years old".format( Quantam.name, Quantam.age))