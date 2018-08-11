def list_sum(input_list):
    # for loop adds the elements
    # of input_list to the sum variable
    sum = 0
    for x in range(len(input_list)):  
        sum = sum + input_list[x]
    
    return sum



#Test cases:
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))
