a = input("First Value: ")
b = input("End Value: ")

try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Error: First Value and End Value must be filled and must be a number")
else:
    p = True
    if a >= 2 and a <= b:
        print("Prime Numbers: ", end="")
        while a < b:
            p = True
            c = a // 2
            if a <= 3:
                print(a, end=" ")
                p = "null"
                a += 1
            elif a % 2 != 0 and c > 3:
                for i in range(3, c + 1, 2):
                    if a % i == 0:
                        p = False
                        break
            elif a % 2 == 0:
                p = False

            if p == True:
                print(a, end=" ")
                a += 2
            elif a % 2 == 0:
                a += 1
            elif p == False:
                a += 2
        
        print()
        print()
        print("Done.")    
    else:
        print("Error: Sorry, the Program cannot be run because First Value is less than 2 or higher than Final Value")