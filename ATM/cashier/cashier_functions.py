
class Cashier:

    def __init__(self):
        self.valid_values = [2000, 5000, 10000]

  # This solution is not the best way :( --> (Fix later)
    def transact(self, money):
        result = ()
        user_money = int(money)
        ten = 0
        two = 0
        five = 0
        result_message = "Transacción válida"

        # valid_values[0] => 2000
        # valid_values[1] => 5000
        # valid_values[2] => 10000

        if (user_money >= 2000):

            if ((user_money % self.valid_values[1] == 0)):
                five = user_money // self.valid_values[1]
                user_money = user_money % self.valid_values[1]

            else:
                while (user_money > 1000):

                    if (user_money % self.valid_values[0] == 0):
                        two = user_money // self.valid_values[0]
                        user_money = user_money % self.valid_values[0]
                    else:
                        user_money = user_money - self.valid_values[1]
                        five += 1

            # Compute the number of ten thousand bills, based on the number of five and two thousand bills
            if (five > 1 or two > 4):
                minus = 0
                ten_quantity = 0

                if (five > 1):
                    five,ten = self.get_bills_quantity(five,self.valid_values[1])

                if (two > 4):
                    two,ten_quantity = self.get_bills_quantity(two,self.valid_values[0])
                    ten += ten_quantity

        if(user_money != 0 ):
            result_message = "Transacción inválida"  

        result = (user_money, two, five, ten, money,result_message )

        return result
        

    def compute_10_bills(self, bills_quantity, bill_amount, ten):
        minus = 0
        for index in range(1, (bills_quantity + 1)):
            if (index * bill_amount % self.valid_values[2] == 0):
                ten += 1
                minus = index

        return minus, ten

    def get_bills_quantity(self,bills_quantity_to_analize,bill_amount_to_analize):
        ten_quantity = 0
        minus, ten_quantity = self.compute_10_bills(bills_quantity_to_analize,bill_amount_to_analize , 0)
        bills_quantity_to_analize -= minus
      
        return bills_quantity_to_analize , ten_quantity