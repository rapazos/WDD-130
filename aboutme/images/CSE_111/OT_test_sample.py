def take_input(): 
    try:
        val=int (input("please enter a whole number:"))
        return val
    except:
        return -1
        
def verify_number(v):
    if v-int (v)  == 0:
        return True
    else:
        return False

def  doing_work (v):
        tv = verify_number(v)
        if tv:
            v =v*5    
            return v
        else:
            return -1

def main(): 
    y=take_input()
    v= doing_work(y)
    print(v)
    
    
if __name__  == "__main__":
    main()