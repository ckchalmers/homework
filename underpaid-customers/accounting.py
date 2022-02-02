def underpaid():
    melon_cost = 1.00

    #open the accounting.py file and parse each line
    the_file = open("customer-orders.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        customer_name = words[1]
        melons = words[2]
        amount_paid = words[3]

    #calculate expected cost and format it with two decimal places
        customer_expected = int(melons) * melon_cost
        customer_expected = f"{customer_expected:.2f}"

    #print a record if the customer underpaid (or overpaid)    
        if customer_expected != amount_paid:
            print(f"{customer_name} paid ${amount_paid}", 
                f"expected ${customer_expected}"
                )
underpaid()