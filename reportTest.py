import os, fnmatch

def getReportData():
	while(True):
		reportDataFile = "/home/valentin/python_dev/report/reportTest/" + input("Название файла отчёта(.txt): ")
		try:
			with open(reportDataFile, encoding = "utf8") as file:
				data = file.readlines()
				return data
		except FileNotFoundError:
			answer = input("Ошибка. Попробовать ещё раз (y/n)? ")
			if answer == "n" or answer == "н":
				return "finish"
	
'''
	Получаем список файлов в текущем директории.
Выбираем файлы с расширением *.txt.
'''
listOfFiles = os.listdir(".")
pattern = "*.txt"
for entry in listOfFiles:
	if fnmatch.fnmatch(entry, pattern):
		print(entry)
reportData = getReportData()
print(reportData)
