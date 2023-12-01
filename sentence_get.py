from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_all_text_colors(url):
    # Seleniumの設定
    options = Options()
    options.headless = True  # ヘッドレスモードでブラウザを起動

    # Chromeドライバーのパスを指定
    driver_path = '/path/to/chromedriver'  # あなたの環境に合わせて変更してください

    # Seleniumでブラウザを起動
    with webdriver.Chrome(options=options) as driver:
        # 指定したURLにアクセス
        driver.get(url)

        # ページのHTMLを取得する
        html = driver.page_source

        # BeautifulSoupを使ってHTMLを解析
        soup = BeautifulSoup(html, 'html.parser')

        # ページ内のすべてのテキスト要素を取り出す
        all_text_elements = soup.find_all(text=True)

        # テキスト要素ごとにスタイルを表示する
        for text_element in all_text_elements:
            # 親要素をもとに、スタイル情報を取得
            style = text_element.find_parents()[0].get('style') if text_element.find_parents() else None
            print(f'Text: {text_element}\nStyle: {style}\n')

# WebページのURLを指定
url = 'https://scraping-for-beginner.herokuapp.com/ranking/'

# 関数を呼び出してすべてのテキストのスタイルを取得
get_all_text_colors(url)

