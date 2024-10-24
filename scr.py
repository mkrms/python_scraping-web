import requests
from bs4 import BeautifulSoup
import csv

print("TOPページのURLを入力してください")
page_url = input(">> ")

print("作成するcsvファイルのURLを入力してください")
csv_filename = input(">> ")

# URLが条件に一致するかどうかを判定する関数


def is_valid_url(url):
    return url.startswith(page_url)

# 特定のURLを除外するかどうかを判定する関数


def is_excluded_url(url):
    excluded_domains = ["www.facebook.com", "facebook.com",
                        "instagram.com", "www.instagram.com", "www.x.com", "x.com"]
    for domain in excluded_domains:
        if domain in url:
            return True
    return False

# 拡張子が除外対象であるかどうかを判定する関数


def is_excluded_extension(url):
    extensions = [".jpg", ".jpeg", ".png", ".gif", ".zip", ".pdf"]
    for ext in extensions:
        if url.endswith(ext):
            return True
    return False

# 重複するURLを除去する関数


def remove_duplicate_urls(urls):
    return list(set(urls))


def write_csv(data, filename):
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['タイトル', 'URL'])
        for row in data:
            writer.writerow(row)
            # 階層ごとに空行を追加
            if row[0].count("/") == 3:
                writer.writerow([])


def scrape_site(url, scraped_urls, data):
    # URLがすでにスクレイピングされたかどうかを確認
    if url in scraped_urls:
        return

    # URLをスクレイピング
    print("Scraping:", url)
    reqs = requests.get(url)

    # ステータスコードを確認
    if reqs.status_code == 200:
        soup = BeautifulSoup(reqs.text, 'html5lib')

        # スクレイピングしたURLをリストに追加
        scraped_urls.append(url)

        # タイトルとURLを取得して表示
        try:
            title = soup.title.text
            print("Title:", title)
            print("URL:", url)
            data.append([title, url])
        except AttributeError:
            print("Title or URL not found:", url)

        # ページ内のすべてのリンクに対して再帰的に処理を行う
        for link in soup.find_all('a'):
            next_url = link.get('href')
            if next_url is not None and next_url.startswith("http") and is_valid_url(next_url) and not is_excluded_url(next_url) and not is_excluded_extension(next_url):
                scrape_site(next_url, scraped_urls, data)
            else:
                pass
    else:
        print("Failed to scrape:", url)


# TOPページのURL
top_url = page_url

# スクレイピングしたURLを格納するリスト
scraped_urls = []

# スクレイピングしたデータを格納するリスト
data = []

# TOPページをスクレイピング
scrape_site(top_url, scraped_urls, data)

# CSVファイルにデータを書き込む
filename = csv_filename
write_csv(data, filename)
print("Scraped data written to", filename)
