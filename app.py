from flask import Flask, render_template, abort
import os

app = Flask(__name__)

def get_cat_photos(cat_id):
    folder_path = os.path.join('static', 'images', cat_id)
    if os.path.exists(folder_path):
        # Додаємо images/ перед назвою папки кота
        photos = [f"images/{cat_id}/{file}" for file in os.listdir(folder_path) 
                  if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        return sorted(photos)
    return []

cats_list = [
    {
        "id": "pes",
        "name": "ПесДюк",
        "role": "Красавчик",
        "desc": "Кудись ходун, десь полежун та професійний муркотун.",
        "full_bio": "Тут довга історія про те, як ПесДюк підкорив цей світ своєю красою...",
        "button_text": "Вся краса тут",
        "img": "dyuk.jpg",
        "gallery": get_cat_photos("pes")
    },
    {
        "id": "mysh",
        "name": "Мишка",
        "role": "Ти щось їси?",
        "desc": "Найдобріша кішка. Але трошки з заскоками, припадками і обідками.",
        "full_bio": "Мишка — це енергія в чистому вигляді. Її хобі: випрошувати їжу та бігати з улюбленою іграшкою.",
        "button_text": "Дивитись фото",
        "img": "mysh.jpg",
        "gallery": get_cat_photos("mysh")
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
