1. Клонируйте репозиторий на локальный компьютер:
git clone https://github.com/pavel-alt/simbirsoft.git

2. Установите все необходимые зависимости: 
python -m pip install -r requirements.txt

3. Добавьте .env файл в корень проекта. В нем должны быть указаны значения для следующих переменных окружения: API_KEY, 
   LOGIN, PASSWORD.

4. Для запуска тестов используйте команду python -m pytest или графический интерфейс PyCharm


Обратите внимание: в тест-кейсах отсутствует пункт об удалении созданных при запуске теста папок и файлов,
поэтому для успешного повторного запуска необходимо зайти в яндекс диск и вручную удалить созданные папки с файлами.
Файл "Документ для копирования.docx" удалять не следует.