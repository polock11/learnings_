def isPanlindrome(x):
    x = str(x)

    if x == x[::-1]:
        return True
    else:
        return False
    

val = isPanlindrome(1234567765432881)
print(val)