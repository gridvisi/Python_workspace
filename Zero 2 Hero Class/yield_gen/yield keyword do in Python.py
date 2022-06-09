
def bank_account(deposited, interest_rate):
    while True:
        calculated_interest = interest_rate * deposited
        received = yield calculated_interest
        if received:
            deposited += received


print('my_account', bank_account(1000, .05))
my_account = bank_account(1000, .05)
first_year_interest = next(my_account)
print(first_year_interest)

next_year_interest = my_account.send(first_year_interest + 1000)
print(next_year_interest)


#2

def money_manager(expected_rate):
    # must receive deposited value from .send():
    under_management = yield  # yield None to start.
    while True:
        try:
            additional_investment = yield expected_rate * under_management
            if additional_investment:
                under_management += additional_investment
        except GeneratorExit:
            '''TODO: write function to send unclaimed funds to state'''
            raise
        finally:
            '''TODO: write function to mail tax info to client'''


def investment_account(deposited, manager):
    '''very simple model of an investment account that delegates to a manager'''
    # must queue up manager:
    next(manager)  # <- same as manager.send(None)
    # This is where we send the initial deposit to the manager:
    manager.send(deposited)
    try:
        yield from manager
    except GeneratorExit:
        return manager.close()  # delegate?

my_manager = money_manager(.03)
my_account = investment_account(1000, my_manager)
first_year_return = next(my_account) # -> 60.0
print(first_year_return,next(my_manager))


next_year_return = my_account.send(first_year_return + 1000)
print(next_year_return) # 123.6

third_year_return = my_account.send(next_year_return + 1000)
print(third_year_return)