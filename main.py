
#ATM Simulator
import time

print("Insert Your Card\n")
time.sleep(2)
print("********** ATM CARD IS PROCESSING ***********\n Please Wait.......\n")
time.sleep(3)  #ATM card is in process

cus_name="Dolly Salvi"
bal_amount=500000
pin=1010


#User Enters ATM Pin
cus_pin=int(input("Enter 4 digit PIN\n"))


if(cus_pin==pin):
    cus_name= cus_name.upper()
    print("Welcome Ms. ",cus_name)
    time.sleep(2)

 # Operation List
    option=int(input("""Select operations to perform\n 1. Deposit\n2. Withdrawal\n.3. Change Pin \n 4. Balance Amount\n"""))

    # Deposit the amount
    if(option==1):
        dep_amount=int(input("Enter Deposit Amount\n"))
        bal_amount=bal_amount+dep_amount
        print("Amount is Successfully Deposited!!\n")
        print("Available Balance",bal_amount)
#withdraw  the Amount
    elif(option==2):
        with_amount=int(input("Enter Amount to Withdraw\n"))
        bal_amount=bal_amount-with_amount
        print("Please collect your cash!!\n")
        print("Available Balance",bal_amount)
   #Change of old pin 

    elif(option==3):
        oldpin=int(input('Enter Existing PIN'))
        if(oldpin==pin):
         newpin=int(input("Create 4 digit New PIN"))
         pin=newpin
         print("New PIN has successfully Changed")
        else:
           print("Existing PIN does not match")
    # Total Balance       
    elif(option==4):
       print("Current Balance",bal_amount)

    else:
          print("Invalid Choice Selection")

else:
    print("You have Entered Wrong PIN")

#please RE-RUN the programm if it shows int()literal error.