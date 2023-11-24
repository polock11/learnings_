x = [1,2,3,3,56,5254,7,3,35,6,7,4,52,5,465,6,5,25,6]

shoot = lambda x : x + 1 
print(shoot(12))

full_name = lambda f_n, l_n : f'Full name: {f_n} {l_n}'
print(full_name('Shakib','Polock'))

k = (lambda x,y : x + y)(9,3)
print(k)

q = lambda _list : [x for x in _list if x%2==0]

print(q(x))
 