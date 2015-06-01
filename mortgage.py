import math
from calendar import month_abbr

MONTHS_IN_YEAR = len(month_abbr) - 1

class Mortgage:
    def __init__(self, amount=100000, interest_rate=5.0, years=30, pmi=0, property_tax=0):
        self._amount = amount
        self._interest_rate = interest_rate
        self._years = years
        self._pmi = pmi
        self._property_tax = property_tax

    def __str__(self):
        return "Amount: %s" % self._amount

    def __repr__(self):
        return "Amount: %s" % self._amount

    def amortize(self):
        self._amortize(self)

    def pay_extra_amortize(self, extra):
        self._amortize(extra)

    def _amortize(self, extra=0.0):
        months_length = self._years * MONTHS_IN_YEAR
        monthly_interest_rate = self._interest_rate / 100.0 / float(MONTHS_IN_YEAR)

        #       L[c(1 + c)^n]
        # P = ----------------
        #      [(1 + c)^n - 1]
        # P = fixed monthly payment
        # L = loan amount
        # n = loan length (in months)
        # c = monthly interest rate

        numerator = self._amount * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, months_length))
        denominator = math.pow(1 + monthly_interest_rate, months_length) - 1
        monthly_payment = numerator / denominator

        print "Loan amount         :", self._amount
        print "Interest Rate       : %s %%" % self._interest_rate
        print "Years to pay off    :", self._years
        print "Monthly payment     :", monthly_payment
        if extra > 0:
            print "Paying extra        :", extra
            print "Real monthly payment:", monthly_payment + extra

        balance = self._amount
        total_interest_paid = 0.0
        total_principal_paid = 0.0
        months_paid = 0
        while True:
            months_paid += 1
            paid_interest = balance * monthly_interest_rate
            total_interest_paid += paid_interest

            if balance < monthly_payment:
                total_principal_paid += balance
                print "Total principal paid:", total_principal_paid
                print "Total interest paid :", total_interest_paid
                print "Required months     :", months_paid
                print "Years and months    : %s years and %s months" % (months_paid / float(MONTHS_IN_YEAR), months_paid % float(MONTHS_IN_YEAR))
                print ""
                return
            else:
                paid_principal = monthly_payment - paid_interest
                if extra > 0.0:
                    paid_principal += extra

                #print " Month %s | Balance: %s | Principal: %s | Interest: %s" % (months_paid+1, balance, paid_principal, paid_interest)
                total_principal_paid += paid_principal
                balance -= paid_principal
