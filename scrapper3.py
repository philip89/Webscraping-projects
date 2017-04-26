import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import sys
#####################################################################################       
# The code here is scrapping the names from the century webpage
url = 'https://www.ssa.gov/OACT/babynames/decades/century.html'    
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
html = resp.read()
soup = BeautifulSoup(html, 'html.parser')
tagged_value = soup.find_all("td")
va = str(tagged_value)
#This is then parsing the html to get rid of the tags ao that is can be used
class HTMLCleaner(HTMLParser):
    container =""
    def handle_data(self,data):
        self.container += data
        return self.container

h = HTMLCleaner()
h.feed(va)
code = h.container
# I am trying to split up the string returned from the HTML PArser so it can be printed properly
code = code.strip('[')
code = code.strip(']')
code = code.split(",")
for i in range(len(code)):
    code[i] = code[i].strip()
names = [i for i in code if i.isalpha()]# This looks through each
#element in the list and if there is anything other than an alphabetic letter it will remove it
top10 = []
for i in range(1,21):
    top10.append(names[i])
# I now have the top ten boys and girls names from the century so I can now get the information about each name
#################################
#Printing boys and girsl names to screen
end = 0
while end == 0:

    print('The following are the 10 most popular boys and girls names of the last century')
    print('\n')
    print('Boys')
    for i in range(0,len(top10),2):
        print("   ",top10[i])
    print('\n')
    print('Girls')
    for i in range(1,len(top10),2):
        print("   ",top10[i])
    print('\n')
    print('Type in one of the names to see detailed information on where the name ranked in each decade and which decade it was used most and least')
    print('\n')
    print('Please enter the name you want to search. Names are case sensitive')
    #print('\n')
    i = 0
    while i == 0:
        name = input()
        if name not in top10:
            print('Please enter a name in the list. Remember names are case sensitive')
        else:
            i = 1
    
######
# This is looping through each decade to find the required name in each decade
    decade = ['1880','1890','1900','1910','1920','1930','1940','1950','1960','1970','1980','1990','2000','2010']
    fp = open('scr.txt','w')
    str1 = ''

    for i in range(len(decade)):
        count = 0
        url2 = 'https://www.ssa.gov/OACT/babynames/decades/names'+decade[i]+'s.html'
        req2 = urllib.request.Request(url2)
        resp2 = urllib.request.urlopen(req2)
        html2 = resp2.read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        tagged_value2 = soup2.find_all("td")
        va2 = str(tagged_value2)
#########################
#This is then parsing the html to get rid of the tags ao that is can be used
        class HTMLCleaner(HTMLParser):
            container2 =""
            def handle_data(self2,data2):
                self2.container2 += data2
                return self2.container2
        h2 = HTMLCleaner()
        h2.feed(va2)
        code2 = h2.container2
        code2 = code2.split(', ')
#########
# This is splitting up the string returned from the HTML Parser so it can be printed properly
        code2.pop(0)
        code2.pop(1)
        code2.pop(len(code2)-1)

        newCodeList =[]
        for p in range(2,len(code2)):
            newCodeList.append(code2[p])
        for val in newCodeList:
            count +=1
            if name == val:
                if(len(newCodeList[count-2]) > 2):
                    str1 = (newCodeList[count-4] + ', ' + val + ', ' + decade[i] + ', ' + newCodeList[count])
                    fp.write(str1)
                    fp.write('\n')
                else:
                    str1 = (newCodeList[count-2] + ', ' + val   + ', ' + decade[i]+ ', ' + newCodeList[count])
                    fp.write(str1)
                    fp.write('\n')

    fp.close()
    fg = open('testert.txt', 'w')
    fpoi= open('scr.txt','r')
    for line in fpoi:
        if name in line:
            fg.write(line)
###############################
# I am creating two lists one for decades and one for number of times names was used
# I save these lists into a dictionary with the decades as keys and number as values
    fg.close()
    d =int(0)
    fgh = open('testert.txt','r')
    plm = open('centurynames.txt' ,'w')
    pop = open('decadeAndNumber.txt','w')
    cou = 0
    didi = {}
    decadeList = []
    numberList = []
    print('\n')
# This loop is splitting ip the text file testert.txt so that the information can be used to give output to a user
    for line1 in fgh:
        line1= line1.split(', ')
        print(line1[1] + ' came '+ line1[0] + ' in the ' + line1[2])
        pxp = (line1[1] + ' came '+ line1[0] + ' in the ' + line1[2])
        plm.write(pxp)
        plm.write('\n')
        op = line1[3]
        op = op.split(',')
        o = op[1].strip('\n')
        par = op[0] + o
        decadeList.append(line1[2])
        numberList.append(par)
        popinput = (line1[2] + ':' + par)
    print('\n')
    for c in range(len(decadeList)):
        didi[decadeList[c]] = numberList[c]
# I am using the max, min keywords to get the max and min values in the dict, I can the print these out and save them to the file centurynames.txt
    ert = max(didi, key=didi.get)
    print(name + ' was highest in ' + ert + ' with ' + didi[ert] + ' people named it')
    ouy = (name + ' was highest in ' + ert + ' with ' + didi[ert] + ' people named it')
    plm.write(ouy)
    plm.write('\n')
    ertl = min(didi, key=didi.get)
    print(name + ' was lowest in ' + ertl + ' with ' + didi[ertl] + ' people named it')
    oui = (name + ' was lowest in ' + ertl + ' with ' + didi[ertl] + ' people named it')
    plm.write(oui)
    plm.write('\n')

    print('Press 0 if you would like to play again. Press any other key to quit')
    end = input()
