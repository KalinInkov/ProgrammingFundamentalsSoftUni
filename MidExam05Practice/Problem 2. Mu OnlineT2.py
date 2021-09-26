import sys
from io import StringIO

test_input1 = "rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000"
test_input2 = "cat 10|potion 30|orc 10|chest 10|snake 25|chest 110"

sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)

initial_health = 100
initial_bitcoins = 0
best_room = 0

room = input().split("|")
# print(room)

for el in room:
    command = el.split()
    best_room+=1
    if command[0] == "potion":
        current_health = initial_health
        initial_health+=int(command[1])

        if initial_health == 100:
            continue
        elif int(command[1])==0:
            continue
        else:

            if initial_health>100:
                initial_health=100
                amount = 100-current_health
                print(f"You healed for {amount} hp.")
            else:
                print(f"You healed for {int(command[1])} hp.")
        print(f"Current health: {initial_health} hp.")

    elif command[0] == "chest":
        print(f"You found {int(command[1])} bitcoins.")
        initial_bitcoins += int(command[1])
    else:
        initial_health -= int(command[1])
        if initial_health <= 0:
            print(f"You died! Killed by {command[0]}.")
            print(f"Best room: {best_room}")
            break
        else:
            print(f"You slayed {command[0]}.")

if initial_health:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
