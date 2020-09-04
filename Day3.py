# pilot question
h = input("ENTER THE HEIGHT OF PLANE:")
h = int(h)
if h <= 1000:
    print("Safe to Land")
elif 1000 <= h <= 5000:
    print("Bring Down to 1000")
else:
    print("Turn Around")

# loop questions using range
p = input("Enter a number between 0 to 200:")
p = int(p)
b1 = True
if p == 1:
    print(p, " is prime")
elif p == 2:
    print(p, " is prime.")
else:
    for i in range(2, p):
        if p % i == 0:
            print(p, " is not prime")
            b1 = False
            break
    if b1:
        print(p," is a prime number")