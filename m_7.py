

import math
def nrst_two(x):
    lower_power = 2 ** math.floor(math.log2(x))
    upper_power = 2 ** math.ceil(math.log2(x))
    if x - lower_power < upper_power - x:
        return lower_power
    else:
        return upper_power

print(nrst_two(8))      
print(nrst_two(11.5)) 
print(nrst_two(14))    
print(nrst_two(2019))   
print(nrst_two(0.1))   
print(nrst_two(0.75))  
print(nrst_two(1.5))  
