Перейдите в папку /backend_test_homework: cd C:/Dev/backend_test_homework

Работа с локальным репозиторием Git. Теория
Версионный контроль в Git предполагает, что любой файл репозитория находится в одном из четырёх состояний:
Неотслеживаемый (англ. untracked).
Отслеживаемый, staged, добавленный в Staging Area (англ. «плацдарм», «временное хранилище»). 
Иначе в Git это называют «добавить в индекс».
Изменённый (англ. modified).
Боевой, на жаргоне разработчиков «закоммиченный» (англ. committed, «брошенный в бой»).
Логика работы такая: как только в репозитории появляется новый файл, он принимает состояние «неотслеживаемый». 
Что бы вы ни делали с этим файлом, Git проигнорирует любые изменения.
Чтобы Git обратил внимание на файл и стал учитывать изменения, нужно добавить файл в индекс. 
Это делается командой git add. Файл перейдёт в состояние «отслеживаемый», 
а если после этого внести в него изменения — в состояние «изменённый».

После завершения работы с файлом его нужно «сохранить» — сообщить программе Git, что актуальное состояние файла надо запомнить. 
Такое сохранение выполняется командой git commit и называется коммитом.

git status: командой git rm --cached README.md вы можете перевести файл в состояние «неотслеживаемый» (unstaged). 
Нет, сейчас мы этого делать не станем, но запомним, что это возможно.

git commit -m "My first commit" 
# добавить изменения к последнему коммиту.
git commit --amend -m "Текст вашего комментария"

# Для отправки локальных изменений на сервер GitHub, выполните команду
git push 
# вернуться к определённому коммиту
git reset и через пробел указать первые семь символов контрольной суммы нужного коммита

# Запуск виртуального окружения проекта
# выполнить инструкции из файла activate во вложенной папке venv/Scripts
...Dev/backend_test_homework$ source venv/Scripts/activate 
# Остановить работу виртуального окружения можно командой.
(venv)...$ deactivate 

# Установка pytest

# Откройте проект backend_test_homework в терминале, активируйте виртуальное окружение и введите команду:
(venv)...Dev/backend_test_homework$ pip install pytest 

#Проверка установки
#После завершения процесса проверьте, что Pytest действительно установился: запросите версию установленного пакета:
(venv)...Dev/backend_test_homework$ pytest --version 

#запустите тесты.
...Dev/backend_test_homework$ pytest 