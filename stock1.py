# stock1.py
#
# [출처] [Python] 실습: 시가총액 상위 200개 종목 엑셀로 가져오기|작성자 작은거인
# https://blog.naver.com/passionisall/222074595074
#
# 코스피와 코스닥 가져오기

import pandas as pd
import requests

for sosok in range(2):
    merge=[] 
    for page in range(1,30):
        url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=' + str(sosok) + '&page=' + str(page)
        r = requests.get(url)
        # read_html : requests의 r을 r.text로 가져와도 되고 , url 자체를 가져오고 인코딩해도됨
        df = pd.read_html(url,encoding='euc-kr')
        merge.append(df[1].dropna(how='all').drop('토론실',axis=1))
    
    if sosok == 0:
        kospi = pd.concat(merge)
        kospi.to_excel('kospi.xlsx')
    elif sosok == 1:
        kosdaq = pd.concat(merge)
        kosdaq.to_excel('kosdaq.xlsx')




