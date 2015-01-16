import math

MONTHS_IN_YEAR = 12

def mortgageafy(loan_amount, loan_length, interest_rate, extra):
	months_length = loan_length * MONTHS_IN_YEAR
	monthly_interest_rate = interest_rate / 100.0 / MONTHS_IN_YEAR
	
	#       L[c(1 + c)^n]
	# P = ----------------
	#      [(1 + c)^n - 1]
	# P = fixed monthly payment
	# L = loan amount
	# n = loan length (in months)
	# c = monthly interest rate

	numerator = loan_amount * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, months_length))
	denominator = math.pow(1 + monthly_interest_rate, months_length) - 1
	monthly_payment = numerator / denominator

	print "Loan amount         :", loan_amount
	print "Interest Rate       :", interest_rate
	print "Years to pay off    :", loan_length
	print "Monthly payment     :", monthly_payment
	print "Paying extra        :", extra
	print "Real monthly payment:", monthly_payment + extra

	balance = loan_amount
	total_interest_paid = 0.0
	total_principal_paid = 0.0
	months_paid = 0
	for year in range(loan_length):
		for month in range(MONTHS_IN_YEAR):
			months_paid = months_paid + 1
			paid_interest = balance * monthly_interest_rate
			paid_principal = monthly_payment - paid_interest + extra
			#print " Year %s | Month %s | Balance: %s | Principal: %s | Interest: %s" % (year+1, month+1, balance, paid_principal, paid_interest)
			total_interest_paid = total_interest_paid + paid_interest
			total_principal_paid = total_principal_paid + paid_principal
			balance = balance - paid_principal
			if balance < 10:
				print "Total principal paid:", total_principal_paid
				print "Total interest paid :", total_interest_paid
				print "Required months     :", months_paid
				print ""
				return
		#print ""

	print "Total principal paid:", total_principal_paid
	print "Total interest paid :", total_interest_paid
	print "Required months     :", months_paid
	print ""

def main():
	loan_amount = 100000.00
	thirty_years = 30
	interest_rate = 5.0
	zero = 0.00

	ten_years = 10
	fifteen_years = 15
	little_extra = 253.97

	mortgageafy(loan_amount, thirty_years, interest_rate, little_extra)
	mortgageafy(loan_amount, fifteen_years, interest_rate, zero)
	

if __name__ == "__main__":
    main()
