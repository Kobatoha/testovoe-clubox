import requests


# Заполнить данные по селлерам на Озон. Для этого нужен личный кабинет продавца, где будет API ключ и ID клиент
clients = {
    'name':
        {'api_key': 'api-key', 'ID_Client_OZON': 'id_client'},
    'name2':
        {'api_key': 'api-key', 'ID_Client_OZON': 'id_client'},
    'name3':
        {'api_key': 'api-key', 'ID_Client_OZON': 'id_client'},
    'nameN':
        {'api_key': 'api-key', 'ID_Client_OZON': 'id_client'},
}

def get_product_info_list():
    url = 'https://api-seller.ozon.ru/v2/product/info/list'
    headers = {
        "Client-Id": clients['name']['ID_Client_OZON'],
        "Api-Key": clients['name']['api_key'],
        "Content-Type": "application/json"
    }
    # Список SKU товаров на Озон (SKU - индефикатор товар в базе Озона)
    sku_list = []

    body = {
        "offer_id": [],
        "product_id": [],
        "sku": sku_list[:200]
    }

    r = requests.post(url, headers=headers, json=body)
    r.json()


def get_product_info():
    url = 'https://api-seller.ozon.ru/v2/product/info'
    headers = {
        "Client-Id": clients['name2']['ID_Client_OZON'],
        "Api-Key": clients['name2']['api_key'],
        "Content-Type": "application/json"
    }
    # Список SKU товаров на Озон (SKU - индефикатор товар в базе Озона)
    sku_list = []

    # Список ID товаров на Озон (product_id - индефикатор товар в недрах Озона)
    product_id_list = []

    for sku in sku_list:

        body = {
            "offer_id": '',
            "product_id": 0,
            "sku": sku
        }
        r = requests.post(url, headers=headers, json=body)

        data_json = r.json()
        product_id_list.append(data_json['result']['id'])
        print(f'product_id: {data_json['result']['id']}\n'
              f'name: {data_json['result']['name']}\n'
              f'offer_id: {data_json['result']['offer_id']}\n'
              f'Цена с учетом всех акций: {data_json['result']['marketing_price']}\n'
              f'Зачеркнутая цена: {data_json['result']['old_price']}\n'
              f'Цена для Премиум: {data_json['result']['premium_price']}\n'
              f'Минимальная цена после всех акций: {data_json['result']['min_price']}\n'
              f'Цена товара с учётом скидок: {data_json['result']['price']}\n'
              f'status: {data_json['result']['status']['state_name']}\n'
              f'sku: {data_json['result']['sku']}\n'
              f'На складе: {data_json['result']['stocks']['present']}\n'
              f'Товар выставлен на продажу: {data_json['result']['visible']}\n')

    return product_id_list


def product_list():
    url = 'https://api-seller.ozon.ru/v2/product/list'
    headers = {
        "Client-Id": clients['name3']['ID_Client_OZON'],
        "Api-Key": clients['name3']['api_key'],
        "Content-Type": "application/json"
    }
    # Список ID товаров на Озон (product_id - индефикатор товар в недрах Озона)
    product_id_list = []

    # OVERPRICED — товары с завышенной ценой.
    # CRITICALLY_OVERPRICED — товары со слишком завышенной ценой.
    # OVERPRICED_WITH_STOCK — товары в продаже со стоимостью выше, чем у конкурентов.

    body = {
        "filter": {
            "offer_id": [],
            "product_id": product_id_list,
            "visibility": "OVERPRICED_WITH_STOCK"
        },
        "last_id": "",
        "limit": 1000
    }

    r = requests.post(url, headers=headers, json=body)
    r.json()




