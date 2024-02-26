def is_plndrm(n):
   
    n_str = str(n)
    
   
    return n_str == n_str[::-1]

print(is_plndrm(45654)) 
print(is_plndrm(42))     
print(is_plndrm(2019))   
print(is_plndrm(10101))  