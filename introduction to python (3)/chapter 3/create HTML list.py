""""The html_list function takes one argument, 
a list of strings, and returns a single string which is an HTML list"""

def html_list(list_of_strings):
    #output_list = []
   #for x in list_of_strings:
    #    output_list.append(" <li> :{} </li>".format(x))
      
    print("<ul>")
    for items in list_of_strings:
        items="<li>"+items+"</li>"
        print(items)
    print("</ul>")
    
html_list(["aaa","aaa","sss"])
        