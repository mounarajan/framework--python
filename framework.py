from semantics3 import Products

class Base(object):
    #Defining api key in constructor
    def __init__(self):
        self.products = Products(
            api_key = "xx",
            api_secret = "xx"
            )
    #Getting product results from constructor
    def get_result_example(self):
        self.products.products_field( "search", "Samsung Galaxy" )
        results = self.products.get_products()
        return results

    def user_selection(self):
        print("1. Try Sample result for api")
        print("2. Get results in a csv file")
        print("3. Get results in a file(JSON Pretty)")
        print("4. Get results in a file(Normal JSON)")
        self.usr_input = input("Enter any choice")
        #return self.usr_input

    def switch_selection(self):
        if self.usr_input == 1:
            print b.get_result_example()
        elif self.usr_input == 2:
            print b.get_result_example()
        elif self.usr_input == 3:
            print b.get_result_example()
        elif self.usr_input == 3:
            print b.get_result_example()
        else:
            print "Please enter a number from 1 to 4"



b = Base()

b.user_selection()
b.switch_selection()

#print "Results of query:\n", b.get_result_example()
