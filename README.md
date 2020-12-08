# atm_bank
Create an atm middleware which communicates with atm hardware and bank database

This is a simulation of an ATM.
This consists of 5 important scripts:
1. client_data.csv : This is the database and updates after each transaction. 

2. atm_actions.py : These are the actions done by the ATM. They are limited to getting user input, and processing cash. Are called by middle_ware.py

3. customer_class.py : This is the data storage object in where details of each customer are kept when database is loaded.

4. bank_side.py : This is where all the processing of transactions happens. This loads the database and only takes queries from middle_ware.py and gives data back. It does not allow middle_ware to update the data

5.middle_ware.py : This is essentially the co-ordinator between ATM and bank. It only calls the ATM to do things and Bank to do things. It is a barrier between the ATM and Bank. At no point does it get access to private data such as pin, and other sensitive data

RUN Code:
Just run:
python middel_ware.py

Once the program starts:
1. Enter card number. (refer database to find valid card number)
2. Enter pin. (Refer database for pin)
3. Enter saving / checking account
4. Enter Action (Bal, Deposit, Withdraw)
5. Enter Dep/ Withdraw amount
Program updates database and ends.

Important:
1. The CSV houses all the card number and pin codes of all account. If the "is_card_blocked" flag entry for a customer is True / 1, bank transaction will never proceed. You have to physically change it to 0 to access that card. 
2. One gets 3 tries to attempt to give the correct pin. If not, the card is blocked automatically.
3. The saving_acc and checking_acc columns in the client_data signify whether the customer holds a saving/ checking account.
4. The s_bal and c_bal state the amount in each account.
