headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

string = ""
string_length = len(string)

for x in headlines:
    if string_length + len (x) > 140:
                
        break
    else:
        string +=x
news_ticker = string
print (news_ticker,"\nSting Length =",string_length)
 
