'''
Created on 18 nov 2024

@author: joaqu
'''


q2 = [] 

for i,x in enumerate(range (10,300,7)): 

   if i%2==0: 

       q2.append(x*x) 


print(q2)





q = {x**2 for n,x in enumerate(range(10,300,7)) if n%2==0}
print(q)