def palindrome(num):
    if (num==num[::-1]):
        return'palindrome'
    else:
        return'notpalindrome'

num=input('enter the number')
s= palindrome(num)
print (s)