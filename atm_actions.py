class ATM():
    def __init__(self):
        print("Welcome")
        self.card_num = None
        self.actions_list = ["Get Balance", "deposit money", "withdraw money"]
        self.working_acc = "NA"
        self.atm_limit = 3000  # max Amt that can be withdrawn from the atm

    def get_card_number(self):
        self.card_num = None
        while not type(self.card_num) == int:
            self.card_num = raw_input("Enter 4 digit card_num:")
            try:
                int(self.card_num)
            except ValueError:
                self.card_num = None
            else:
                self.card_num = int(self.card_num)
                if not (self.card_num > 999 and self.card_num < 10000):
                    self.card_num = None
        return(self.card_num)
    
    def card_blocked(self):
        print("Card is blocked. Please contact Bank")

    
    def get_atm_pin(self):
        self.pin = None
        while not type(self.pin) == int:
            self.pin = raw_input("Enter 4 digit pin:")
            try:
                int(self.pin)
            except ValueError:
                self.pin = None
            else:
                self.pin = int(self.pin)
                if not (self.pin > 999 and self.pin < 10000):
                    self.pin = None
        return(self.pin)
    
    def print_out(self, data):
        print(data)

    def get_account_selection(self, saving, checking):
        account_selected = False
        account = ""
        string = "You have"
        if saving :
            string = string + " saving"
        if checking:
            if saving:
                string = string + " &"
            string = string + " checking"
        string = string + " account available with us."
        print(string)

        while not account_selected :
            acceptable_input = []
            
            if saving:
                acceptable_input.append("s")
            if checking:
                acceptable_input.append("c")
            usr_inp = ""
            while usr_inp not in acceptable_input:
                usr_inp = raw_input("press s for saving and c for checking : ")
                if usr_inp not in acceptable_input:
                    print("We do not have that account. Please retry \n")
                    print(string)
            if usr_inp == "s":
                print("You have selected saving account")
                account = "savings"
                account_selected = True
                self.working_acc = account
                return(account)
            if usr_inp == "c":
                print("You have selected checking account")
                account = "checking"
                account_selected = True
                self.working_acc = account
                return (account)
    
    def get_action(self):
        
        got_action = False
        action = None
        while not got_action:
            action = raw_input("Press \t 0 for Balance \n\t Press 1 deposit money \n\t Press 2 for withdrawal:")
            try:
                int(action)
            except ValueError:
                action = None
            else:
                action = int(action)
                if action in [0,1,2]:
                    got_action = True
                else:
                    action = None
         
        return (action)     

    def show_bal(self, bal):
        print("Your balance in " + self.working_acc + " is " + str(bal))

    def get_money_deposit(self):
        money_recieved = False
        while not money_recieved: 
            usr_money = raw_input("Please deposit money (max 2000):")
            money_recieved = True
            try:
                int(usr_money)
            except ValueError:
                money_recieved = False
            else:
                usr_money = int(usr_money)
                if usr_money > 2000:
                    money_recieved = False
                    print("ATM is returning Money. Please deposit less than 2000")
        return usr_money 

    def return_amt(self, amt):
        print("Transaction Unsuccessful")
        print("ATM returning amt :", amt)

    def withdraw_money(self, max_amt):
        max_withdraw = min(max_amt, self.atm_limit)
        print("\n Max atm limit is " + str(self.atm_limit))
        print("Account_Bal " + str(max_amt))
        got_usr_amt = False
        usr_amt = None
        while (not got_usr_amt) or (not type(usr_amt) == int):
            usr_amt = raw_input("Enter amt less than " + str(max_withdraw) + ":")
            got_usr_amt = True
            try:
                int(usr_amt)
            except ValueError:
                got_usr_amt == False
                usr_amt = None
            else:
                usr_amt = int(usr_amt)
                if usr_amt > max_withdraw:
                    got_usr_amt = False
                    usr_amt = None
        return usr_amt 

    def dispense_amt(self, amt):
        print("ATM is dispensing amt : " + str(amt))