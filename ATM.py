import logging
import pandas as pd
import random
import csv
class ATM:
    def __init__(self,acc_num,passwrd):
        self.acc_num=acc_num
        self.passwrd=passwrd
    def login(self):
        f=open('DVM.csv','r')
        a=csv.reader(f)
        acc_found =False
        global index,name
        index=-1
        for i in a:
            if i[1] == str(self.acc_num) :
                acc_found=True
                if i[2] == str(self.passwrd):
                    name=i[0]
                    print('login successfull ! ')
                    print('Welcome',format(name))
                    global balance
                    balance = int(i[3])

                    return True
                    break
                elif i[1] != str(self.passwrd):
                    print('WRONG PASSWORD')
            else:
                index = index + 1
        if acc_found == False:
            print('ACCOUNT NUMBER ENTERED WAS NOT FOUND ! ')
        f.close()

    def create_acc(self):
        name=input('enter your name')
        f=open('DVM.csv','a')
        w=csv.writer(f)
        #name
        w.writerow([name,str(self.acc_num),str(self.passwrd),0])
        print("ACCOUNT CREATED SUCCESSFULLY")
        f.close()
    def deposit(self,ammount):
        df = pd.read_csv("DVM.csv")
        resultant= balance +ammount
        df.loc[index, 'AMOUNT'] = resultant
        df.to_csv("DVM.csv", index=False)
        print('AMMOUNT SUCCESSFULLY DEPOSITED !')
        print('Now You Have {} RUPEES IN YOUR ACCOUNT '.format(resultant))
        f_name='TransactionHis_user-{}.log'.format(self.acc_num)
        logging.basicConfig(filename=f_name, level=logging.DEBUG,format='%(asctime)s:%(message)s')
        logging.debug('AMOUNT {} DEPOSITED'.format(ammount))
    def withdrawl(self,ammount):
        df = pd.read_csv("DVM.csv")
        resultant = balance - ammount
        if resultant > 0:
            df.loc[index, 'AMOUNT'] = resultant
            df.to_csv("DVM.csv", index=False)
            print('WITHDRAWL SUCCESSFULLY !')
            print('Now You Have {} RUPEES IN YOUR ACCOUNT '.format(resultant))
            f_name = 'TransactionHis_user-{}.log'.format(self.acc_num)
            logging.basicConfig(filename=f_name, level=logging.DEBUG,format='%(asctime)s:%(message)s')
            logging.debug('AMOUNT {} WITHDRAWALED'.format(ammount))
        else:
            print('INSUFFICIENT BALANCE !')
            print('YOU ONLY HAVE {} RUPEES IN YOUR ACCOUNT'.format(balance))
    def view_balance(self):
        return print('YOU HAVE {} RUPEES IN YOUR ACCOUNT'.format(balance))


class user(ATM):
    def __init__(self,name,acc_num,passwrd):
        super().__init__()
        self.name=name
        self.acc_num = acc_num
        self.passwrd = passwrd
    def name(self):
        return self.name





print('WELCOME')
print()
print('IF YOU ALREADY HAVE AN ACCOUNT PRESS 1')
print()
print('IF YOU WANT TO CREATE AN ACCOUNT PRESS 2')
n=int(input("1 or 2"))
if n == 2:
    account_num=int(input('enter your desired account number'))
    passwrd=int(input('enter the password'))
    a=ATM(account_num,passwrd)
    a.create_acc()
if n==1:
    account_num=int(input('ENTER YOUR ACCOUNT NUMBER'))
    passwrd=int(input('ENTER YOUR PASSWORD'))
    a=ATM(account_num,passwrd)
    log=a.login()
    if log == True:
        print('whatcha wanna do?')
        print('1-DEPOSIT')
        print('2-WITHDRAWL')
        print('3-VIEW BALANCE')
        c=int(input('1or2or3'))
        if c==1:
            ammount = int(input('enter the ammount you wanna deposit'))
            a.deposit(ammount)
        if c == 2:
            ammount=int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAWL !"))
            a.withdrawl(ammount)
        if c == 3:
            a.view_balance()



