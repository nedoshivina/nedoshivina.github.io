import requests  # Подключение библиотеки requests
from collections import Counter  # Импортирование counter из библиотеки collections для подсчета людей с одинаковым возрастом
ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711' # Сервисный ключ (уже созданный)
API_VER = '5.71'  # Версия api
FRIENDS = []  # Список друзей
def calc_age(uid):
    # Запрос данных о пользователе т.к. в запросе друзей нужен айди, а пользователь может ввести никнейм. Поэтому надо конвертировать ник в айди
    x = requests.get("https://api.vk.com/method/users.get?v={}&access_token={}&user_ids={}".format(API_VER, ACCESS_TOKEN, uid))
    ID = x.json()['response'][0]['id']  # Добавляем айди
    global temp, keys
    # Запрос данных о друзьях
    r = requests.get('https://api.vk.com/method/friends.get?v={}&access_token={}&user_id={}&fields=bdate'.format(API_VER, ACCESS_TOKEN, ID))
    for i in range(r.json()['response']['count']):  # От 0 до количества друзей
        try:  # Выполняем инструкцию, которая может породить исключение
            if (r.json()['response']['items'][i]['bdate']).count(".") == 2:  # Подсчет двух точек, т.к. у некоторых нет даты рождения или она состоит только из дня и месяца
                temp = int(r.json()['response']['items'][i]['bdate'][::-1][:4][::-1])  # Вычисление года
                temp = 2020 - temp  # Вычисление возраста
                FRIENDS.append(temp)  # Добавляем в список возраст друга
        except BaseException:  # Если исключение, то ничего не делать
            pass
    friends = (list(Counter(sorted(FRIENDS)).most_common()))  # подсчет друзей с одинаковым возрастом
    return friends
# Моё: [(19, 41), (20, 15), (18, 9), (17, 5), (21, 5), (22, 5), (30, 3), (15, 2), (16, 2), (26, 1), (83, 1), (101, 1)]
if __name__ == '__main__':
    res = calc_age('nedoshivinaasay')  # Id пользователя или никнейм
    print(res)
