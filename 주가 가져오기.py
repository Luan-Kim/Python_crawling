import requests
from bs4 import BeautifulSoup

def print_stock_price(code, page_num):
    result = [[], []]

    for i in range(page_num):
        url = 'https://finance.naver.com/item/sise_day.nhn?code='+code+'&page='+str(i+1)
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        tr = soup.select('table > tr')

        for i in range(1, len(tr)-1):
            if tr[i].select('td')[0].text.strip():
                result[0].append(tr[i].select('td')[0].text.strip())
                result[1].append(tr[i].select('td')[1].text.strip())

        for i in range(len(result[0])):
            print(result[0][i], result[1][i])

print("조회하실 종목코드를 입력해주세요.")
stock_code = input()
pages = 1
print("13일치 해당 종목의 종가입니다.")
print_stock_price(stock_code, pages)
