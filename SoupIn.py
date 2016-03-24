from bs4 import BeautifulSoup
import urllib2
import media

#Get the desired movie title
movie_title = raw_input("What is one of your favorite movies? ")


#movie_title = "Batman Begins"

#get a web page's html from url
#html_in = urllib2.urlopen('http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html')
html_in = urllib2.urlopen('http://www.imdb.com/title/tt0372784')
#make the soup
working = BeautifulSoup(html_in, "html.parser")

#send findall() a function looking for all image tags with alt text
def get_poster_image(tag):
    tempstr = (tag)
    try:
        if (movie_title in tempstr):
            return True
    except TypeError:
        return False
    return False#tag.name == 'img' and tag.has_attr('alt')
potential_images = working.find_all('img')
#look for specific string with that list
for elem in potential_images:
    try:
        imgs = []
        if (movie_title in elem['alt'] and "Poster" in elem['alt']):
            imgs = elem['alt']
        if imgs:
            print elem['alt']
    except KeyError:
        break
#using str.find(moviename) && str.find(poster)
'''actual_image = ""
for img in potential_image:
    strtext = img#img.alt.string
    if (strtext.find("alt=\"" + movie_title) != -1 and strtext.find("Poster") != -1):
        actual_image = img
        break'''
#save that image for our poster image
try:
    print potential_images[0]['src']
except IndexError:
    print "Nothing found"
