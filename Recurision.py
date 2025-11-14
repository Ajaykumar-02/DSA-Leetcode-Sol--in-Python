# #infinte Recursion
# def name():
#     print("ak")
#     name()
# name()    

#Head Recursion  # Tc = o(n+1)= o(n) & Sc=o(n)
count=0 #global variable

def func():
    global count
    if count==4:
        return
    print("Ak")
    count +=1
    func()
func()    
 
# Tail Recursion # Tc = o(n+1)= o(n) & Sc=o(n)
count =0

def func():
    global count
    if count==4:
        return
    count +=1
    func()
    print("ak")
func()    

