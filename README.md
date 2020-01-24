#### [Создать токен](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
Скопировать токен в `token.txt`, файл должен находиться в одной директории с исполняемым скриптом

#### Запустить:
* Открыть cmd/powershell/terminal
* `cd ~/Путь до директории с файлом`
* `python3 ./fork-parser.py`

* Ввести URL форков интересующего репозитория, например: `https://github.com/kmike/pymorphy2/network/members`
* Ввести название CSV-файла, файл будет сохранен в директории с программой

Для работы скрипта нужен [Python3](https://www.python.org/), [модуль Requests](https://2.python-requests.org/en/master/)
