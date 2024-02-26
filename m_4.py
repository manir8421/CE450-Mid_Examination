
def horn(hood): 
    horn = hood
    def hood(horn): 
        return horn 
    return horn(hood) 

hood = lambda horn: horn(2) 

print(horn(hood))