
from mortgage import Mortgage

def main():
   loan_amount = 122028
   num_years_left = 9
   thirty_years = 30
   interest_rate = 3.625
   zero = 0.00

   ten_years = 10
   fifteen_years = 15
   little_extra = 200.0

   #my_mortgage = Mortgage(loan_amount, interest_rate, num_years_left)
   my_mortgage = Mortgage()
   print my_mortgage
   my_mortgage.amortize()
   my_mortgage.pay_extra_amortize(200)

if __name__ == "__main__":
   main()
