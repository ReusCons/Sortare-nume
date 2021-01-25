with open('lista_initiala.txt','r') as f:
    fam=f.readlines()
fam[-1]=fam[-1]+'\n'
q=[]
for i in fam:
    q.append(i.split())
obj=[]
t=[]
for i in q:
    lista1=list(i[0])
    lista2=list(i[1])
    obj.append(lista1[0])
    obj.append(lista2[0])
    obj=[''.join(obj)]
    t.append(obj[0])
    obj.clear()
lst=[]
p=0
for i in t:
    lst.append(i+fam[p])
    p+=1
lst.sort()
n=0
while n<len(lst):
    lst[n]=(lst[n])[2:]
    n+=1
with open('lista_ordonata.txt', 'w') as f:
    for i in lst:
        f.write(i)