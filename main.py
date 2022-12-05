import requests
from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"
    }

    r = requests.get("https://cars.av.by/filter?page",headers=headers)

    with open("av.html","w",encoding="utf8") as file:
        file.write(r.text)

    soup = BeautifulSoup(r.text,"lxml")

    find_cars = soup.find_all(class_="listing-item__title")
    find_carsCost = soup.find_all(class_="listing-item__prices")

    cars = []
    costs = []

    for item in find_cars:
        if item.find("a",class_="listing-item__link") is not None:
            cars.append(item.text)
    
    for i in find_carsCost:
        if i.find(class_="listing-item__price") is not None:
            costs.append(i.text)
    
    for item in cars:
        for i in costs:
            print(item,'|',i)


def main():
    get_data("https://cars.av.by/filter?page")


if __name__ == '__main__':
    main()
