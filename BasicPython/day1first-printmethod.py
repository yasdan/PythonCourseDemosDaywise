#print("Tip Calculater")
# def tipcalculator():
#     bilamt=float(input("What is the total bill amount $"))
#     tipercent=int(input("What percentage tip do you like to give"))
#     persons=int(input("How many persons to split the bill"))
#     shareforone=round((bilamt+(bilamt*tipercent/100))/persons,2)
#     print(f"Each person should pay: ${shareforone}")

#tipcalculator()
import time
# def printRectangle():
#     rows = int(input("Enter no.of rows for rectangle shape? "))
#     for i  in range(1,rows+1):
#         for j in range(rows+2):
#             print("**",end='')
#             time.sleep(.25)
#         print()
#printRectangle()




def printDiamond():
    rows= int(input("How many rows for Diamond shape : "))
    for i in range(1,rows+1):
        for j in range(1,rows-i+1):
            print(end=' ')
        for k in range(0,2*i-1):
            print("*",end='')
            time.sleep(0.10)
        print()
    for i in range(1,rows):
        for j in range(1,i+1):
            print(end=" ")
        for k in range(1,(2*(rows-i))):
            print("*",end='')
           # time.sleep(0.06)
        print()
printDiamond()






