import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "Ufa"
}

# Преобразование Python-объекта в JSON-строку
json_string = json.dumps(data)
print(json_string)


json_string = '{"name": "Alice", "age": 30, "city": "Ufa"}'

# Парсинг JSON-строки в Python-словарь
data = json.loads(json_string)
print(data)            # {'name': 'Alice', 'age': 30, 'city': 'Ufa'}
print(data['name'])

