
def romanToInt(s):
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    x = list(s)
    r = 0
    for i in range(0, len(x)-1):
        if m[x[i]] >= m[x[i+1]]:
            r = r + m[x[i]]
        else:
            r = r - m[x[i]]
    r = r + m[x[-1]]
    return r

num  = romanToInt('MMDCLXXIV')
print(num)