print("hello\n")

g = 6.67 * (10**-11)
 
mass1 = float(input("enter the mass of planet 1"))

mass2 = float(input("enter the mass of planet 2"))

raduis = float(input("enter the distance between them"))

print("u entered" , g , mass1, mass2, raduis)

gForce = (g*mass1*mass2)/(raduis**2)
print("the gravitionjal force betwwen them is : " , gForce)