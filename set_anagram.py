#solve 1
'''
strs = ["eat","tea","tan","ate","nat","bat"]
def ana_grp(s):
    d = {}

    for word in strs:
        val = ''.join(sorted(word))
        d[word] = val

    val_set = list(set([value for value in d.values()]))

    ana_group = []

    for i in val_set:
        group = [[k for k,v in d.items() if i == v]]
        ana_group.extend(group)
    
    return ana_group

print(ana_grp(strs))
'''

#solve 2
from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

ana_map = defaultdict(list)

for word in strs:
    s_w = ''.join(sorted(word))
    ana_map[s_w].append(word)

r = list(ana_map.values())
print (r)