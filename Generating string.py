import random
import numpy as np
initial=random.randint(1,10)
"multiply=random.randint(1,10)"
NumOfVertices=10
NumOfRows=random.randint(1,NumOfVertices-1)
NumOfCol=NumOfVertices-NumOfRows
NumOfElements=NumOfCol*NumOfRows
print(NumOfRows)
string=""
for i in range(NumOfElements):
    a=random.randint(0,1)
    conv=str(a)
    string+=conv
conv=str(NumOfRows)
string+=conv
print(string)