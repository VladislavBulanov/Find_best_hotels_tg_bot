# Telegram-бот для поиска отелей

Данный Telegram-бот создан для помощи в подборе подходящих отелей на сайте Expedia.com. Пользователь вводит необходимые данные (город, дата заселения и т.д.) и получает в ответ краткую информацию о подходящих отелях с соответствующими ссылками на сайт:

![The example of result](img/results.png)

### Команды

![The user interface](img/ui.png)  

1. `/start`: запустить бота
2. `/help`: вывести справку с описанием функционала доступных команд
3. `/low`: показать самые дешёвые отели
4. `/high`: показать самые релевантные отели
5. `/custom`: показать отели в выбранном диапазоне цен
6. `/history`: вывести историю запросов пользователя

## Инструкция по установке

Приложение написано на языке Python с использованием API Telegram PyTelegramBot и API сайта Expedia.com, расположенным на ресурсе Rapidapi.com:  
https://rapidapi.com/apidojo/api/hotels4/  

Для установки необходимо:

1. Клонировать данный репозиторий.

2. В виртуальном окружении установить необходимые пакеты и библиотеки, описанные в файле requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```

3. В рабочей директории создать файл `.env` и прописать в нём токен Вашего Telegram-бота, а также ключ, соответствующий Вашей учётной записи и выбранному API на ресурсе Rapidapi.com:  

![The .enf file example](img/env_file_desc.png)  

4. Запустить главный скрипт `main.py`.  

###
#### Telegram-бот готов к использованию!