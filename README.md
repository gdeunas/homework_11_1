# homework_11_1

## Описание:

Проект homework_11_1 - это приложение на Python.

1. В модуле generators есть функция filter_by_currency, которая принимает на вход 
список словарей, представляющих транзакции.
Функция должна возвращать итератор, который поочередно выдает транзакции, 
где валюта операции соответствует заданной (например, USD).

2. Генератор transaction_descriptions , который принимает список словарей 
с транзакциями и возвращает описание каждой операции по очереди.

3. Генератор card_number_generator, который выдает номера банковских карт в формате 
XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать 
номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Генератор должен принимать начальное и конечное значения для генерации 
диапазона номеров.


## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/gdeunas/homework_11_1.git
```
2. ssh:
```
git@github.com:gdeunas/homework_11_1.git
```

## Тестирование:

Тестированы функции:
* generators.filter_by_currency
```
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
* generators.transaction_descriptions
```descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
* generators.card_number_generator
```
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).