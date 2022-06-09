# https://stackoverflow.com/questions/19595499/python-continue-not-properly-in-loop?r=SearchResults


from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

trs = soup.find_all('tr')

for tr in trs:

    for link in tr.find_all('a'):
        fulllink = link.get('href')
        print (fulllink) #print in terminal to verify results

    tds = tr.find_all("td")


    try: #we are using "try" because the table is not well formatted.
       names = str(tds[0].get_text())
       years = str(tds[1].get_text())
       positions = str(tds[2].get_text())
       parties = str(tds[3].get_text())
       states = str(tds[4].get_text())
       congress = tds[5].get_text()

       print (names, years, positions, parties, states, congress)

    except exc:
      print("bad tr string")