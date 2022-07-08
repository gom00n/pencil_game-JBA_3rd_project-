from random import randint
while True:
    a = input("How many pencils would you like to use:")
    if a.isdigit() and a != "0":
        break
    elif a == "0":
        print("The number of pencils should be positive")
    else:
        print("The number of pencils should be numeric")

print("Who will be the first (John, Jack):")
names = ["John", "Jack"]
while True:
    name=input()
    if name not in names:
        print("Choose between John and Jack")
    else:
        break
if name == "John":
    counter = 0
else:
    counter = 1
moves = [3, "", 1, 2]
while int(a) > 0:

    print("|"*int(a))
    print(names[counter % 2]+"'s turn:")

    if counter % 2 == 1:
        if int(a) % 4 == 1:
            if int(a) == 1:
                x = 1
            else:
                 x = randint(1, 3)

        else:
            x = moves[int(a) % 4]
        print(x)

    else:
        x = input()
        if x not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            continue
        if int(x) > int(a):
            print("Too many pencils were taken")
            continue
    a = int(a) - int(x)
    counter += 1
print(names[(counter)%2],"won!")
