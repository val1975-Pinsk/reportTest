import os, fnmatch
'''
	Получаем список файлов в текущем директории.
Выбираем файлы с расширением *.txt.
'''
listOfFiles = os.listdir(".")
pattern = "*.txt"
for entry in listOfFiles:
	if fnmatch.fnmatch(entry, pattern):
		print(entry)
reportData = getReportData(input("Название файла отчёта(.txt): "))

