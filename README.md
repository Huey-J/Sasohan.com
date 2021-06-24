# sasohan.com

![image](https://user-images.githubusercontent.com/77145383/123231131-e26f3a80-d512-11eb-9ff6-73a94d69859c.png)

## Description

메모, 포트폴리오 웹


## Environment

- python 3.8.2
- django 3.1.7
- Maria DB 10.5

## Set Up

git bash에서 실행
```
source myvenv/Scripts/activate
cd sasohan_project

# 패키지 설치
pip install django
pip install mysqlclient

# DB생성 (sasohan)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 실행
python manage.py runserver
```
