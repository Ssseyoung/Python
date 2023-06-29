import urllib.request
from bs4 import BeautifulSoup

# 자동차 정보 가져오기
def getCar():
    url = 'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EC%9E%90%EB%8F%99%EC%B0%A8%ED%8C%90%EB%A7%A4%EB%9F%89&oquery=%ED%8C%90%EB%A7%A4%EB%9F%89&tqi=i5XCEdprvxZss5GVl0wssssss1C-501331&acq=%ED%8C%90%EB%A7%A4%EB%9F%89&acr=2&qdt=0'
    res = urllib.request.urlopen(url)
    result = res.read().decode('utf-8')

    bs = BeautifulSoup( result, 'html.parser' )

    # select() 함수로 자동차 이름, 판매량, 순위 가져오기
    names = bs.select('.title > a')
    quantitys = bs.select('.info_area .sub_info:nth-of-type(1)')
    rankings = bs.select('.info_area .sub_info:nth-of-type(2)')
    
    # print(quantitys)
    # print(rankings)

    car_names = []
    car_quantitys = []
    car_rankings = []

    for item in names:
        car_names.append( item.text )
        # print(item.text)
    for item in quantitys:
        car_quantitys.append( item.text )
        # print(item.text)
    for item in rankings:
        car_rankings.append( item.text )
        # print(item.text)
        
        
    count = len(car_names)
    
    for i in range(count):
        print('#################################')
        print('자동차 이름 :', car_names[i])
        print('판매량 :', car_quantitys[i])
        print('순위 :', car_rankings[i])

    # 자동차 이름, 판매량, 순위
    result = (car_names, car_quantitys, car_rankings)
    return result


getCar()