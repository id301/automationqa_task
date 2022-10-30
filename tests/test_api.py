__author__ = 'id301'


def test_api(setup_task2):
    """Отправка запроса'GET https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name'
    Проверка:
    1. Все поля "name" в ответе на запрос содержат значение "Alcatel"
    2. Все элементы в ответе отсортированы по полю 'name' в алфавитном порядке"""
    products = setup_task2.get_products(search='Alcatel', sort_field='name')
    for product in products:
        assert product.name.count('Alcatel') > 0, f'Поле name не содержит значение "Alcatel" в элементе: {product}'
    names = [x.name for x in products]
    assert names == sorted(names), 'Элементы в ответе не отсортированы по полю name в алфавитном порядке'