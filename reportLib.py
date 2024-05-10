def convertDate(date):
	month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
	subDate = date.split("-")
	return subDate[2] + " " + month[int(subDate[1]) - 1] + " " + subDate[0]
	
	
def newDirReport(string):
	string = string[16:len(string)-5]
	words = string.split(", ")
	return directReport(words[2], convertDate(words[0]), words[1])
