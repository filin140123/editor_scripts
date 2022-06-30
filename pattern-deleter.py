filename = input("Введите полное название файла: ")
which = input("Строки с каким паттерном подвергнуть изменениям?: ")
delete = input("Что удалить?: ")

s = []

with open(filename, "r", encoding="utf-8") as f:
	for i in f.readlines():
		s.append(i)

for i, e in enumerate(s):
	if which in e:
		s[i] = e.replace(delete, "")

with open("deleted-" + delete + filename, "w", encoding="utf-8") as r:
	r.writelines(s)
