# let's build a program that tells you how much you pay for a loan for an entire time.
import math




class Loans:

    def __init__(self, loan, pays, rate):
        self.loan_amount = loan
        self.monthly_payment = pays
        self.loan_interest = rate
        self.interest_rate = rate / 100

    def pay_loan_amount(self):
        total_cal = []
        monthly_pays = 0
        last_pay = 0
        remaining = 0
        total_interest = 0
        months = 0
        while True:
            desc_pay = self.monthly_payment - (self.loan_amount * self.interest_rate)
            discount_loan = self.loan_amount - desc_pay
            self.loan_amount = discount_loan                        #This will get the remaining of the loan each time.
            monthly_pays = self.monthly_payment + monthly_pays
            interest_pay = (self.loan_amount * self.interest_rate)
            total_interest += interest_pay
            desc_int = self.monthly_payment - desc_pay
            months = months + 1
            total_cal.append([
                {"month":math.ceil(months),
                 "monthly_pay":math.ceil(self.monthly_payment),
                 "des_pay": math.ceil(desc_pay),
                 "des_int": math.ceil(desc_int),
                 "loan_amount": math.ceil(self.loan_amount)}
                            ])
            if self.loan_amount < 0: break

        return total_cal

#loan1 = Loans(150000, 39800, 10)
#print(loan1.pay_loan_amount())

#In this program we will call culculate the quote for a bank loan.

class Bank():
    def __init__(self, loan, rate, months):
        self.loan_amount = loan
        self.months = months
        self.loan_interest = rate
        self.interest_rate = rate / 100

    def bank_loan(self):

        interest_rat = self.interest_rate / 12
        rate_int = interest_rat * (1 + interest_rat)**self.months
        rate_down = (1 + interest_rat)**self.months - 1
        month_pay = self.loan_amount  * rate_int / rate_down

        total = []
        months_count = 0
        while True:
            dec_pay = month_pay - (self.loan_amount  * interest_rat)
            desc_amount = self.loan_amount - dec_pay
            self.loan_amount = desc_amount
            desc_pay = interest_rat * self.loan_amount
            pay_month = month_pay- desc_pay
            months_count +=  1

            total.append([
                {"month":math.ceil(months_count),
                 "month_pay":math.ceil(month_pay),
                 "pay_month": math.ceil(pay_month),
                 "des_pay": math.ceil(desc_pay),
                 "loan_amount": math.ceil(self.loan_amount)}
                ])

            if self.loan_amount  <= 0: break
        return total

result = Bank(3000000,5, 48)
print(result.bank_loan())















