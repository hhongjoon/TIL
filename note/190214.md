190214

```html
{% extends 'base.html'%}
{% block title %}STATIC{%end block%}

{% block css %}
    <link rel="stylesheet" href="{% static 'style.css' %}" type="text/css">
{% endblock %}

{% block body %}
    <img src="{% static 'balls.jpg' %}" alt='image'></img>
{% endblock %}
```

```
python manage.py startapp utilites
```

---

app을 만들고 INSTALLED_APPS에 추가

app을 두개 만들면 파일명들이 겹침 -> 경로를 지정해야함



세팅에 먼저 만든 앱으로 들어가서 진행하기에 home/templates/home/.html 이런식으로 진행