import sys

#coundown function
def countdown(n):
    if n<=0:
        print("BlastOff")
    else:
        print(n)
        countdown(n-1)

#countup function

def countup(n):
    if n >= 0:
        print('BlastOff')
    else:
        print(n)
        countup(n+1)

#ask user to enter num

if sys.version_info[0] == 3:
    num = input("Enter number: ")
else:
    num = input("Enter number: ")

#conver string to num

num = int(num)

if num>0:
    countdown(num)
elif num<0:
    countup(num)
else:
    print("Blastoff")