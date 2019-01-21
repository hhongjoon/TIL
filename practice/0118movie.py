import os
import csv
import requests
from pprint import pprint
import datetime
from datetime import timedelta
from PIL import Image
def func1():
#10주간 데이터 중 TOP 10, 

    date = datetime.datetime(2019, 1, 13)  ## 기준 날짜 설정
    str_date = date.strftime('%Y%m%d')     ## 형식으로 변환
    ago7 = timedelta(days=-7)            ## 7일 전 가는 법
    token = os.getenv("API_TOKEN")  ## token
    
    movie_list = {}               ##return 할 딕셔너리 초기화 { '영화코드':{영화명, 해당일관객수, 해당일}    }   이중 딕셔너리로 자료구조
    
    for i in range(10):# 10주반복
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={token}&targetDt={str_date}&weekGb=0"
        req = requests.get(url).json()
        for j in range(10): #페이지 내 top 10반복
            #pprint(req)
            moviecode = req['boxOfficeResult']['dailyBoxOfficeList'][j]['movieCd']
            movie_name = req['boxOfficeResult']['dailyBoxOfficeList'][j]['movieNm']
            movie_audi = req['boxOfficeResult']['dailyBoxOfficeList'][j]['audiCnt']
            movie_date = str_date
            if moviecode not in movie_list :
                movie_list[moviecode] = {'영화명':movie_name, '해당일관객수':movie_audi ,'해당일' : movie_date}

        
        date = date + ago7    # 7일전으로
        str_date = date.strftime('%Y%m%d')
    pprint(movie_list)  # 확인용
    return movie_list
   

def func2():
    with open('boxoffice.csv', newline='', encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        func2_list = []
        for row in reader:
            func2_list.append(row['영화코드'])
    
    #print(func2_list)
    token = os.getenv("API_TOKEN")  ## token
    func2_result = {}
    for i in func2_list:
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={token}&movieCd={i}"
        
        req = requests.get(url).json()
        #pprint(req)
        code = i
        movieNm = req['movieInfoResult']['movieInfo']['movieNm']
        movieNmEn = req['movieInfoResult']['movieInfo']['movieNmEn']
        movieNmOg = req['movieInfoResult']['movieInfo']['movieNmOg']
        openDt = req['movieInfoResult']['movieInfo']['openDt']  # 개봉연도
        showTm = req['movieInfoResult']['movieInfo']['showTm']
        directors = req['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'] # 감독
        watchGradeNm = req['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm'] # 등급

        #장르 2개
        genres = req['movieInfoResult']['movieInfo']['genres'][0]['genreNm']

        
        ## 배우 3명
        actor = []
        actor_count = len(req['movieInfoResult']['movieInfo']['actors'])
        if actor_count >=3 :
            actor_count = 3
            for act in range(actor_count):
                actor.append(req['movieInfoResult']['movieInfo']['actors'][act]['peopleNm'])
        elif actor_count == 2 :
            for act in range(actor_count):
                actor.append(req['movieInfoResult']['movieInfo']['actors'][act]['peopleNm'])
            actor.append('')
        elif actor_count == 1:
            actor.append(req['movieInfoResult']['movieInfo']['actors'][0]['peopleNm'])
            actor.append('')
            actor.append('')
        else:
            for act in range(3):
                actor.append('')


        # 입력
        func2_result[code] = {'영화명':movieNm,'영화명_영어':movieNmEn ,'영화명_원문' : movieNmOg,
                             '개봉연도':openDt ,'상영시간':showTm, '장르': genres,
                              '감독명':directors, '관람등급':watchGradeNm, '배우1':actor[0], '배우2':actor[1], '배우3':actor[2] }
    
    return func2_result

     
    
    
def func3():
    with open('movie.csv', newline='', encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        func3_list = []
        for row in reader:
            func3_list.append((row['영화명'], row['영화코드']))
    #print(func3_list)
    #검색

    n_key = os.getenv("NAVER_KEY")
    n_secret = os.getenv("NAVER_SECRET")

    func3_result={}
    for i in func3_list:
        #print(i[0])
        url = f"https://openapi.naver.com/v1/search/movie.json?query={i[0]}&display=10&start=1"
        headers = {
            "X-Naver-Client-Id": n_key,
            "X-Naver-Client-Secret": n_secret
        }
        req = requests.get(url, headers = headers).json()
        #pprint(req)
        image = req['items'][0]['image']
        link = req['items'][0]['link']
        userRating = req['items'][0]['userRating']
    
   
    # 입력
    
        func3_result[i[1]] = {'이미지':image,'링크':link ,'평점' : userRating}
    
    #print (func3_result)
    return func3_result

def func4():
    # os.mkdir('./images')
    with open('movie_naver.csv', newline='', encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        #func4_list = []
        for row in reader:
            image_url = row['이미지']
            r = requests.get(image_url, stream=True)
            with open(f'./images/row', 'wb') as f:
                for chunk in r:
                    f.write(chunk)
    

            
            


def make_csv(data):  # 엑셀로 열면 제대료 열림


    with open('boxoffice.csv', 'w', newline='', encoding = 'utf-8') as f:
        fieldnames = ('영화코드', '영화명', '해당일관객수', '해당일')
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for key, value in data.items():
            writer.writerow({'영화코드': key, '영화명': value['영화명'], '해당일관객수':value['해당일관객수'], '해당일':value['해당일']})

        pass

def make_csv_func2(data):
    with open('movie.csv', 'w', newline='', encoding = 'utf-8') as f:
        fieldnames = ('영화코드', '영화명', '영화명_영어', '영화명_원문', '개봉연도','상영시간','장르',                 ## 맨위 헤더
                              '감독명', '관람등급', '배우1', '배우2', '배우3')
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for key, value in data.items():                     ## 작성
            writer.writerow({'영화코드': key, '영화명': value['영화명'], '영화명_영어':value['영화명_영어'], '영화명_원문':value['영화명_원문'],
                             '개봉연도':value['개봉연도'],'상영시간':value['상영시간'],'장르':value['장르'],
                             '감독명':value['감독명'], '관람등급':value['관람등급'], '배우1':value['배우1'], '배우2':value['배우2'], '배우3':value['배우3']})

        pass
def make_csv_func3(data):  # 엑셀로 열면 제대료 열림


    with open('movie_naver.csv', 'w', newline='', encoding = 'utf-8') as f:
        fieldnames = ('영화코드', '이미지', '링크', '평점')
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for key, value in data.items():
            writer.writerow({'영화코드': key, '이미지': value['이미지'], '링크':value['링크'], '평점':value['평점']})

        pass


def main():
    result = func1()
    make_csv(result)
    result2 = func2()
    make_csv_func2(result2)

    result3 = func3()
    make_csv_func3(result3)
    # func4()
    pass


if __name__ == "__main__":
    main()