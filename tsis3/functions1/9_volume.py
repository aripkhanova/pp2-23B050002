def volumeSphere(radius: float): 
   fp = (4/3) * 3.142 
   sp = radius ** 3 
   volume = fp * sp 
   return volume

print("Radius: ")
r = int(input())
v = volumeSphere (r)
print("Volume: ", v)