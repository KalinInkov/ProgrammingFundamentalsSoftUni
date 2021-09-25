import sys
from io import StringIO

test_input1 = """10@10@10@2
Jump 1
Jump 2
Love!
"""
test_input2="""2@4@2
Jump 2
Jump 2
Jump 8
Jump 3
Jump 1
Love!
"""
#sys.stdin=StringIO(test_input1)
sys.stdin=StringIO(test_input2)


vilas_need_hearts = [int(x) for x in input().split('@')]

last_position=0
success_mission = 0
while True:
    command = input()
    if command == "Love!":
        break
    jump_l = int(command.split()[1])
    last_position+=jump_l

    if last_position<0 or last_position>= len(vilas_need_hearts):
        last_position = 0
    if vilas_need_hearts[last_position]!=0:
        vilas_need_hearts[last_position] -= 2
        if vilas_need_hearts[last_position] == 0:
            success_mission+=1
            print(f"Place {last_position} has Valentine's day.")
    else:
        print(f"Place {last_position} already had Valentine's day.")

print(f"Cupid's last position was {last_position}.")

if success_mission== len(vilas_need_hearts):
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(vilas_need_hearts)-success_mission} places.")


