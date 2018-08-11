import time
import urllib
import requests
import bs4

start_url = "https://en.wikipedia.org/wiki/Roman_Reigns"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = ["https://en.wikipedia.org/wiki/Roman_Reigns"]

def find_first_link(url):
    
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # This div contains the article's body

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None

    article_link = None

    # Find all the direct children of content_div that are paragraphs

    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return 

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link


def continue_crawl(search_history,target_url,Iterations = 25):
    if search_history[-1] == target_url: 
        print ("We've found the target article :",search_history[-1])
        return False
    elif len(search_history) > Iterations:
        print ("Too many Iterations !!! \nAborting the crawl")
        return False
    elif search_history[-1] == search_history[:-1]:
         print ("We have been to this page previously. Its a cycle and we should avoid it. \nAborting the crawl")
         return False
    else:
        return True
    
while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    time.sleep(2) # Slow things down so as to not hammer Wikipedia's servers
