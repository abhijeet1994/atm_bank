import customer_class 
import pandas as pd
import atm_actions
import sys


class Bank_side():
    def __init__(self):
        data_file = "client_data.csv"
        self.pd1 = pd.read_csv(data_file)
        pd2 = self.pd1.values.tolist()
        self.current_client = None
        self.client = {}
        for row in pd2:
            card_no = row[1]
            obj = customer_class.Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            self.client[card_no] = obj
        print("Data_loaded")
    
    def check_user_exists(self, card_no):
        if card_no in self.client.keys():
            self.current_client = card_no
            return (True, self.client[self.current_client].is_card_blocked)
        else: 
            return(False, False)

    def check_pin(self, pin):
        if self.client[card_number].validate_pin(pin):
            return (True, self.current_client)
        return (False, None)

    def check_card_block(self):
        return self.client[self.current_client].is_card_blocked
    
    def close(self):
        self.update_database()
        self.pd1.to_csv('client_data.csv', index = False)
        print("System Updated. Thank you for visiting")
        self.current_client = None


    def update_database(self):
        usr = self.client[self.current_client]
        row = [usr.s_bal, usr.c_bal, usr.is_card_blocked]
        cols = ['s_bal', 'c_bal', 'is_card_blocked']
        self.pd1.loc[self.pd1['card_no'] == self.current_client, cols] = row
        #print(self.pd1.head())


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
       
    bank = Bank_side()
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
    