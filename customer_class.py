class Customer:
    def __init__(self, name, card_no, account_number, pin, saving_acc=False, checking_acc= True, s_bal = 0,  c_bal = 0, is_card_blocked= False):
        self.name = name                        #Person Name : First + Last
        self.card_no = card_no                  #Card No of Debit card
        self.account_number = account_number    #Account number (Same as card for now)
        self.pin = pin                          #4 digit Pin
        self.saving_acc = saving_acc            # Bool: Does Saving Acc exist
        self.checking_acc = checking_acc        # Bool: Does Checking Acc Exist. Default True
        self.s_bal = s_bal                      # Saving Acc Balance
        self.c_bal = c_bal                      # Checking Acc Bal
        self.access_granted = False             # Has Person got Access 
        self.max_tries = 3                      # Max Number of tries to Access
        self.tries = 0                          # Counter for Invalid Attempts
        self.is_card_blocked = is_card_blocked  # Bool: Card is blocked. Contact Bank
        self.working_account = "NA"             # Working account chosen by customer


    def check_card_blocked(self):
        return self.is_card_blocked
    
    def get_name(self):
        return self.name
    
    def validate_pin(self, pin):
        if not self.is_card_blocked:
            if pin == self.pin:
                self.tries = 0
                self.access_granted = True
                return(True, self.is_card_blocked)
            else:
                self.tries += 1
                if self.tries >= self.max_tries:
                    self.is_card_blocked = 1
                    self.tries = 0 
        return (False, self.is_card_blocked)

    def check_accounts(self):
        data = [0,0]
        if not self.access_granted:
            print(self.access_granted)
            return ([10,10])
        if self.saving_acc:
            data[0] = 1
        if self.checking_acc:
            data[1] = 1
        return data
    
    def select_working_account(self, account_type = "NA"):
        if account_type == "savings":
            if self.saving_acc:
                self.working_account = "s"
                
        if account_type == "checking":
            if self.checking_acc:
                self.working_account = "c"
                

    def get_balance(self):
        if not self.access_granted:
            return ("Error")
        if self.working_account == "s":
            return (self.s_bal)
        if self.working_account == "c":
            return (self.c_bal)
        return ("Error")

    def deposit_money(self, amt = 0):
        if not self.access_granted:
            return (False)
        if self.working_account == "c":
            self.c_bal = self.c_bal + amt
            print ("Transaction_Success \t Checking Bal = " +  str(self.c_bal))
            return(True)
        if self.working_account == "s":
            self.s_bal = self.s_bal + amt
            print ("Transaction_Success \t Saving Bal : " + str(self.s_bal))
            return(True)
        return (False)
    
    def withdraw_amt(self, amt = 0):
        if not self.access_granted:
            return(False)
        if self.working_account == "c":
            if amt <= self.c_bal:
                self.c_bal = self.c_bal - amt
                print("Withdrawal_Success" + "\t Checking Bal :" + str(self.c_bal))
                return (True)
            print("Not enough Balance")
            return (False)
        
        if self.working_account == "s":
            if amt <= self.s_bal:
                self.s_bal = self.s_bal - amt
                print("Withdrawal_Success" + "\t Saving Bal :" + str(self.s_bal))
                return (True)
            print("Not enough Balance")
            return (False)
        return (False)

    def close_transaction(self):
        self.access_granted = False
        self.working_account = "NA"
        return("Done")

