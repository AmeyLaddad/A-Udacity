def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename    
    with open(filename) as f:
        
        #use the for loop syntax to process each line
        for line in f:
            name = line.split(',')
            cast_list.append(name[0])
      
    #and add the actor name to cast_list
    return cast_list

print (create_cast_list('/media/hp/Timepass/A-Udacity/introduction to python (3)/chapter 4/flying_circus_cast.txt'))

