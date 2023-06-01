def diffie_hellman():
    n=int(input("Enter Prime Modulo N. : "))
    g=int(input("Enter Primetive Prime No G. : "))
    
    # Private Keys for Alice and Bob 
    Xa=int(input("Enter the Private key for Alice : "))
    Xb=int(input("Enter the Private key for Bob : "))
    
    #compute public values
    Ya=g**Xa %n
    Yb=g**Xb %n
    
    #check same keys
    Ka=Yb**Xa %n
    Kb=Ya**Xb %n
    
    return [Ka==Kb,Ka]
if __name__=='__main__':
    result=diffie_hellman()
    success=result[0]
    if success:
        print("Alice and Bob can communicate ")
        print("They share secret no. : ",result[1])
    else:
        print("Alice and Bob cannot communicate")