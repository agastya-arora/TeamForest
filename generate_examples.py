#generates example graphs and checks log concavity
from generate_list import generate_list
from string_to_graph import create_matrix
import find_cycles as fc
import get_all_minors
#Set number of examples to generate and number of vertices
vertices = 5
NumExamples = 1
for x in range(NumExamples):
    list = generate_list(vertices)
    matrix = create_matrix(vertices,list) #random graph
    print(matrix)
    for i in range(2,vertices):
        LogConcaveStatus = True
        list = []
        for y in range(i-1,i+2):
            all_minors = get_all_minors.get_minor(matrix,vertices,y)
            NumCollections = 0 #Counts number of valid sub forests for y vertices
            for minor in all_minors:
                cycle_status = fc.find_cycle(minor)
                if not cycle_status:
                    NumCollections += 1 #Adds if no cycle is found
            list.append(NumCollections) #creates list of number of forests for i-1 to i+1
        if not((list[1])*(list[1]) >= list[0]*list[2]): #Check log concavity
            LogConcaveStatus = False
    print(LogConcaveStatus)
