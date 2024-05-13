import os, fnmatch
from reportClass import *
from reportLib import *
	
report = Report()
	
def getReportData():
	while(True):
		reportDataFile = "/home/valentin/python_dev/report/reportTest/" + input("Название файла отчёта(.txt): ") + ".txt"
		try:
			with open(reportDataFile, encoding = "utf8") as file:
				data = file.readlines()
				reportData = []
				for string in data:
					if isGetString(string):
						string = string.strip()
						string = string[:len(string)-5]
						reportData.append(string)
				return reportData
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
if reportData == "finish":
	print("Работа программы закончена.")	
else:
	#	Составление отчёта.
	report = []
	for string in reportData:
		#	Определение содержания строки
		if sringIsHeader(string):
		#	Заголовочная строка.
			dirReport = newDirReport(string)
			report.append(dirReport)
		elif stringIsSubHeader(string):
		#	Вторая часть заголовка.
			dirReport.setSubHeader(string)
		elif stringIsRecervedCount(string):
		#	Количество заказаных мест.
			passenger = Passenger()
			passenger.recerved = getRecervCntValFromStr(string)
		elif stringIsFulfilledStatus(string):
		#	Статус заказа.
			passenger.fulfilled = getFulfilledStatus(string)
		elif stringIsRemark(string):
		#	Пояснения к заказу.
			passenger.remark = getRemarkFromString(string)
			dirReport.passengers.append(passenger)
			
			#print(f"Заказано мест: {passenger.recerved}\nПояснения: {passenger.remark}")

for report_ in report:
	report_.display()
