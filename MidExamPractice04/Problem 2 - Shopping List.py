import sys
from io import StringIO

test_input1 = """Tomatoes!Potatoes!Bread
Unnecessary Milk
Urgent Tomatoes
Go Shopping!
"""
test_input2 = """Milk!Pepper!Salt!Water!Banana
Urgent Salt
Unnecessary Grapes 
Correct Pepper Onion
Rearrange Grapes
Correct Tomatoes Potatoes
Go Shopping!
"""
#sys.stdin=StringIO(test_input1)
sys.stdin=StringIO(test_input2)




shopping_list = input().split('!')

while True:
    command = input()
    if command == "Go Shopping!":
        break
    current_command = command.split()
    if current_command[0] == "Urgent":
        if current_command[1] in shopping_list:
            continue
        else:
            shopping_list.insert(0, current_command[1])

    elif current_command[0] == "Unnecessary":
        if current_command[1] not in shopping_list:
            continue
        else:
            index_to_delete = shopping_list.index(current_command[1])
            del shopping_list[index_to_delete]

    elif current_command[0] == "Correct":
        if current_command[1] not in shopping_list:
            continue
        else:
            index_to_change = shopping_list.index(current_command[1])
            shopping_list[index_to_change] = current_command[2]

    elif current_command[0] == "Rearrange":
        if current_command[1] not in shopping_list:
            continue
        else:
            index_to_remove = shopping_list.index(current_command[1])
            shopping_list.append(current_command[1])
            del shopping_list[index_to_remove]

print(*shopping_list, sep=', ')