from flask import Flask, request, jsonify, make_response
from datetime import datetime

app = Flask(__name__)

# Эндпоинт для возврата текущей даты
@app.route('/date', methods=['GET'])
def get_date():
    # Получаем текущую дату
    now = datetime.now()
    # Создаем список из 10 000 записей с текущей датой
    data = [{"year": now.year, "month": now.month, "day": now.day} for _ in range(10000)]
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'public, max-age=300'
    return response

# Эндпоинт для возврата имени, полученного из POST-запроса
@app.route('/name', methods=['POST'])
def get_name():
    # Получаем имя из формы
    name = request.form.get('name')
    # Проверяем, что имя было предоставлено
    if not name:
        return "Name is required", 400
    # Создаем список из 10 000 записей с полученным именем
    data = [{"name": name} for _ in range(10000)]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)