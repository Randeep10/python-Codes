print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name3 = name1 + name2
lower = name3.lower()

t = lower.count('t')
r = lower.count('r')
u = lower.count('u')
e = lower.count('e')
totalTrue = t + r + u + e

l = lower.count('l')
o = lower.count('o')
v = lower.count('v')
e = lower.count('e')
totalLove = l + o + v + e

totalGrand = int(str(totalTrue) + str(totalLove))

if (totalGrand >= 10) or (totalGrand >= 90): 
    print(f"Your score is {totalGrand}, you go together like coke and mentos.")
elif (totalGrand >= 40) and (totalGrand <= 50): 
    print(f"Your score is {totalGrand}, you are alright together.")
else:
    print(f"Your score is {totalGrand}.")
