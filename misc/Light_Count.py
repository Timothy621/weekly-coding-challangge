print("Walk on hte Axis")
case_number = int(input("please input the number of test cases you want"))
case = []
x = 0
while x < case_number:
    y = input(f'insert value for case {x}')
    case.append(int(y))
    x = x+1
print("test inputs")
print(case)
for i in case:
    Total = 2 * i
    i -= 1
    while i > 0:
        Total = Total + i
        i -= 1
    print(Total)

print("Your name is Mine")
case_number = int(input("please input the number of test cases you want"))
case = []

while x < case_number:
    y = input(f'insert names for case {x} seperated by a "," example: Tom,Toma')
    case.append(y)
    x = x+1
print("test inputs")
print(case)

for i in case:
    v = i.split(",")
    print(v)
    if v[0] in v[1]:
        print(True)
        print(f'{v[0]} is in {v[1]}')
    elif v[1] in v[0]:
        print(True)
        print(f'{v[1]} is in {v[0]}')
    else:
        print(False)
