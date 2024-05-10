class directReport:
	def __init__(self, direction, date, time):
		self.direction = direction
		self.date = date
		self.time = time
	
	def display(self):
		print(f"Направление: {self.direction}\nДата: {self.date}\nВремя отправления: {self.time}")


