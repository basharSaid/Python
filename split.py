import collections
from collections import Counter

file = open('document.txt')
re = file.read()
a = re.split()

cnt=Counter()
cnt.update(a)

print(cnt)


    

        

        

        

 
    

        











