
def Ton(now): 
    then = 42 
    def no(know): 
        return know * now(know) 
    return no 

then, no = 7, 4 
now = lambda oh: oh * no 
ok = Ton(now)(no)
print(ok)
