print('Enter three values')
v1 = int(input('Enter v1\n'))
v2 = int(input('Enter v2\n'))
v3 = int(input('Enter v3\n'))
if(v1>v2):
    if(v1>v3):
        max1 = v1
    else:
        max1 = v3
else:
    if(v2>v3):
        max1 = v2        
    else:
        max1 = v3
if(max1 == v1):
    if(v2>v3):
        max2 = v2
    else:
        max2 = v3
elif(max1 == v2):
    if(v1>v3):
        max2 = v1
    else:
        max2 = v3
else:
    if(v1>v2):
        max2 = v1
    else:
        max2 = v2 

print(f'First maximum value is {max1}')
print(f'Second maximum value is {max2}')                               