import sys
from user.authentication import authenticate_user
from transactions.journal import receive_income
from transactions.journal import pay_expense
import banking



if __name__ == '__main__':
    amount = '100'
    if len(sys.argv) > 0:
        for i in range (len(sys.argv) - 1):
            print(sys.argv[i + 1])
    authenticate_user()
    receive_income(amount)
    pay_expense(amount)
    banking.fvb.reconciliation.do_reconciliation()