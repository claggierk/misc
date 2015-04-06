import math
import datetime
import sys

MONTHS_IN_YEAR = 12

def output_amortization(payments):
	with open("amortization.html", 'w') as outfile:
		outfile.write("<html>\n")
		outfile.write("  <body>\n")
		for year_key in sorted(payments.keys()):
			outfile.write("    <table border=\"4\">\n")
			for month_key in sorted(payments[year_key].keys()):
				outfile.write("      <tr>\n")
				outfile.write("        <td>" + str(payments[year_key][month_key]["loan_year"]) + "</td>\n")
				outfile.write("        <td>" + str(payments[year_key][month_key]["loan_month"]) + "</td>\n")
				outfile.write("        <td>" + str(payments[year_key][month_key]["calendar_year"]) + "</td>\n")
				outfile.write("        <td>" + str(payments[year_key][month_key]["calendar_month"]) + "</td>\n")
				outfile.write("        <td>" + str(payments[year_key][month_key]["balance"]) + "</td>\n")
				outfile.write("        <td>" + str(payments[year_key][month_key]["paid_principal"]) + "</td>\n")
				outfile.write("        <td>" + str(payments[year_key][month_key]["paid_interest"]) + "</td>\n")
				outfile.write("      </tr>\n\n")
			outfile.write("    </table><br>\n")
		outfile.write("  </body>\n")
		outfile.write("</html>\n")

def create_month(loan_year, loan_month, calendar_year, calendar_month, balance, paid_principal, paid_interest):
	return {
		"loan_year": loan_year,
		"loan_month": loan_month,
		"calendar_year": calendar_year,
		"calendar_month": calendar_month,
		"balance": balance,
		"paid_principal": paid_principal,
		"paid_interest": paid_interest
	}

def build_payments(amount_owed, interest_rate, loan_length, extra=0.0):
	months_length = loan_length * MONTHS_IN_YEAR
	monthly_interest_rate = interest_rate / 100.0 / MONTHS_IN_YEAR

	#       L[c(1 + c)^n]
	# P = -----------------
	#      [(1 + c)^n - 1]
	# P = fixed monthly payment
	# L = loan amount
	# n = loan length (in months)
	# c = monthly interest rate

	numerator = amount_owed * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, months_length))
	denominator = math.pow(1 + monthly_interest_rate, months_length) - 1
	monthly_payment = numerator / denominator

	print "Loan amount         :", amount_owed
	print "Interest Rate       :", interest_rate
	print "Years to pay off    :", loan_length
	print "Monthly payment     :", monthly_payment
	print "Paying extra        :", extra
	print "Real monthly payment:", monthly_payment + extra

	balance = amount_owed
	total_interest_paid = 0.0
	total_principal_paid = 0.0
	months_paid = 0

	current_date = datetime.date.today()
	current_year = current_date.year
	current_month = current_date.month

	all_payments = {
		current_year: {}
	}
	for year in range(loan_length):
		for month in range(MONTHS_IN_YEAR):
			months_paid += 1
			paid_interest = balance * monthly_interest_rate
			paid_principal = monthly_payment - paid_interest + extra

			# check this month's payment will exceed the loan amount
			if balance - paid_principal < 0:
				paid_principal = balance

			balance -= paid_principal

			all_payments[current_year][current_month] = create_month(year+1, month+1, current_year, current_month, balance, paid_principal, paid_interest)
			##### print all_payments[current_year][current_month]

			# update the month and the year
			if current_month + 1 == 13:
				current_month = 1
				current_year += 1
				all_payments[current_year] = {}
			else:
				current_month += 1

			# update totals
			total_interest_paid += paid_interest
			total_principal_paid += paid_principal

			# check if next month's payment will exceed the balance
			if balance == 0:
				break
		# if the loan is paid off, break
		if balance == 0:
			break

	print "Total principal paid:", total_principal_paid
	print "Total interest paid :", total_interest_paid
	print "Required months     : %d (%d years %d months)" % (months_paid, months_paid/MONTHS_IN_YEAR, months_paid - (months_paid/MONTHS_IN_YEAR * MONTHS_IN_YEAR))
	print ""
	return all_payments

def Usage():
	print "**************************************************"
	print "Usage  : python %s [loan amount] [interest rate] [loan length (years)] [extra to principal]" % sys.argv[0]
	print "Example: python %s 123243.24 3.625 10 100" % sys.argv[0]
	print "**************************************************"

def main():
	if len(sys.argv) != 5:
		Usage()
		return

	amount_owed = float(sys.argv[1])
	interest_rate = float(sys.argv[2])
	loan_length = int(sys.argv[3])
	extra = float(sys.argv[4])

	'''
	amount_owed = 100000.00
	interest_rate = 5.0
	ten_years = 10
	fifteen_years = 15
	thirty_years = 30
	zero = 0.00
	extra = 253.97
	'''

	payments = build_payments(amount_owed, interest_rate, loan_length, extra)
	output_amortization(payments)

if __name__ == "__main__":
    main()
