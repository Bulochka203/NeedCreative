![pylounge](https://img.shields.io/pypi/pyversions/django?color=orange&style=for-the-badge)![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

<h1 align="center">Привет, это команда "Нужен Креатив"
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

# Основные фишки нашего `web-приложения`
 
+ Cовмещает CRM систему(для преподавателей) и игровой формат(для детей)
+ Мотивация детей посредством развития своего игрового персонажа - дерева
+ Удобство для родителей - оперативная осведомленность об основных событиях организации (новостная лента)
+ Родителям виден прогресс своего ребенка  (успехи в секции, его развитие)
+ Приложение адаптивно под любые секции доп. образования (также возможны индивидуальные заказы по замене анимации выращивания дерева на символ организации, выращивании на самом дереве других мотивационных фишек организации и т.д)

# Все только на стадии разработки
+ Сейчас готов раздел профиля ребенка, так же подготовлена примерная структура проекта
+ К стадии MVP будет готова: 
    + Новостная лента 
    + Календарь событий 
    + Режим для родителя 
    + 

# Установка

+ Использованная версия Python 3.9.6
+ Использованные версии Django 3.2.14 и 4.1.2

```
git clone https://github.com/Bulochka203/NeedCreative.git
```
```
cd dance
```
```
python3 -m venv venv
```
```
source env/bin/activate
```
```
pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
