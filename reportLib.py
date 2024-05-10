def convertDate(date):
	month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
	subDate = date.split("-")
	return subDate[2] + " " + month[int(subDate[1]) - 1] + " " + subDate[0]
	
	
def newDirReport(string):
	string = string[16:len(string)-5]
	words = string.split(", ")
	return directReport(words[2], convertDate(words[0]), words[1])


def sringIsHeader(string):
	if "Пинск" in string:
		return True
	else: return False

	
def isGetString(string):
	words = ["Пинск", "свободно", "д.к.", "дк", "Дк", "Д.К.", "безнал", "б/н", "17р", "ребенок", "width=\"25px\"", "selected=\"\">Поехал"]
	for word in words:
		if word in string: return True
	return False

