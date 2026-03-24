from flask import Flask, render_template, abort

app = Flask(__name__)

cats_list = [
    {
        "id": "pes",
        "name": "ПесДюк",
        "role": "Красавчик",
        "desc": "Кудись ходун, десь полежун та професійний муркотун.",
        "full_bio": "Тут довга історія про те, як ПесДюк підкорив цей світ своєю красою...",
        "button_text": "Вся краса тут",
        "img": "dyuk.jpg",
        "gallery": ["dyuk1.jpg", "dyuk2.jpg", "dyuk3.jpg", "dyuk4.jpg", "dyuk5.jpg", "dyuk6.jpg", "dyuk7.jpg", "dyuk8.jpg", "dyuk9.jpg", "dyuk10.jpg"]
    },
    {
        "id": "mysh",
        "name": "Мишка",
        "role": "Ти щось їси?",
        "desc": "Трошки з заскоками, припадками і обідками.",
        "full_bio": "Мишка — це енергія в чистому вигляді. Її хобі: випрошувати їжу та бігати з улюбленою іграшкою.",
        "button_text": "Дивитись фото",
        "img": "mysh.jpg",
        "gallery": ["mysh1.jpg", "mysh2.jpg"]
    }
]

@app.route('/')
def index():
    return render_template('index.html', cats=cats_list)

@app.route('/cat/<cat_id>')
def cat_detail(cat_id):
    cat = next((item for item in cats_list if item["id"] == cat_id), None)
    if cat:
        return render_template('cat_detail.html', cat=cat)
    return "Котика не знайдено 😿", 404

if __name__ == '__main__':
    app.run(debug=True, port=8180)
