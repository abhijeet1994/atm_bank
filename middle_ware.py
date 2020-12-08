import bank_side
import atm_actions
import customer_class 
import pandas as pd
import atm_actions
import sys



def get_card_number(bank, atm):
    user_exists = False
    while not user_exists:
        card_no = atm.get_card_number()
        user_exists, card_blocked = bank.check_user_exists(card_no)
    

def verify_pin(bank, atm):
    flag = 0
    atm.print_out("Please enter 4 digit pin between 1000 and 9999:")
    while flag == 0 :
        pin = atm.get_atm_pin()
        accept, block = bank.client[bank.current_client].validate_pin(pin)
        if accept:
            return (True, False)
        if block:
            
            return (False, True)
        atm.print_out("please re-enter correct 4 digit pin")

def select_working_account(bank, atm):
    saving, checking = bank.client[bank.current_client].check_accounts()
    bank.client[bank.current_client].select_working_account(atm.get_account_selection(saving, checking))


def do_action(bank, atm):
    action = atm.get_action()
    if action == 0 :                #Get Balance
        bal = bank.client[bank.current_client].get_balance()
        atm.show_bal(bal)
    if action == 1 :                #Deposit _ Money
        amt = atm.get_money_deposit()
        if not bank.client[bank.current_client].deposit_money(amt):
            atm.return_amt(amt)
    if action == 2:
        max_amt = bank.client[bank.current_client].get_balance()
        amt = atm.withdraw_money(max_amt)
        if bank.client[bank.current_client].withdraw_amt(amt):
            atm.dispense_amt(amt)
        else:
            print("Transaction unsucessful")
    
    bank.close()


if __name__ == "__main__":
       
    bank = bank_side.Bank_side()
    atm = atm_actions.ATM()

    get_card_number(bank, atm)
    
    #check if card exists
    if bank.check_card_block():
        atm.card_blocked()
        bank.close()
        sys.exit()
    
    #Check atm pin
    access,blocked = verify_pin(bank, atm)
    if blocked :
        print ("Card Blocked. Please contact bank")
        bank.close()
        sys.exit()
    
    #Get_account_types:
    select_working_account(bank, atm)

    #Get Action Associated (Get Balance, Withdraw, Deposit)
    do_action(bank, atm)
    