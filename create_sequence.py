import find_cycles as fc
import get_all_minors as gam

def create_sequence(matrix):
    lst=[]
    vertices=len(matrix[0])
    for y in range(1,vertices+1):
        all_minors = gam.get_minor(matrix,vertices,y)
        NumCollections = 0 #Counts number of valid sub forests for y vertices
        for minor in all_minors:
            cycle_status = fc.find_cycle(minor)
            if not cycle_status:
                NumCollections += 1 #Adds if no cycle is found
        lst.append(NumCollections) #creates list of number of forests for i-1 to i+1
    return lst
