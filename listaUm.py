
l = [11,5,34,7,9,8,22,13,20,21,19]
tam_l = len(l)
#algoritmo ordenamento BUBLE
print("ORDENAMENTO - BUBLE")
print(l)

for i in range(tam_l):
    troca = False
    for j in range(1,tam_l - i):
        if l[j] < l[j-1]:
            l[j],l[j-1] = l[j-1],l[j]
            print(l)
            troca = True
    if not troca: break       
print(l)


#algoritmo ordenamento INSERTEION
print("ORDENAMENTO - ISERTION")
lis2 = [11,5,34,7,9,8,22,13,20,21,19]
print(lis2)
tam_lis = len(lis2)
for i in range(tam_lis):
    for j in range(1,tam_lis):
        if lis2[j] < lis2[j-1]:
            lis2[j],lis2[j-1] = lis2[j-1], lis2[j]
            print(lis2)
            for k in range(j,0,-1):
                if lis2[k] < lis2[k-1]:
                    lis2[k],lis2[k-1] = lis2[k-1], lis2[k]
                    print(lis2)
print(lis2)
#algoritmo ordenamento por SELECT
print("ORDENAMENTO - SELECT")
lis2 = [11,5,34,7,9,8,22,13,20,21,19]
print(lis2)
tam_lis = len(lis2)
x=1
for i in range(tam_lis):
    for j in range(x, tam_lis):
        if lis2[i] > lis2[j]:
            lis2[i], lis2[j] = lis2[j], lis2[i]
            print(lis2)
       
    x = x+1
print(lis2)    
   
            
        
    
                                    
        
