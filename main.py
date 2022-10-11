import requests


intelligence_dict = {}


def get_intelligence(hero_name):
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    orders = response.json()
    for hero in orders:
        if hero["name"] == hero_name:
            intelligence = hero["powerstats"]["intelligence"]
            intelligence_dict[hero_name] = int(intelligence)


get_intelligence("Hulk")
get_intelligence("Captain America")
get_intelligence("Thanos")

A = list(intelligence_dict.values())
B = list(intelligence_dict.keys())
print(f"Наибольший интерллект у персонажа {B[A.index(max(A))]} - {A[A.index(max(A))]}")