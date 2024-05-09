class directReport:
	def __init__(self, direction, date, time):
		self.direction = direction
		self.date = date
		self.time = time
	
	def display(self):
		print(f"Направление: {self.direction}\nДата: {self.date}\nВремя отправления: {self.time}")


def convertDate(date):
	month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
	subDate = date.split("-")
	return subDate[2] + " " + month[int(subDate[1]) - 1] + " " + subDate[0]
	
	
def newDirReport(string):
	string = string[16:len(string)-5]
	words = string.split(", ")
	return directReport(words[2], convertDate(words[0]), words[1])
