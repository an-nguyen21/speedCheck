import math

speed = input("Speed: ")

if int(speed) <= 70:
    print("Ok")

elif int(speed) > 70:
   demerit = (int(speed) - 70) / 5 
   if demerit < 12:
        print(f"Score: {math.ceil(demerit)}")

if int(demerit) > 12:
    print("License suspended")

