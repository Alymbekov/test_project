import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

info = None

def get_html(url):
    response = requests.get(
        url=url
    )
    status_code = response.status_code
    print(status_code)
    return response.text


def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_table_structure = soup.find(
        'table', class_='table'
    )
    all_td_tags = all_table_structure.find_all('td')
    global domen
    domen = "http://kenesh.kg"
    links = list(
        map(
            lambda td: f"{domen}{td.find('a').get('href')}", all_td_tags
        ))
    filtered_list = list(set(filter(lambda link: 'deputy' in link, links)))
    return filtered_list


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    deputy_contacts = soup.find('div', class_='deputy-page')
    try:
        full_name = deputy_contacts.find('h3', class_='deputy-name').text.strip()
    except:
        full_name = ''
    try:
        phone_number = deputy_contacts.find('p', class_='mb-10').text.strip()
    except:
        phone_number = ''
    try:
        bio = deputy_contacts.find('div', id="biography").text.strip()
    except:
        bio = ''
    try:
        avatar = domen + deputy_contacts.find('div', class_='deputy-img').find('img').get('src')
    except:
        avatar = ''
    all_informations = {
        'full_name': full_name,
        'phone_number': phone_number,
        'avatar': avatar,
        'bio': bio
    }
    return all_informations

def writing_to_csv(all_info):
    import csv
    with open('deputies_information.csv', 'a', newline='') as csvfile:
        fieldnames = [
            'full_name', 'phone_number',
            'avatar', 'bio'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(
            all_info
        )


def make_all_function(url):
    html = get_html(url)
    data = get_page_data(html)
    info = data
    writing_to_csv(data)
    return data


def main():
    some_var = "http://kenesh.kg/ru/deputy/show/141/kasimalieva-aida-kamchibekovna"
    html = get_html(url="http://kenesh.kg/ru/deputy/list/35")
    all_links = get_all_links(html)
    with Pool(40) as p:
        p.map(make_all_function, all_links)
    res = make_all_function("http://kenesh.kg/ru/deputy/show/176/abdikerimov-sharshenbek-shayloobekovich")
    return res

# Точка входа в программу
if __name__ == '__main__':
    main()