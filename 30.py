def palindrome(n):
    rev = int(str(n)[::-1])
    sump = n + rev
    if sump == int(str(sump)[::-1]):
        return sump
    else:
        return palindrome(sump)
    
n = 153
sump = palindrome(n)
print(sump)
