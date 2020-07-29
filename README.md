# Cashier_App-django

This is a simple app that represents the functionality of an ATM.

## App requirements 
```
    ➔ It should display a screen that allows the user to enter the desired amount.

    ➔ This amount must be delivered using ₡2,000, ₡5,000 or ₡10,000 bills, in case the exact amount 
    is not delivered, it must indicate to the user that it fails, in addition to always delivering 
    the least amount of bills possible, prevailing the ₡10,000 bills in large quantities. 

    ➔ All customers are supposed to be able to order as much as they want without a verification 
    that the client has the funds available.

    ➔ Once the transaction is done, it should show the user a message like: "Your money is 2 bill(s) 
    of ₡2000, 1 bill(s) of ₡5000 and 2 bill(s) of ₡10,000" You can use plurals to indicate unit 
    values,for example 1 bills of ₡10,000.

    ➔ Once the transaction has finished, the system should return to the desired quantity request 
    screen.

    ➔ You should keep a log of each executed transaction.

    ➔ You must list the system logs in a separate window, protected with authentication.
```

#### Note: There are some numbers that can cause problems like 11, 16, 21, 27, 29 thousand, these should be considered, but number like 3,000 should be dealt with in the error messages.
    

## Important:

#### - To run the server you should to use the following command : 
#### ( Remember that you should run this command in the directory where is the manage.py file )
```
python manage.py runserver
```

