class ATM:
	def	__init__(self, balance, bank_name):
		self.withdrawls_list = []
		self.balance = balance
		self.bank_name = bank_name

	def withdraw(self, request):
		print "Welcome to " + self.bank_name
		print "Current balance " + str(self.balance)

		if request > self.balance:
			print "Can't give all this money !!"

		elif request < 0:
			print "Check your request plz"

		else:
			self.withdrawls_list.append(request)

			while request <= self.balance:
				if request == 0:
					break
				if request >= 100:
					print "give 100" 
					request = request - 100
					self.balance = self.balance - 100
				elif request >= 50:
					print "give 50"
					request = request - 50
					self.balance = self.balance - 50
				elif request >= 10:
					print "give 10"
					request = request - 10
					self.balance = self.balance - 10
				elif request >= 5:
					print "give 5"
					request = request - 5
					self.balance = self.balance - 5
				else:
					print "give " + str(request)
					self.balance = self.balance - request
					request = 0

		print "============================="

	def show_withdrawals(self):
		print "_____________________________"
		print self.bank_name + " withdraws"
		for withdraw in self.withdrawls_list:
			print withdraw
#------------------------------------
balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")


atm1.withdraw(100)
atm1.withdraw(200)
atm1.withdraw(23)
atm1.withdraw(50)


atm2.withdraw(50)
atm2.withdraw(70)
atm2.withdraw(30)
atm2.withdraw(100)

atm1.show_withdrawals()
atm2.show_withdrawals()
#------------------------------------
