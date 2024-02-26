

x = "x"
g = x 

def x(x): 
    g = "h" 
    if x == g: 
        return x + "i" 
    x = lambda x: x(g) 
    return lambda g: x(g) 

x = x(x)(x) 
print(x)