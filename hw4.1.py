"""
Завдання 1
Макс 20 балів
написати програму, яка просить в користувача ввести через пробіл міста, в яких він був за минулі 10 років
потім окремо запросити у користувача міста, куди він хоче поїхати внаступні 10 років
вивести на екран повідомлення з текстом про те, що користувачу, мабуть, дуже сподобалося в містах, які він повторив в
двох циклах вводу, а саме... (сформувати строку, використовуючи join)
якщо повтору не було - вивести повідомлення, що користувач відкритий до чогось нового

врахувати випадки, що користувач нічого не вводить не потрібно, в даному випадку вам явно зазначено,
що ці перевірки не потрібні.
не потрібно перевіряти введення цифр
ми виходим із того, що користувач введе щось на зразок "Київ Тернопіль париЖ акапулько-80"

В той же час врахуйте, що користувач може вводити дані в різних регістрах

використати сети!!!
"""
MSG_UR_OPEN_TONEW = 'Ви відкриті до чогось нового!'


user_city_visited = set(input("Введіть міcта в яких ви були за останні 10 років. --> ").title().split())
user_want_visit = set(input("Введіть міста куди хотіли б поїхати в наступні 10 років --> ").title().split())

intersection = user_city_visited & user_want_visit
text = ' ,'.join(intersection)
if intersection:
    print(f'Ви були в містах:{text}')
else:
    print(MSG_UR_OPEN_TONEW)