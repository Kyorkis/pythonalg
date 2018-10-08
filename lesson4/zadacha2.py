n = 3000


#100 loops, best of 5: 41 nsec per loop (n = 10)
#100 loops, best of 5: 41 nsec per loop (n = 30)
#100 loops, best of 5: 71.7 nsec per loop ( n = 50)
#100 loops, best of 5: 41 nsec per loop(n = 150)
#100 loops, best of 5: 41 nsec per loop(n=1500)

#12 function calls in 0.011 seconds(n=10)
#32 function calls in 0.000 seconds(n=30)
#52 function calls in 0.001 seconds(n=50)
#152 function calls in 0.001 seconds(n=150)
#1502 function calls in 0.011 seconds(n=1500)
#3002 function calls in 0.023 seconds(n=3000)


# ----Получается алгоритм с решетом намного быстрее считает ,но с большим количеством обращений----

a = [0] *n
for i in range(n):
    a[i] = i 

a[1]=0

m = 2
while m<n:
    if a[m] !=0:
        j = m*2
        while j <n:
            j = j+m
    m +=1

b = []
for i in a:
    if a[i] !=0:
        b.append(a[i])

del a
print(b)                   
#a[1] = 0
#lst = []

#i = 2
#while i <=n:
#    if a[i] !=0:
#        lst.append(a[i])
#        for j in range(i, n+1,i):
#            a[j] =0
#    i +=1
#print(lst)            