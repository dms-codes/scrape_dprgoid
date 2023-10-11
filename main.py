import requests
from bs4 import BeautifulSoup as bs
import csv
from urllib.parse import urljoin

# Constants
BASE_URL = "https://www.dpr.go.id/anggota/index/propinsi/"
TIMEOUT = 30
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

# Function to extract and clean text from an element
def extract_text(element):
    return element.text.strip() if element else ''

def fetch_details(session, url):
    anggota_data = {
        'Nama': '',
        'URL': url,
        'Email': '',
        'Tempat & Tanggal Lahir': '',
        'Agama': '',
        'No.Anggota': '',
        'Fraksi': '',
        'Daerah Pemilihan': '',
        'Biografi Singkat': '',
        'Riwayat Pendidikan': '',
        'Riwayat Pekerjaan': '',
        'Riwayat Organisasi': '',
        'Riwayat Pergerakan': '',
        'Riwayat Penghargaan': '',
    }

    html = session.get(url, timeout=TIMEOUT, headers=HEADERS).content
    soup = bs(html, 'html.parser')

    anggota_data['Nama'] = extract_text(soup.find('h3', class_='text-center'))
    anggota_data['Email'] = extract_text(soup.find('h1', class_='text-center'))

    details = soup.find('div', class_='keterangan mb40').find_all('div', class_='input pull-left')
    anggota_data['Tempat & Tanggal Lahir'] = details[1].text.strip().replace(':', '')
    anggota_data['Agama'] = details[2].text.strip().replace(':', '')

    anggota_data['No.Anggota'], anggota_data['Fraksi'], _, anggota_data['Daerah Pemilihan'] = [e.text for e in soup.find('div', class_='anggota').find_all('div', class_=None)]

    categories = ['Riwayat Pendidikan', 'Riwayat Pekerjaan', 'Riwayat Organisasi', 'Riwayat Pergerakan', 'Riwayat Penghargaan']
    for i, e in enumerate(soup.find_all('div', class_='link-list')):
        res = '\n'.join([ee.text for ee in e.find_all('li')])
        anggota_data[categories[i]] = res

    menu = soup.find('ul', class_="side-category-menu list-unstyled").find_all('li')[1]
    menu_url = urljoin(url, menu.find('a', href=True)['href'])
    html_menu = session.get(menu_url, timeout=TIMEOUT, headers=HEADERS).content
    soup_menu = bs(html_menu, 'html.parser')
    anggota_data['Biografi Singkat'] = soup_menu.find('div', class_='cerita').text.strip()

    return anggota_data

def main():
    session = requests.Session()
    with open('data_anggota_dpr.csv', 'w', newline='') as f:
        fieldnames = ['Nama', 'URL', 'Email', 'Tempat & Tanggal Lahir', 'Agama', 'No.Anggota', 'Fraksi',
                      'Daerah Pemilihan', 'Biografi Singkat', 'Riwayat Pendidikan', 'Riwayat Pekerjaan',
                      'Riwayat Organisasi', 'Riwayat Pergerakan', 'Riwayat Penghargaan']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, 34):
            url = f"{BASE_URL}{i}"
            html = session.get(url, timeout=TIMEOUT, headers=HEADERS).content
            soup = bs(html, 'html.parser')
            for tr in soup.find('table', {'id': 'data-anggota2'}).find_all('tr'):
                try:
                    url_ = urljoin(url, tr['onclick'].replace("location.href='", "").replace("'", ""))
                    anggota_data = fetch_details(session, url_)
                    writer.writerow(anggota_data)
                    f.flush()
                except:pass
                
if __name__ == '__main__':
    main()
