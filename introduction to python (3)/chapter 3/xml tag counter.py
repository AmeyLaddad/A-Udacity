""" a function, `tag_count`, that takes as its argument a list
of strings. It return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and end with a right angle bracket ">".
"""
#Define the tag_count function
def tag_count(list_of_strings):
    count = 0
    for x in range (len(list_of_strings)):
        if list_of_strings[x].startswith("<"): 
            if list_of_strings[x].endswith(">"):
                count += 1            
    return count


list1 = ['<greeting>', 'Hello World!', '</greeting>', 'hiii']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))
