import requests


def define_URL() :
    URL = input("Please put the URL of the website that you want to scrap : ")
    URL_complet = ("https://www."+URL+".com")
    response = requests.request(URL_complet)
    print (URL_complet,response)

define_URL()