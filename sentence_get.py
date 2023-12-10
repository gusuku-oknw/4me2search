import requests #リクエストモジュールを使用
from bs4 import BeautifulSoup #BeautifulSoup4をつかいHTMLの解析に使う

def get_text_color_from_url(url, element_selector): #WEBページとCSSのソースファイルを取得する関数
    try:
        # ウェブページからHTMLを取得
        response = requests.get(url) #responseに指定されたURLのHTMLを取得し格納
        response.raise_for_status()  # HTTPプロトコルのエラーチェック

        # HTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser') #BeautifulSoupにてHTMLの解析

        # 指定されたCSSセレクタで要素を取得
        element = soup.select_one(element_selector) #CSSセレクタの取得、elementに格納

        if element: #要素があるとき処理
            # 取得した要素のHTMLを表示
            print(f"取得した要素のHTML: {element}")

            # 要素のスタイルから色を取得
            color = element.get('style') #要素のスタイル属性より色を取得
            print(f"取得した色: {color}")

            # CSSファイルのURLを取得
            css_file_url = None #CSSファイルの格納変数初期化
            link_element = soup.select_one('link[rel="stylesheet"]') #CSSファイルの指定
            if link_element:
                css_file_url = link_element.get('href') #CSSファイルのURLを取得し格納
                print(f"CSSファイルのURL: {css_file_url}")

                # CSSファイルの内容を取得
                css_response = requests.get(css_file_url) #CSSファイルのリクエストU
                css_response.raise_for_status() #CSSファイルのHTTPプロトコルエラーチェック
                css_content = css_response.text #CSSファイルの内容を取得
                print(f"CSSファイルの内容:\n{css_content}")

            return color

        return None

    except requests.exceptions.RequestException as e: #例外処理時にexceptブロック
        print(f"Error: {e}")
        return None

# ウェブページのURLを指定する①
url = 'https://appletools.blog/scraping-practice/'

# 取得したい要素のCSSセレクタを指定
element_selector = 'head'

# 要素のスタイルから色を取得
text_color = get_text_color_from_url(url, element_selector)
