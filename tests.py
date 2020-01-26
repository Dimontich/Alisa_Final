from alice_code import get_random_card, first_step, parse_card, get_new_random_card


def test_wrong_input():
    """Проверка ввода ерунды"""
    # TODO
    pass


def test_get_random_card():
    """Проверка получения случайной карты"""

    assert get_random_card(['1c']) == '1c'


def test_first_step():
    """Проверка первого шага"""

    data = dict()
    first_step(data)

    assert data['is_player_step'] != None
    assert data['alice_data'] != None
    assert data['player_data'] != None
    assert data['cards'] != None

    assert data['alice_data']['card_list'][0] not in data['cards']
    assert data['alice_data']['card_list'][1] not in data['cards']
    assert data['alice_data']['card_list'][2] not in data['cards']
    assert data['player_data']['card_list'][0] not in data['cards']
    assert data['player_data']['card_list'][1] not in data['cards']
    assert data['player_data']['card_list'][2] not in data['cards']


def test_parse_card():
    """Проверка парса названия карты"""

    assert parse_card('8j')[0] == 8
    assert parse_card('8j')[1] == 'j'


def test_get_new_random_card_available():
    """Проверка взятия карты из колоды"""

    data = dict(cards=['1a', '1b'],
                player_data=dict(card_list=[]),
                alice_data=dict(card_list=[]))

    get_new_random_card(data, True)

    assert len(data['cards']) == 1
    assert len(data['player_data']['card_list']) == 1
    assert len(data['alice_data']['card_list']) == 0

    get_new_random_card(data, False)

    assert len(data['cards']) == 0
    assert len(data['player_data']['card_list']) == 1
    assert len(data['alice_data']['card_list']) == 1


def test_get_new_random_card_bad():
    """Проверка взятия карты из колоды (в колоде карт нет)"""

    data = dict(cards=[],
                player_data=dict(card_list=[]),
                alice_data=dict(card_list=[]))

    assert get_new_random_card(data, True) is False
