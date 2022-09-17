import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
    
'''
Fungsi Scarape merupakan fungsi yang berfungsi untuk melalukan scaraping data berita 
dari rss jambi.antaranews.com, fungsi ini akan menghasilkan list of dict yang berisi 
data berita dengan detail sebagai berikut:
{
    url: -> url dari artikel berita,
    judul: -> judul dari berita,
    waktu_tayang: -> waktu tayang berita yanng berbentuk unix timestamp,
    konten: -> ini artikel berita
}
'''
def Scrape():
    page_rss = requests.get('https://jambi.antaranews.com/rss/terkini.xml')
    soup = BeautifulSoup(page_rss.text, 'xml')
    channel_tag = soup.find_all('channel')
    result = {
        'status': False,
        'data' : None
    }
    data_final = []
    for item in channel_tag:
        urls = [text.get_text() for text in item.find_all('link')][1:]
        title = [text.get_text() for text in item.find_all('title')][1:]
        times = []
        for str_time in item.find_all('pubDate'):
            time_text = str_time.get_text()
            timestamp = time.mktime(datetime.strptime(time_text, "%a, %d %b %Y %X %z").timetuple())
            times.append(
                int(timestamp)
            )
        for index, url in enumerate(urls):
            req = requests.get(url)
            page_detail_berita = BeautifulSoup(req.content, 'html.parser')
            content = page_detail_berita.find('div', {'class':'post-content clearfix'})
            content = content.text
            clear_content = ''.join(content.strip().splitlines())
            data = {
                "url": url,
                "judul": title[index],
                "waktu_tayang": times[index],
                "konten": clear_content
            }

            data_final.append(data)
        result['status'] = True
        result['data'] = data_final

    return result

    
            