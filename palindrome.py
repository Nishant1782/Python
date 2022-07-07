n = input('Enter any number to check if it is palindrome or not')
if(n == n[::-1]):
    print('Palindrome Number')
else:
    print('Not Palindrome')    
