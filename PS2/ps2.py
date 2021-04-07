def monthy_finances(balance, annualInterestRate, monthlyPaymentRate):
    '''Return balance after one month with min payment rate made'''
    monthly_interest_rate = annualInterestRate/12.0
    min_month_payment = balance * monthlyPaymentRate
    unpaid_balance = balance - min_month_payment
    new_balance = unpaid_balance * (1 + monthly_interest_rate)
    # print('Remaining balance: {:.2f}'.format(new_balance))
    return new_balance

def monthy_finances_minval(balance, annualInterestRate, payment):
    '''Return balance after one month with min payment made'''
    monthly_interest_rate = annualInterestRate/12.0
    unpaid_balance = balance - payment
    new_balance = unpaid_balance * (1 + monthly_interest_rate)
    # print('Remaining balance: {:.2f}'.format(new_balance))
    return new_balance

def year_with_min(balance, annualInterestRate, monthly_payment_rate):
    '''Return balance after one year with min payment rate made each month'''
    for month in range(12):
        balance = monthy_finances(balance, annualInterestRate, monthlyPaymentRate)
    return balance

def year_with_minval(balance, annualInterestRate, payment):
    '''Return balance after one year with min payment made each month'''
    for month in range(12):
        balance = monthy_finances_minval(balance, annualInterestRate, payment)
    return balance


def find_fixed_payment(balance, annualInterestRate):
    '''Return minmum monthly payment to pay off in a year'''
    payment = 0
    while True:
        final_balance = year_with_minval(balance, annualInterestRate, payment)
        if final_balance < 0:
            break
        else: payment += 10
        print('final', final_balance)
    print('Lowest Payment: {}'.format(payment))
    return payment

def bisection_search(balance, annualInterestRate):
    '''return minimum payment usign bisection_search'''
    #define starting upper and lower bounds for the payments
    payment_lower = balance/12
    payment_upper = balance *(1+ annualInterestRate/12)**12/12
    payment = (payment_upper + payment_lower )/2
    #each operation will involve picing a balance in the middle of the bounds, then adjusting bounds based on result
    last_remaining = 0
    while round(payment_upper, 2) != round(payment_lower,2):
        payment = (payment_upper + payment_lower )/2
        remaining = year_with_minval(balance, annualInterestRate, payment)
        # print(f'upper: {payment_upper}, lower: {payment_lower}, remaining: {remaining}')
        if remaining > 0 :
            payment_lower = payment
        elif remaining < 0 :
            payment_upper = payment
        print(remaining)

    print('Lowest Payment: {:.2f}'.format(payment))
    return payment
