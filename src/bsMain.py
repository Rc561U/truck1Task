import json

from bs4 import BeautifulSoup


# with open('page_source.html') as file:
#     soup = BeautifulSoup(file, "html.parser")
#     items = soup.select('a[data-item-name="detail-page-link"]')
#     print(items[0]['href'])
def save_data_to_json(data):
    with open("test.json", "w") as data1:
        json.dump(data, data1, indent=4, ensure_ascii=False)


dict1 = {
    "renault": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}

# with open("test.json", 'w') as file:
#     data = {
#         "ads": [
#
#         ]
#     }
#     json.dump(data,file)


with open('test.json') as file:
    data = json.load(file)
    print(data)
    data['ads'].append({
        "name": "Eaaaaa",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    }),
    save_data_to_json(data)
