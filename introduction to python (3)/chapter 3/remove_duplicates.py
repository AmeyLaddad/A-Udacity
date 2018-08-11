def remove_duplicates(input_list):
    final = []
    for x in input_list:
        if x not in final:
            final.append(x)
    return final
            
print(remove_duplicates(["india","pakistan","nepal","bhutan","USA","USA"]))    

"""
 "This is the second way" 
 
 
def remove_duplicates(input_list):
    for x in input_list:
        y = 0        
        while y<len(input_list):
            if x == input_list[y]:
                del input_list[y]

    return input_list
    
print(remove_duplicates(["india","pakistan","nepal","bhutan","USA","UK"]))
                
"""