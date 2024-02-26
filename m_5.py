

pear = "ni" 
def apple(banana): 
    def plum(peach): 
        pear = lambda pear: peach(pear) 
        return pear 
    return plum(banana)("ck") 

print(apple(lambda peach: pear + peach))