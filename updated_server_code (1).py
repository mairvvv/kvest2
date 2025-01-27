
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Папка для хранения изображений
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Модуль для работы с квестами
quests = []

# Главная страница
@app.route('/')
def index():
    return 'Добро пожаловать в админ-панель для добавления квестов!'

# Добавление нового квеста
@app.route('/add-quest', methods=['POST'])
def add_quest():
    if 'image' not in request.files:
        return jsonify({'message': 'Нет изображения!'}), 400

    image = request.files['image']
    name = request.form['name']
    price = request.form['price']
    duration = request.form['duration']
    description = request.form['description']
    address = request.form['address']  # Новый параметр для адреса

    # Сохранение изображения
    image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_filename)

    # Добавление квеста в список
    new_quest = {
        'name': name,
        'price': price,
        'duration': duration,
        'description': description,
        'address': address,  # Сохраняем адрес
        'image': image_filename
    }
    quests.append(new_quest)

    return jsonify({'message': 'Квест добавлен успешно!'})

if __name__ == '__main__':
    app.run(debug=True)
