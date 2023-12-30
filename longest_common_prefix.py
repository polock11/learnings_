# def sol(str):
#     res =''

#     for i in range(len(str[0])):
#         for s in str:
#             if  i== len(s) or s[i] != str[0][i]:
#                 return res
#         res += str[0][i]
#     return res

# strs = ["flower","flow","flight"]
# r = sol(strs)
# print(r)

#['flight', 'flow', 'flower']
#['club','clap','clove']
#["dog","racecar","car"]



def Solution(strs):

    min = 0
    res = ''


    if len(strs) == 0:
        return res
    elif len(strs) == 1:
        return strs[0]

    k = sorted(strs)

    fw = list(k[0])
    lw = list(k[-1])


    if len(fw) > len(lw):
        min = len(lw)
    else:
        min = len(fw) 

    for i in range(min):
        if fw[i] == lw[i]:
            res += fw[i]
        else:
            break
    
    return res

l = ['flight', 'flow', 'flower']
res = Solution(l)
print(res)

