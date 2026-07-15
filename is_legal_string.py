def is_legal_list(lst):
    print(lst)
    NumOfRows=lst.pop(0) #removes first element from the list
    for i in lst:
        if i!=0 or i!=1:
            return False
    if len(lst)//NumOfRows:
        return True
    else:
        return False
    
    
    




