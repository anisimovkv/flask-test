
### Создание базы данных:
```bash
"C:\Program Files\PostgreSQL\10\bin\psql.exe" -h localhost -U postgres -d flask-test -p 5432 -a -q -f ./create.sql
```
> ###Примечание:
> Флаг -d указывает имя базы, где будет созданы таблицы, `flask-test` - это имя используется и вприложении в файле `config.py`
> При использовании другой базы и необходимо внести изменения, в строке запуска `psql` и `config.py`


### Импорт данных из файла csv:
```bash
"C:\Program Files\PostgreSQL\10\bin\psql.exe" -h localhost -U postgres -d flask-test -p 5432 -a -q -f ./import.sql
```
> ###Примечание:
> В файле imoprt.sql указаны место положение файлов, например `C:/Users/admin/Downloads/Reviews.csv`, 
> необходимо внести изменения, указав нужный путь к фалам csv, если путь не совпадает.


### Установка зависимостей:
```bash
pip install -r requiremnts.txt
```

### Запуск приложения:
```bash
python app.py
```

### Примеры работы:
1. Получения всех товаров.
```bash
curl -X GET http://127.0.0.1:5000/products/
```

или в браузере:
http://127.0.0.1:5000/products/


2. Получение отзывов по id B0756CYWWD c пагинацией.

```bash
curl -X GET http://127.0.0.1:5000/product/B0756CYWWD/review
```

или в браузере: 
http://127.0.0.1:5000/product/B0756CYWWD/review

3. Добавление отзыва для товара B0756CYWWD.
```bash
curl -X PUT http://127.0.0.1:5000/product/B0756CYWWD/add_review/ -H "Content-Type: application/json" -d "{\"title\":\"blabla\", \"review\":\"bla bla 2\"}"
```
