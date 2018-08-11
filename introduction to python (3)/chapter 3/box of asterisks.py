def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box
   
    # print sides of box
    for i in range(height-2):    
        print("*" + " " * (width-2) + "*") 
    
    print("*" * width) #print bottom edge of box

# Test Cases
print("Test 1:")
starbox(5, 5) 
print("Test 2:")
starbox(2, 3)  

print("Test 3:")
starbox(9, 9) 
