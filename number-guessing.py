import random
import math

lower=int(input("Enter lower bound: "))
upper=int(input("Enter upper bound: "))

x=random.randint(lower, upper)
tries=math.ceil(math.log(upper-lower+1,2))
print("You've ",tries," tries to get the integer")

count=0;
flag=False

while count<tries:
    count+=1
    guess=int(input("Enter guess: "))

    if x==guess:
        print("Congratulations! you did it in ",count," tries")

        flag=True
        break
    elif x>guess:
        print("Too Small!")
    elif x<guess:
        print("Too High!")

if not flag:
    print("The number is : %d"% x)
    print("Better luck next time!")



