n = int(input('Enter any number to check if it is magic number or not:\n'))
sum = 0
for d in str(n):
    sum += int(d)
t = str(sum)
rev = t[::-1] 
rev = int(rev)
if(rev*sum == n):
    print('Magical')
else:
    print('Not Magical')    