# Домашнее задание к занятию 3. Функции. Разработка приложения ToDo

## Задание 1
Реализуйте функцию `count_letter`, которая принимает список слов и некоторую букву и возвращает количество слов в списке, в которых эта буква встречается хотя бы один раз.

Например, для списка `['python', 'c++', 'c', 'scala', 'java']` и буквы `c` ваша функция должна вернуть число 3.

### Подсказки
- Используйте конструкцию `for word in ...` для итерации по списку. 
- Используйте переменную для хранения промежуточного результата подсчета.
- Используйте конструкцию `letter in word` для проверки наличия буквы в слове.

### Ответ:
Реализовал данную функцию таким образом, [файл прилагаю](../Homeworks_py/03/Task03.1.py):
```python
def count_letter(word_list, letter):
    count = 0
    for word in word_list:
        if letter in word:
            count += 1
    return count


list_words = ["python", "c++", "c", "scala", "java"]

print(count_letter(list_words, "c"))
```   

## Задание 2
Зарегистрируйтесь на сайте https://www.pythonanywhere.com/.

### Ответ:
Зарегистрировался.

### Инструкция

Инструкция по работе с PythonАnywhere доступна по ссылке: https://github.com/netology-code/guides/blob/master/python%20anywhere/instruction.md

Любые вопросы по решению задач задавайте в чате в Telegram.