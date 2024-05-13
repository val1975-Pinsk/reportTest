class Passenger:
	def __init__(self):
		self.recerved = 0
		self.fulfilled = False
		self.remark = "undefined"


class Report:
	def __init__(self):
		self.body = []


class directReport:
	def __init__(self, direction, date, time):
		self.direction = direction
		self.date = date
		self.time = time
		self.auto = "undefined"
		self.occupied = 0
		self.freely = 0
		self.passengers = []
		self.fullyPrice = Payment(35)
		self.discounted = Payment(30)
		self.halfTheCost = Payment(17)
	
	def display(self):
		print("\n")
		print(f"Направление:{self.direction}\nДата: {self.date}\nВремя отправления: {self.time}")
		print(f"Занято мест: {self.occupied}\nСвободных мест: {self.freely}\nАвтомобиль: {self.auto}")
		print("\n")
		for passenger in self.passengers:
			print(f"Кол-во мест: {passenger.recerved}\nСтатус: {passenger.fulfilled}\nПояснения: {passenger.remark}")
		print("===============================================")

	def setSubHeader(self, string):
		string = string[16:len(string)-5]
		words = string.split(", ")
		self.occupied = int(words[0][:len(words[0])-2])
		self.freely = int(words[1][:len(words[0])-12])
		self.auto = words[2]
		
class Payment:
	def __init__(self, value):
		self.value = value
		self.count = 0
