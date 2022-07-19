my_list = [1,'a',5.5,'shree']
l_int = []
l_float = []
l_string = []

for a in my_list:
    if(type(a) == type(1)):
        l_int.append(a)
    elif(type(a) == type('String')):
        l_string.append(a)
    elif(type(a) ==type(1.2)):
        l_float.append(a)
    else:
        print(f'type of {a} is not from integer or string or float')
print(l_int)
print(l_float)
print(l_string)   
list_length = [len(l_int), len(l_float), len(l_string)]

print(max(list_length))                 