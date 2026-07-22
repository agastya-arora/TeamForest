import find_cycles as fc
import get_all_minors

def create_sequence(vertices,matrix):
    for y in range(1,vertices):
        all_minors = get_all_minors.get_minor(matrix,vertices,y)
        NumCollections = 0 #Counts number of valid sub forests for y vertices
        for minor in all_minors:
            cycle_status = fc.find_cycle(minor)
            if not cycle_status:
                NumCollections += 1 #Adds if no cycle is found
        list.append(NumCollections) #creates list of number of forests for i-1 to i+1
    return list
