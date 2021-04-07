# sasohan.com
python 3.8.2

django 3.1.7

Maria DB 10.5


# Purpose

메모용 SNS


# Set Up

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
