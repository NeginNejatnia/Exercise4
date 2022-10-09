char = input("Enter your square: ")
width_m = int(input("Enter the width_m: "))
height_n = int(input("Enter the height_n: "))

for i in range(0,height_n):
    print(char * width_m)

print("\n".join(char * width_m for _ in range(height_n)))