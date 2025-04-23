import requests
from bs4 import BeautifulSoup
import pprint

respon= requests.get('https://news.ycombinator.com/')
soup=  BeautifulSoup(respon.text,"html.parser")
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

def sorted_hn(hnlist):
  return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for index, item in enumerate(links):
    title = links[index].getText()
    href = links[index].get('href',None)
    votes = subtext[index].select('.score')
    if len(votes):
      points = int(votes[0].getText().replace(' points',''))
      if points > 99:
        hn.append({'title': title, 'links': href, 'votes': points})


  return sorted_hn(hn)

pprint.pprint(create_custom_hn(links, subtext))