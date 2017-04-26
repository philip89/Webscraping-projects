import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
###########################################
fh = open('topten-2015.txt', 'w')

###########################################
#Every thing in here is taking the HTML code from the website
#Going through it and taking everything with a td tag out and storeing it in va
url = 'https://www.ssa.gov/OACT/babynames/'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
html = resp.read()
soup = BeautifulSoup(html, 'html.parser')
tagged_value = soup.find_all("td")
va = str(tagged_value)
############################################
#This is then parsing the html to get rid of the tags ao that is can be used
class HTMLCleaner(HTMLParser):
    container =""
    def handle_data(self,data):
        self.container += data
        return self.container

h = HTMLCleaner()
h.feed(va)
code = h.container
#############################################
# I am trying to split up the string returned from the HTML PArser so it can
#be printed properly
code = code.strip('[')
code = code.strip(']')
code = code.split(",")
for i in range(len(code)):
    code[i] = code[i].strip()
#print(code)
print("Position     Boys       Girls")
fh.write('Position     Boys       Girls')
fh.write('\n')
print()
for i in range(0,30,3):
    print("   ",code[i] ,"      ", code[i+1],"-----",code[i+2])
    fh.write('   ')
    fh.write(code[i])
    fh.write('          ')
    fh.write(code[i+1])
    fh.write('-----')
    fh.write(code[i+2])
    fh.write('\n')
