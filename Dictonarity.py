phone_book = {'Oleg':+79105406720, 'Tanya':+79533273575}
print(phone_book['Oleg'])
phone_book.update({"Ira": 1235,
                   'Sergey': 33355})
print(phone_book)
print(phone_book.get('ins' ,'Нет такого абонента'))
#phone_book.pop('Ira')
print(phone_book)
print(phone_book.keys())