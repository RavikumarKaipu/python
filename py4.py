def order(a):
    list_a=[]
    l=len(a)
    for i in range(l):
        for j in range(i+1,l+1):
            list_a.append(a[i:j])
    return sorted(list_a)
i=input().strip()
s=order(i)
for k in s:
    print(k)
