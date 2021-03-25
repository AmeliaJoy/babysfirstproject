friends=1
A = True
if A == True:
    import time
    t=time.localtime()
    p=(t[4])
    if p==14 :
        pop=input ("Do you walk up to the boy who is in a big crowd?He looks popular.(Y or N)")
        if pop=="Y":
            print("You say,\"Hello\".") 
            if friends==1:
                print("He responds,\"Hello?\"")
