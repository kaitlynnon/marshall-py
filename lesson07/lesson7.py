# Lesson 7
from random import randrange

dc = int(input("Enter the difficuty class (1-20): "))

roll = randrange(1,21)
print(f"You have rolled {roll} on the dice")

if roll >= dc:
    d20 = randrange(1,20)
    print("You succeeded the ability check")
else:
    print("You did not succeed the ability check")