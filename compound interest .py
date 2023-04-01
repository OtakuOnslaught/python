import time
print("Calculation of the Compound interest and the Simple interest")
time.sleep(1)
while(True):
    rate = float(input("please enter the rate of interest - "))
    if rate > 100 :
       print("invalid")
    else:
          break
time.sleep(1)
prin = int(input("please enter the amout of money -")) 
time.sleep(1)
time = int(input("please enter the time limit - "))
A= (prin*(1+ rate/100)**time)
CI = (A-prin)
SI= (prin*rate*time/100)
print("your SIMPLE INTEREST =" , SI)
print("your COMPOUND INTEREST =", CI)