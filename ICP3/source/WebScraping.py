# ICP3

# Importing Required Libraries
import urllib.request
from bs4 import BeautifulSoup


wikiURL = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
openURL = urllib.request.urlopen(wikiURL)


soup = BeautifulSoup(openURL, "html.parser")

# Title of the Page
title = soup.find('title')
print("Title Of The PAGE ", title.text)



# Finding all anchor Links in WebPage
links = soup.find_all('a')

# Iterating the Links and showing Href values of the anchor tag
print("Links:")
for link in links:
    print(link.get('href'))

# Finding the right table.
tableData = soup.find('table', {'class': 'wikitable sortable plainrowheaders'})
# Finding tr's (Ignoring Header Row)
tableRows = tableData.findAll('tr')[1:]

# Iterating the tr's
for trData in tableRows:
    # Printing the th tag text
    print("th (State)-->",  trData.find('th').text)
    state = trData.find('th').text
    # Finding all td tags
    tds = trData.findAll('td')

    # Checking the index range with length of td and getting required data
    if 1 in range(len(tds)):
        ac = tds[1].text
        print("Adminstrative Capitals -->", ac)
    if 2 in range(len(tds)):
        lc = tds[2].text
        print("Legislative Capitals -->", lc)
    if 3 in range(len(tds)):
        jc = tds[3].text
        print("Judiciary Capitals -->", jc)
    if 4 in range(len(tds)):
        yc = tds[4].text
        print("Year of Capital establishment -->", yc)
    # Not displaying Empty Data
    if 5 in range(len(tds)) and tds[5].text.strip() != '':
        fc = tds[5].text
        print("Former Capital -->", fc)
    # Writing to a Row in CSV file

