import requests 
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'])

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        print(title)
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if vote and (points := int(vote[0].getText().replace(' points', ''))) > 99:
            hn.append({'title': title, 'link': href, 'votes': points})
        # if len(vote):
        #     points = int(vote[0].getText().replace(' points', ''))
        #     if points > 99:
        #         hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))