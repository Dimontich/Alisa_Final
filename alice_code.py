import random

from alice_class import AliceResponse, AliceRequest

print("Добро пожалывать в игру матстак. Каждому игроку в начале кона раздается по три карты\n"
      "")

ALL_CARDS = ["1a", "2a", "3a", "4a", "5a", "6a",
             "1b", "2b", "3b", "4b", "5b", "6b",
             "1c", "2c", "3c", "4c", "5c", "6c",
             "1d", "2d", "3d", "4d", "5d", "6d"]

player_card = []
Alica_card = []


## Выделяет из карты номер и масть
## @param text Название карты
## @return Кортеж из номера и масти
def parse_card(text):
    return (int(text[0]),
            text[1])


## Функция, координирующая действия бизнес-логики
def handle_dialog(request: AliceRequest, response: AliceResponse, session_data: dict):
    is_first_step = len(session_data) == 0
    if is_first_step:
        first_step(session_data)
        # TODO: greetings

    if session_data['is_player_step']:
        # TODO: ходит игрок
        pass

    else:
        # TODO: ходит Алиса
        pass

    return session_data


## Получить случайную карту
## @param args Списки с картами
def get_random_card(card_list):
    return card_list[random.randint(0, len(card_list) - 1)]


## Инициализация игрока и Алисы
## @param session_data Данные о сессии
def first_step(session_data):
    session_data['is_player_step'] = False  # True - если ход игрока, иначе - ход Алисы
    session_data['alice_data'] = dict()  # Данные об Алиса
    session_data['player_data'] = dict()  # Данные об игроке
    session_data['cards'] = ALL_CARDS.copy()  # Доступные карты
    session_data['current_card'] = None  # Карта на столе

    # Карты для Алисы и игрока
    for data in (session_data['alice_data'], session_data['player_data']):  # берем по ссылке данные
        data['card_list'] = []

        for i in range(0, 3):
            card = get_random_card(session_data['cards'])

            data['card_list'].append(card)
            session_data['cards'].remove(card)


## Получить новую случайную карту
## @param session_data Данные о сессии
## @param player_turn True, если карту берет игрок, иначе - карту берет Алиса
## @return True, если операция успешна, иначе - False
def get_new_random_card(session_data, player_turn):
    if len(session_data['cards']) == 0:
        return False

    card = get_random_card(session_data['cards'])

    data = session_data['player_data'] if player_turn else session_data['alice_data']

    data['card_list'].append(card)
    session_data['cards'].remove(card)


## Логика хода игрока
## @return Текст ответа
def player_turn(card_name, session_data):
    if len(session_data['cards']) != 0 and card_name not in session_data['cards']:
        return f'В колоде нет такой карты. Доступные карты: {str(session_data["cards"])}'

    # На столе есть карта
    if session_data['current_card']:
        player_number, player_type = parse_card(card_name)
        table_number, table_type = parse_card(session_data['current_card'])

        if player_type == table_type:
            return f'Масть карты на столе ({session_data["current_card"]}) не совпадает с Вашей картой ({card_name})'

        if player_number <= table_number:
            return f'Вы не можете побить карту на столе ({session_data["current_card"]}) ' \
                   f'Вашей картой меньшего веса ({card_name})'

        # TODO: очистить стол, убрать карту

        return f'TODO'

    # Надо положить карту на стол
    if len(session_data['cards']) == 0:
        pass
        # TODO: winner

    session_data['current_card'] = card_name

    session_data['player_data']['card_list'].remove(card_name)
    session_data['is_player_turn'] = False


def alice_turn(session_data):
    if session_data['current_card']:
        table_number, table_type = parse_card(session_data['current_card'])

        for card in session_data['alice_data']['card_list']:
            alice_number, alice_type = parse_card(card)

            if alice_type == table_type and alice_number > table_number:
                session_data['current_card'] = None
                session_data['alice_data']['card_list'].remove(card)
                break

        # Отбить не удалось
        if session_data['current_card']:
            session_data['current_card'] = None
            session_data['alice_data']['card_list'].append(session_data['current_card'])

            session_data['is_player_turn'] = True

    # Алиса кладет карту
    if not session_data['is_player_turn']:
        card_list = session_data['alice_data']['card_list']
        if len(card_list) < 3:
            get_new_random_card(session_data, False)

        if len(card_list) == 0
            card = get_random_card(card_list)


def second_step_Alica():
    try:
        j = 0
        while j < 1:
            step_a = random.randint(0, 3)

            if step_a == 0:
                a_a = random.choice(card_a)
                Alica_card.append(a_a)
                card_a.remove(a_a)

            if step_a == 1:
                b_a = random.choice(card_b)
                Alica_card.append(b_a)
                card_b.remove(b_a)

            if step_a == 2:
                c_a = random.choice(card_c)
                Alica_card.append(c_a)
                card_c.remove(c_a)

            if step_a == 3:
                d_a = random.choice(card_d)
                Alica_card.append(d_a)
                card_d.remove(d_a)
            j += 1
    except:
        print("Игра окончена. Я выиграла")


