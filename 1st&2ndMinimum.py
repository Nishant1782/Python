demo_list = [10,20,50,100,200,500]
temp = 0
for i in demo_list:
    if(i==200):
        temp = i
if(temp == 0):
    print('Value not found')        
v1 = temp/7
v2 = temp*(v1/100)
v3 = temp + v2    
if(v1<v2):
    if(v1<v3):
        min1 = v1
    else:
        min1 = v3
else:
    if(v2<v3):
        min1 = v2        
    else:
        min1 = v3
if(min1 == v1):
    if(v2<v3):
        min2 = v2
    else:
        max2 = v3
elif(min1 == v2):
    if(v1<v3):
        min2 = v1
    else:
        min2 = v3
else:
    if(v1<v2):
        min2 = v1
    else:
        min2 = v2        
print(f'First minimun value is {min1}')
print(f'Second minimun value is {min2}')

