filename = input("Введите полное название файла: ")
which = input("Строки с каким паттерном подвергнуть изменениям?: ")
delete = input("Что удалить?: ")

with open(filename, "r", encoding="utf-8") as f:
    s = [e.replace(delete, "") if which in e else e for i, e in enumerate(f.readlines())]

    with open(f"deleted-{delete}-in-{which}-strings-{filename}", "w", encoding="utf-8") as r:
        r.writelines(s)
