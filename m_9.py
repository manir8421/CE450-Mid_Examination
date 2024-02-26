
def has_subls(ls, subls):
    
    if not subls:
        return True
    
    if not ls:
        return False
    
    if ls[0] == subls[0]:
      
        return has_subls(ls[1:], subls[1:])
    else:
        return has_subls(ls[1:], subls)


print(has_subls([], []))            
print(has_subls([3, 3, 2, 1], []))  
print(has_subls([], [3, 3, 2, 1]))  
print(has_subls([3, 3, 2, 1], [3, 2, 1]))  
print(has_subls([3, 2, 1], [3, 2, 1]))     
