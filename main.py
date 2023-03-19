from bs4 import BeautifulSoup
import requests
import numpy as np

# link to the item's search page on MercadoLibre
link = 'https://listado.mercadolibre.com.ar/planchita-babyliss#D[A:planchita%20babyliss]'

def get_prices_by_link(link):
    # get source
    r = requests.get(link)

    # parse source
    page_parse = BeautifulSoup(r.text, 'html.parser')

    # find all list items from search results
    search_results = page_parse.findAll("li", {"class":"ui-search-layout__item shops__layout-item"})

    # initialise price list
    item_prices = []

    for result in search_results:
        price_as_text = result.find("div", {"class":"ui-search-price__second-line shops__price-second-line"}).find("span", {"class":"price-tag-fraction"}).text
        price = float(price_as_text.replace(".", ""))
        item_prices.append(price)

    return(item_prices)

def get_average(prices):
    return np.mean(prices)

print("Price list:",get_prices_by_link(link))
print("Number of items accounted for:",len(get_prices_by_link(link)))
print("Average price:",get_average(get_prices_by_link(link)))