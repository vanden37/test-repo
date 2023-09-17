temp = list(map(int, input().split()))
reg = str(input())
print("test=3", reg)
            
if reg == 'heat':
    if temp[0] >= temp[1]:
            print(temp[0])
    else:
            print(temp[1])
if reg == 'freeze':
    if temp[0] >= temp[1]:
            print(temp[1])
    else:
            print(temp[0])
if reg == 'fan':
            print(temp[0])
if reg == 'auto':            
            print(temp[1])