from flask import Flask, render_template
import os

app = Flask(__name__)

# Создаем папку для загрузок если её нет
os.makedirs('uploads', exist_ok=True)

# Данные ваших проектов
projects = [
    {
        "id": 1,
        "title": "Интерактивный кинотеатр",
        "description": "Полнофункциональный сайт кинотеатра с возможностью выбора даты, времени и мест в зале. Особенность проекта - интерактивная SVG карта зала с подсветкой выбранных мест и автоматическим расчетом стоимости. Адаптивный дизайн для всех устройств.",
         "gallery": [
            "static/images/project1.jpg",
            "static/images/project1-1.jpg",
            "static/images/project1-2.jpg"
        ],
        "github": "https://github.com/vpershukova/Kinoteatr",
        "tags": ["HTML", "CSS", "JavaScript", "Интерактивная графика", "Адаптивный дизайн"]
    },
    {
        "id": 2,
        "title": "Интернет-магазин My-Giro",
        "description": "Адаптивный полнофункциональный веб-сайт интернет-магазина гироскутеров, сигвеев и электросамокатов. Полнофункциональный каталог с фильтрацией товаров по категориям, информационные разделы о компании и продукции, форма подписки на рассылку. Реализована мобильная версия с гамбургер-меню.",
        "gallery": [
            "static/images/project2.jpg",
            "static/images/project2-1.jpg",
            "static/images/project2-2.jpg"
        ],
        "github": "https://github.com/vpershukova/hoverboard",
        "tags": ["HTML", "CSS", "JavaScript", "Адаптивный дизайн"]
    },
    {
        "id": 3,
        "title": "Todolist",
        "description": "Адаптивный полнофункциональный веб-сайт для управления задачами с поддержкой тем оформления. Полнофункциональный менеджер задач с созданием, редактированием, фильтрацией и отслеживанием прогресса выполнения, возможность переключения между светлой и темной темой, информационные разделы о возможностях системы. Реализована мобильная версия с гамбургер-меню.",
        "gallery": [
            "static/images/project3.jpg",
            "static/images/project3-1.jpg",
            "static/images/project3-2.jpg",
            "static/images/project3-3.jpg"
        ],
        "github": "https://github.com/vpershukova/todolist.git",
        "tags": ["HTML", "CSS", "JavaScript", "Адаптивный дизайн", "Python"]
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True, port=5000)