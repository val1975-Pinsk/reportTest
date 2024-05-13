class Passenger:
	def __init__(self):
		self.recerved = 0
		self.fulfilled = False
		self.remark = "undefined"
	
	def display(self):
		print(f"recerved: {self.recerved}\nfulfilled: {self.fulfilled}\nremark: {self.remark}")
	
	
	def getPayment(self):
		discountedWords = ["дк", "Д.К.", "Д к ", "Дк"]
		response = {
			"discounted":0,
			"fullyPrice":0,
			"halfTheCost":0
			}
		if not self.fulfilled: return response
		for unit in discountedWords:
			if unit in self.remark:
				response["discounted"] += 1
		response["fullyPrice"] += 1
		return response
	
	
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
		self.fullyPrice = Payment("fullyPrice", 35)
		self.discounted = Payment("discounted", 30)
		self.halfTheCost = Payment("halfTheCost", 17)
	
	def display(self):
		print("\n")
		print(f"Направление:{self.direction}\nДата: {self.date}\nВремя отправления: {self.time}")
		print(f"Занято мест: {self.occupied}\nСвободных мест: {self.freely}\nАвтомобиль: {self.auto}")
		print("\n")
		for unit in self.passengers:
			unit.display()
			pay = unit.getPayment()
			print("fullyPrice: ",pay["fullyPrice"])
			self.fullyPrice.addCount(pay["fullyPrice"])
			'''
			self.discounted.addCount(pay["discounted"])
			self.halfTheCost.addCount(pay["halfTheCost"])'''
		self.fullyPrice.display()
		self.discounted.display()
		self.halfTheCost.display()
		print("===============================================")

	def setSubHeader(self, string):
		string = string[16:len(string)-5]
		words = string.split(", ")
		self.occupied = int(words[0][:len(words[0])-2])
		self.freely = int(words[1][:len(words[0])-12])
		self.auto = words[2]
	
		
class Payment:
	def __init__(self, name, value):
		self.name = name
		self.value = value
		self.count = 0
		
	def addCount(self, value):
		self.count =+ value

	def display(self):
		print(f"{self.name}: {self.count}")
