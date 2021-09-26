import sys
from io import StringIO

test_input1 = """Iron, Wood, Sword
Collect - Gold
Drop - Wood
Craft!
"""
test_input2 = """Iron, Sword
Drop - Bronze
Combine Items - Sword:Bow
Renew - Iron
Craft!
"""

#sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)

journal = input().split(", ")
while True:
    command = input().split(" - ")
    if command[0]=="Craft!":
        break
    elif command[0]=="Collect":
        if command[1] in journal:
            continue
        else:
            journal.append(command[1])

    elif command[0]=="Drop":
        if command[1] in journal:
            item_to_remove = journal.index(command[1])
            journal.pop(item_to_remove)
        else:
            continue

    elif command[0] == "Combine Items":
        items = command[1].split(":")
        if items[0] in journal:
            index_to_add = journal.index(items[0])
            journal.insert(index_to_add+1,items[1])
        else:
            continue
    elif command[0]=="Renew":
        if command[1] in journal:
            index_to_move_last = journal.index(command[1])
            journal.append(command[1])
            journal.pop(index_to_move_last)
print(*journal,sep=", ")


