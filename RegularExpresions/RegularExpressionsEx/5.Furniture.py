import re
# import sys
# from io import StringIO
#
# test_input1 = """>>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase
# """
#
# sys.stdin = StringIO(test_input1)




total_money_spend = 0
command = input()
pattern = r">>(?P<FurniteName>[a-zA-Z]+)<<(?P<Price>[0-9]+|[+-]?[0-9]+\.[0-9]+)!(?P<Quantity>\d+)"
purchases = []
while not command=="Purchase":
    match = re.match(pattern,command)
    if match:
        data = match.groupdict()
        purchases.append(data['FurniteName'])
        total_money_spend+=float(data['Price'])*int(data['Quantity'])
    command = input()



#
print("Bought furniture:")
#
# for el in purchases:
#
#     print(el['FurniteName'])
#     #print(float(el['Price'])*float(el['Quantity']))
#     current_money = float(el['Price'])*float(el['Quantity'])
#     total_money_spend+=current_money
if purchases:
    print('\n'.join(purchases))
print(f"Total money spend: {total_money_spend:.2f}" )