import random
import numpy as np

def generate_list(n):
    NumOfVertices=n
    NumOfRows=random.randint(1,NumOfVertices-1) # number of rows of the block
    NumOfCol=NumOfVertices-NumOfRows # number of columns in the block
    NumOfElements=NumOfCol*NumOfRows #in the block
    print(NumOfRows)
    lst=[]

    for i in range(NumOfElements):
        a=random.randint(0,1)
        conv=str(a)
        lst.append(conv)
    
    conv=str(NumOfRows)
    lst.append(conv)
    return(lst)
