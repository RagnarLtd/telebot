def send_result(value: list, days: int) -> str:
    """
    Функция обработки текста для вывода юзеру
    """
    if value[0] == 0:
        price = 'Нет информации'
        total_price = 'Нет информации'
    else:
        price = value[0] + 'руб.'
        total_price = str(int(value[0]) * days) + 'руб.'
    send_text = (f'*Наименование отеля*: [{value[1]}]({value[4]})'
                 f'\n*Адрес отеля*: _{value[2]}_'
                 f'\n*Стоимость за ночь*: _{price}_'
                 f'\n*Стоимость за выбранный период*: _{total_price}_'
                 f'\n*Расстояние от центра города*: _{value[3]}_ км')
    return send_text