import random
initial=random.randint(1,10)
multiply=random.randint(1,10)
product=initial*multiply 
string=""
for i in range(product):
    a=random.randint(0,1)
    conv=str(a)
    string+=conv
convInitial=str(initial)
convMultiply=str(multiply)
string+=convInitial
storeMultiply=(len(string)-1)//initial
print(storeMultiply)
print(string)