class directReport:
	def __init__(self, direction, date, time):
		self.direction = direction
		self.date = date
		self.time = time
		self.fullyPrice = Payment(35)
		self.discounted = Payment(30)
		self.halfTheCost = Payment(17)
	
	def display(self):
		print(f"Направление: {self.direction}\nДата: {self.date}\nВремя отправления: {self.time}")

class Payment:
	def __init__(self, value):
		self.value = value
		self.count = 0
