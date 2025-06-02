import math, cmath

def func():
        try:
            print(f"Enter index a (write it with a sign)*: ", end="")
            a = int(input())
            if a == 0:
                raise Exception("a can't be 0")
            print(f"Enter index b (write it with a sign)*: ", end="")
            b = int(input())
            print(f"Enter index c (write it with a sign)*: ", end="")
            c = int(input())

            D = b**2-4*a*c
            print("The discriminant is equal to:", D)
            print("The square root of the discriminant is: ", (math.sqrt(D)))

            try:
                if D < 0:
                    print("The discriminant is negative, it is impossible to extract roots without using complex numbers, do you want to continue? (Write 1 if you want to continue, 2 if not.)")
                    yn = input()

                    if yn == "1":
                        x1 = (-b + (cmath.sqrt(D))) / (2 * a)
                        x2 = (-b - (cmath.sqrt(D))) / (2 * a)
                        print("x1: ", x1, end="\n")
                        print("x2: ", x2)


                    if yn == "2":
                        print("The equation is unsolvable (without using complex numbers)")

                if (D > 0):
                    x1 = (-b + (math.sqrt(D))) / (2 * a)
                    x2 = (-b - (math.sqrt(D))) / (2 * a)
                    print("x1: ", x1, end="\n")
                    print("x2: ", x2)

            except ValueError:
                print("Value ERROR")

        except:
            print("Syntax ERROR")

func()
