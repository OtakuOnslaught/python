print("SQUARE AND CUBES ")

n =  int(input("enter the no.- "))
while(True):
    s=input("do you want to find the square or the cube  of the no. (or type leave to exit the program)- ")
    if s .lower() == "square":
        print(n*n)
        
    elif s.lower() == "cube":
        print(n*n*n)
    else:
        break