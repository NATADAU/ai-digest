from flask import Flask, render_template

app = Flask(__name__)


ARTICLES = [
    {
        "title": "Нейросеть для создания песни ИИ бесплатно: лучшие нейросети для музыки",
        "tag": "Музыка",
        "color": "#FF6B6B",
        "summary": "ИИ не просто склеивает звуки — создаёт мелодию, ритм, аранжировку и вокал по текстовому описанию.",
        "read_time": "11 мин",
        "level": "Просто",
        "url": "https://habr.com/ru/companies/ranvik/articles/1032296/"
    },
    {
        "title": "Штампы LLM. Разбираю с новой точки зрения",
        "tag": "Промпты",
        "color": "#4ECDC4",
        "summary": "Как эксперты определяют LLM по штампам в тексте и почему все просят исключить их из генерации.",
        "read_time": "4 мин",
        "level": "Просто",
        "url": "https://habr.com/ru/articles/1032294/"
    },
    {
        "title": "Как Ричард Докинз решил, что ИИ разумен",
        "tag": "Философия",
        "color": "#FFE66D",
        "summary": "Тест Тьюринга, игра в подражание и почему некоторые люди считают, что машины уже мыслят.",
        "read_time": "7 мин",
        "level": "Просто",
        "url": "https://habr.com/ru/articles/1032262/"
    },
    {
        "title": "Доктор AI-болит: Как ИИ изменяет ландшафт медицины?",
        "tag": "Медицина",
        "color": "#A78BFA",
        "summary": "ИИ приходит на помощь, чтобы врачи сосредоточились на главном, а не на бумагах.",
        "read_time": "5 мин",
        "level": "Просто",
        "url": "https://habr.com/ru/companies/kemp_ai/articles/1032238/"
    },
    {
        "title": "API нейросетей для бизнеса в SpeShu.AI",
        "tag": "Бизнес",
        "color": "#F472B6",
        "summary": "Как российскому бизнесу интегрировать ИИ через API с оплатой в рублях и официальной бухгалтерией.",
        "read_time": "4 мин",
        "level": "Просто",
        "url": "https://habr.com/ru/companies/tsnis/articles/1032248/"
    },
    {
        "title": "Frontend Status: свежий дайджест фронтенда и AI",
        "tag": "Дайджест",
        "color": "#38BDF8",
        "summary": "AI из вау-демо переходит в дисциплину: промпт-пайплайны и практики Claude Code для предсказуемого результата.",
        "read_time": "8 мин",
        "level": "Просто",
        "url": "https://habr.com/ru/articles/1032276/"
    },
    {
        "title": "Сделаем Python безопасным… снова",
        "tag": "Код",
        "color": "#FB923C",
        "summary": "Как перехватить выполнение Python-кода, запретить опасные вызовы и построить систему контрактов.",
        "read_time": "33 мин",
        "level": "Средне",
        "url": "https://habr.com/ru/companies/otus/articles/1029676/"
    },
    {
        "title": "Как Ричард Докинз решил, что ИИ разумен",
        "tag": "Сознание",
        "color": "#34D399",
        "summary": "Современные комментаторы игнорируют детали оригинальной игры Тьюринга — но будущее уже наступило.",
        "read_time": "7 мин",
        "level": "Просто",
        "url": "https://habr.com/ru/articles/1032262/"
    },
    {
        "title": "SmileLadder. Цикл «Память и мозг». Как формируется память",
        "tag": "Нейронаука",
        "color": "#F87171",
        "summary": "Как работает механизм внимания и как мозг формирует память — ответ на вопрос, как мы справляемся с потоком задач.",
        "read_time": "6 мин",
        "level": "Средне",
        "url": "https://habr.com/ru/articles/1032310/"
    }
]


@app.route("/")
def index():
    return render_template("index.html", articles=ARTICLES)


if __name__ == "__main__":
    app.run(debug=True)
