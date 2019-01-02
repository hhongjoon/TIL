1220 오후 Flask

```html
#한 줄씩 나오게끔

{% for i in my_num %}
<h1>{{ i }}</h1>       
{% endfor %}
```





---

---

---

```python
@app.route("/naver")
def naver():
    return render_template("naver.html")
```



```html
naver.html

<h1>네이버 검색</h1>
<form action = "https://search.naver.com/search.naver" >
    <input type="text" name="query"/>
    <input type="submit" value="Submit"/>
</form>
```

name = query로 해주어야 다음 화면 넘어감 (네이버에서 적용) / 다른 브라우저는 해당 값

 

```
print(1,end='')  한줄에 띄울 떄
```



새롭게 서버 켜는 방식 (파이썬에 코드를 넣어서 실행)

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

기존방식 명령창에

 flask run --host=0.0.0.0 --port=8080

```python
# debug를 넣어서 수정 저장하면 알아서 되게끔

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
```



```python
@app.route("/opgg")
def opgg():
    return render_template("opgg.html")

@app.route("/opgg_2")
def opgg_2():
    userID = request.args.get('userName')
    url = "http://www.op.gg/summoner/userName="
    user_url = url+userID
    rank = scraping(user_url)
    
    if rank is None:
         return render_template("opgg_2.html", user_rank = "없는 사용자")
    
    if rank == "unranked":
        return render_template("opgg_3.html", user_rank = rank.text)

    else:
        return render_template("opgg_4.html", user_rank = rank.text)

    
def scraping(my_url):
    req = requests.get(my_url).text
    soup = BeautifulSoup(req, 'html.parser')
    #aa = soup.select("#marketindexLastList .stock_dn .item_wrp .stock_item")
    aa = soup.select_one(".SummonerRatingMedium .tierRank")


    # for i in aa:
    #     print(i.text)
    
    return aa
```

- 









```html
<h1>opgg페이지</h1>
<form action = "/opgg_2">
    <input type="text" name="userName"/>
    <input type="submit" value="Submit"/>
</form>





<h1>opgg2</h1>

<h1>{{ user_rank }}</h1>     




```









```html
# 강사님 풀이

<h1>
    {{}}님은 {{}} 점입니다.
</h1>
```

































