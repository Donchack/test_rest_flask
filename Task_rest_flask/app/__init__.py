import requests, os

from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy


import config


app = Flask(__name__)
app.config.from_object(
        os.environ.get('FLASK_ENV')
        or config.DevelopmentConfig
)
db = SQLAlchemy(app)

from app.models import Question

@app.route('/')
def index():
    return '<h2>Это тестовая страница приложения Flask<h2>'

@app.route('/', methods = ['POST'])
def add_questions():
    uri_service_quest = 'https://jservice.io/api/random'
    # берем количество вопросов, которые нужно добавить в БД из REST запроса POST
    count_quest = int(request.json.get('questions_num', 0))
    last_quest = [] # последний сохраненный в БД вопрос
    while count_quest:
        params = {'count': count_quest}
        # делаем запрос к сервису вопросов, получаем список вопросов
        resp = requests.get(uri_service_quest, params)
        # создаем множество запрошенных вопросов
        set_quest = set(q['question'] for q in resp.json())
        # выбираем вопросоы из БД, если они есть в множестве запрошенных вопросов
        repeat_quest = Question.query.filter(Question.id_quest in set_quest).all()
        set_repeat_quest = set(q.question for q in repeat_quest)
        # получаем множество уникальных запрошенных вопросов
        set_uniq_new_quest = set_quest.difference(set_repeat_quest)
        # добавляем вопросы в БД
        for q in resp.json():
            if q['question'] in set_uniq_new_quest:
                the_quest = Question(
                        id_quest=q['id'],
                        question=q['question'],
                        answer=q['answer'],
                        created_at=q['created_at']
                )
                db.session.add(the_quest)
                last_quest = {
                        'id': q['id'], 
                        'question' : q['question'],
                        'answer' : q['answer'],
                        'created_at' : q['created_at']
                }
                count_quest -= 1    
    # выполняем транзакцию, записывая изменения в БД
    db.session.commit()
    # возвращаем последний сохраненный вопрос
    return jsonify(last_quest)
    # return str(request)