def is_legal_list(lst):
    print(lst)
    NumOfRows=lst.pop(0) #removes first element from the list
    if len(lst)%NumOfRows!=0:
        return False
    for i in lst:
        if i!=0 or i!=1:
            return False
    return True
    
    
    




