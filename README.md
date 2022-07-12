# editor_scripts

Free scripts for edTech editors

# Python Scripts

## change-ext
Меняет расширение файлов в папке на новое.

**Use case:**
1. Указать расширения файлов через пробел (одно или несколько), которые нужно изменить.
2. Указать новое желаемое расширение.


## change-ext2
Тоже самое, что и *change-ext*, но с поддержкой вложенных директорий.


## change-names
Меняет имена одинаково названных файлов на название папки, в которой те находятся. Поддерживает вложенные папки.

**Use case:**
1. Указать название файла, например `readme.md`
2. Скрипт переименует все файлы с этим названием.


## pattern-deleter
Создает новый файл без вхождения указанного паттерна, затрагивая только те строки, которые вы выбрали.

**Use case:**
1. Указать название файла, например `readme.md`
2. Указать паттерн для поиска строк, например "heading" или "#"
3. Указать паттерн для удаления, например слово "hello" или символ "%"
4. Скрипт создаст новый файл, но уже без вхождений паттерна.


## find-strings
Ищет строки в файлах по слову, фразе или символу/ам и сохраняет их в файл `.txt`


## find-strings2
Тоже самое, что и find-strings, но с поддержкой вложенных директорий.


## editlib
Без функционала. Вспомогательная библиотека для скриптов.


# Bash Scripts


## push_all

Добавляет, коммитит и пушит все изменения и новые файлы.

## push_changes_only

Добавляет, коммитит и пушит ТОЛЬКО изменения, без новых файлов.

## pull_push_all

Забирает с ремоута и сразу добавляет, коммитит и пушит. Применяется после принятого пулл-реквеста.

## branch_push

Добавляет, коммитит и пушит в новую, только что созданную, ветку. Можно идти и делать пулл реквест.
