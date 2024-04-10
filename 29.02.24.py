# Написать функцию, которая принимает список словарей, где каждый словарь
# представляет собой запись об ученике (с ключами 'имя', 'возраст', 'оценки'),
# и возвращает список словарей, отсортированный по возрасту учеников в порядке убывания.

students = [{"Name": "Mark", "age": 12, "marks": [7, 9, 5, 8]},
            {"Name": "John", "age": 11, "marks": [6, 8, 7, 9]},
            {"Name": "Alex", "age": 15, "marks": [9, 7, 5, 8]},
            {"Name": "Ros", "age": 14, "marks": [8, 9, 7, 9]}]

student_sort = sorted(students, key=lambda x: x['age'], reverse=True)
print(student_sort)


