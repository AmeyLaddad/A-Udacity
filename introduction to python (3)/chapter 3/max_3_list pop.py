def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    sorted_list = sorted (input_list,reverse=True)
    output = sorted_list[:3]
    return output
    
print(top_three([2,2,2,2,4,64,7,47,5,10]))
