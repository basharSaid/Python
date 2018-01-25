import collections

file = open('document.txt')
re = file.read()
wort = re.split()
cnt = collections.Counter(wort)

for i in cnt:
    print ('%s : %d' % (i, cnt[i]))
    
