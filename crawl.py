__author__ = 'GongLi'

import requests
from bs4 import BeautifulSoup

class Dish:

    def __init__(self, soupTag):

        temp = soupTag.find("img").attrs
        self.imageLink = temp['data-src']
        self.dishName = temp['alt'][:-5].strip()

        self.recipeLink = soupTag.find("a", class_="image-link").attrs['href']
        self.materials = soupTag.find("p", class_='ing ellipsis').text.strip(" \n")

    def __unicode__(self):

        return self.dishName +"\t"+ self.imageLink +"\t"+ self.recipeLink +"\t"+ self.materials



def parseData(data):

    soup = BeautifulSoup(data.text)
    dishes = soup.find_all("div", class_ ='recipe-140-horizontal pure-g')

    for dish in dishes:
        dishObject = Dish(dish)
        yield dishObject


if __name__ == "__main__":

    file = open("dishes.csv", "w")
    index = 1
    for i in range(50):
        url = 'http://www.xiachufang.com/category/40076/pop/?page=' + str(i)
        data = requests.get(url)

        for item in parseData(data):

            print unicode(index) +u'\t'+unicode(item)
            file.write((unicode(item) +u'\n').encode('utf-8'))
            index += 1

    file.close()

