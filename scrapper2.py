import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import sys
###########################################
#Every thing in here is taking the HTML code from the website
#Going through it and taking everything with a td tag out and storeing it in va
url = ''
####################################################
fh = open('decadenames.txt', 'w')
####################################################
print('This program will show you the most popular baby names for any decade from the 1880s to 2010. Use the list below to choose a decade')
print('You can also choose how many names you would like to se from 1 to 200')
#print('which decade do you want to use')
#print('Decades----number')
print('2010 press 1')
print('2000 press 2')
print('1990 press 3')
print('1980 press 4')
print('1970 press 5')
print('1960 press 6')
print('1950 press 7')
print('1940 press 8')
print('1930 press 9')
print('1920 press 10')
print('1910 press 11')
print('1900 press 12')
print('1890 press 13')
print('1880 press 14')
####################################################
d = 0
print('Please enter a number between 1 and 14. If you do not want to play press a different key')

while d == 0:
#    try:
    dec2 = input()
    if not dec2.isdigit():
        sys.exit();
    else:
        dec =int(dec2)
    if dec < 1 or dec > 14:
        print('Please choose a number between 1 and 14')
        d = 0
    else:
        d = 1
#   except ValueError:
#        print('please enter a number')
#        d = 0
decade = ''
#####################################################
p = 0
print("How many results would you like to see? Choose between 1 and 200 results")
while p == 0:
    try:
        number = int(input())
        if number < 1 or number > 200:
            print('Please choose a number between 1 and 200')
            p = 0
        else:
            p = 1
    except ValueError:
        print('please enter a number between 1 and 200')
        p = 0
#####################################################
if dec == 1:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names2010s.html'
    decade = '2010s' 
elif dec == 2:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names2000s.html'
    decade = '2000s'
elif dec == 3:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1900s.html'
    decade = '1990s'
elif dec == 4:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1980s.html'
    decade = '1980s'
elif dec == 5:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1970s.html'
    decade = '1970s'
elif dec == 6:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1960s.html'
    decade = '1960s'
elif dec == 7:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1950s.html'
    decade = '1950s'
elif dec == 8:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1940s.html'
    decade = '1940s'
elif dec == 9:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1930s.html'
    decade = '1930s'
elif dec == 10:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1920s.html'
    decade = '1920s'
elif dec == 11:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1910s.html'
    decade = '1910s'
elif dec == 12:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1900s.html'
    decade = '1900s'
elif dec == 13:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1890s.html'
    decade = '1890s'
elif dec == 14:
    url = 'https://www.ssa.gov/OACT/babynames/decades/names1880s.html'
    decade = '1880s'

###########################################
#Every thing in here is taking the HTML code from the website
#Going through it and taking everything with a td tag out and storeing it in va

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
#print(code[50])
my_list = [item for item in code if item.isalpha()]# This looks through each
#element in the list and if there is anything other than an alphabetic letter it will remove it
#############################################

n = number
number *= 2
x = 0
print("These are the top " , n ," most popular baby names in the ", decade)
print()
print("Position     Boys        Girls")
fh.write('These are the top ')
fh.write(str(n))
fh.write(' most popular baby names in the  ')
fh.write(decade)
fh.write('\n')
fh.write('Boys        Girls')
fh.write('\n')
for i in range(0,number,2):
    x += 1
    print("   ",x ,"      ", my_list[i],"-----",my_list[i+1])
    fh.write(my_list[i])
    fh.write('-----')
    fh.write(my_list[i+1])
    fh.write('\n')
