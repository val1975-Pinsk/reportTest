import os, fnmatch
from reportClass import *

def isGetString(string):
	words = ["Пинск", "свободно", "д.к.", "дк", "Дк", "Д.К.", "безнал", "б/н", "17р", "ребенок", "width=\"25px\"", "selected=\"\">Поехал"]
	for word in words:
		if word in string: return True
	return False
	
	
def getReportData():
	while(True):
		reportDataFile = "/home/valentin/python_dev/report/reportTest/" + input("Название файла отчёта(.txt): ") + ".txt"
		try:
			with open(reportDataFile, encoding = "utf8") as file:
				data = file.readlines()
				reportData = []
				for string in data:
					if isGetString(string):
						reportData.append(string.strip())
				return reportData
		except FileNotFoundError:
			answer = input("Ошибка. Попробовать ещё раз (y/n)? ")
			if answer == "n" or answer == "н":
				return "finish"


def sringIsHeader(string):
	if "Пинск" in string:
		return True
	else: return False

	
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
if reportData == "finish":
	print("Работа программы закончена.")
else:
	#	Составление отчёта.
	report = []
	for string in reportData:
		if sringIsHeader(string):
			dirReport = newDirReport(string)
			dirReport.display()