def second_step_player():
    try:
        j = 0
        while j < 1:
            step_a = random.randint(0, 3)
            if step_a == 0:
                a_a = random.choice(card_a)
                player_card.append(a_a)
                card_a.remove(a_a)
            if step_a == 1:
                b_a = random.choice(card_b)
                player_card.append(b_a)
                card_b.remove(b_a)
            if step_a == 2:
                c_a = random.choice(card_c)
                player_card.append(c_a)
                card_c.remove(c_a)
            if step_a == 3:
                d_a = random.choice(card_d)
                player_card.append(d_a)
                card_d.remove(d_a)
            j += 1
    except:
        print("Вы выиграли")


print(player_card)

print('')

print(Alica_card)
print('')
move_A = []


def randon_step():
    move_A = random.choice(Alica_card)
    Alica_card.remove(move_A)
    print(move_A)
    return move_A


def player_step():
    print("Назовите карту")
    card_p = input()
    card_p = str(card_p)
    card2 = str(card_p)
    if card_p in player_card:
        import re
        card2 = re.sub(r"\d+", "", card2, flags=re.UNICODE)
        print(card2)  # буква
        replaced = re.sub('[\D]', '', card_p)
        print(replaced)
        for t in replaced:  # отделение числа
            try:
                n = int(t)
            except ValueError:
                continue

    # Из карт выделить цыфры
    Alica_card.sort(reverse=True)
    print(Alica_card)
    myString = ''.join(Alica_card)
    s = myString
    l = len(s)
    integ = []
    k = 0
    while k < l:
        s_int = ''
        a = s[k]
        while '0' <= a <= '9':
            s_int += a
            k += 1
            if k < l:
                a = s[k]
            else:
                break
        k += 1
        if s_int != '':
            integ.append(int(s_int))
    print(integ)

    myString_1 = ''.join(Alica_card)
    s = myString_1
    l = len(s)
    integ_1 = []
    k = 0
    while k < l:
        s_int = ''
        a = s[k]
        while 'a' <= a <= 'z':
            s_int += a
            k += 1
            if k < l:
                a = s[k]
            else:
                break
        k += 1
        if s_int != '':
            integ_1.append(str(s_int))
            print(integ_1)

    pattern = card2
    for q in range(len(integ_1)):
        if pattern in integ_1[q]:
            print(q)
            break
    print("ляля" + str(integ_1))
    print("ляляля" + str(pattern))
    if card2 in integ_1:
        print("Масть есть")

        print(n)

        if integ[q] > n:
            print("отбилась")
            Alica_card.remove(integ_1)  # непраильно
            print(Alica_card)
            player_card.remove(card2)
            print(player_card)
            second_step()
            stepic_Alica()
        else:
            print("Взяла")
            if len(player_card) < 3:
                second_step_player()
            Alica_card.append(card_p)
            print(player_card)
            player_step()
    else:
        print("Беру")
        if len(player_card) < 3:
            second_step_player()
        Alica_card.append(card_p)
        print(player_card)
        player_step()


# Отбивается игрок
def stepic_Alica():
    move_A = randon_step()
    print("Мой ход - ", move_A)
    list_num = []
    for p in move_A:  # перевод в стоку
        try:
            num = str(p)
            list_num.append(num)
        except ValueError:
            continue
    # print(list_num)

    list_num1 = []
    for i in move_A:  # отделение числа
        try:
            num = int(i)
            list_num1.append(num)
        except ValueError:
            continue
    # print(list_num1)

    print("Можете отбиться")

    ans = input().lower()

    if ans == "да":
        print("Назовите карту")
        card = input()
        card = str(card)
        card1 = str(card)
        if card in player_card:
            print("Проверяю ваш ход")
            import re
            card1 = re.sub(r"\d+", "", card1, flags=re.UNICODE)
            print(card1)  # буква
            replaced = re.sub('[\D]', '', card)
            print(replaced)
            for t in replaced:  # отделение числа
                try:
                    n = int(t)
                except ValueError:
                    continue

            if card1 == list_num[1] and n > num:
                print("Отбой!")
                player_card.remove(card)
                if len(player_card) < 3:
                    second_step_player()
                if len(Alica_card) < 3:
                    second_step_Alica()
                print(Alica_card)
                print(player_card)
                player_step()
                # вызов функции отбивания Алисы
            else:
                print("Не обманывайте")
                player_card.append(move_A)
                print(player_card)
                second_step_Alica()
                print(Alica_card)
                randon_step()
                stepic_Alica()

        else:
            print("Не врите")
            player_card.append(move_A)
            print(player_card)
            second_step_Alica()
            print(Alica_card)

            stepic_Alica()
    elif ans == 'нет':
        print("Берите!")
        player_card.append(move_A)
        print(player_card)
        second_step_Alica()
        print(Alica_card)
        stepic_Alica()

    else:
        print("Я вас не поняла")
        print("Берите!")
        player_card.append(move_A)
        print(player_card)
        second_step_Alica()
        print(Alica_card)
        stepic_Alica()


if __name__ == '__main__':
    stepic_Alica()
