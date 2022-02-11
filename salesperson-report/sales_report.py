"""Generate sales report showing total melons each salesperson sold."""

#instead of using two lists, use a dictionary of salesperson:melons_sold 
#salespeople = []
#melons_sold = []
melon_sales_dict = {}

f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')
    salesperson = entries[0]
    melons = int(entries[2])    
#check if a salesperson is already in the list and removes duplicates by summing their melons sold.
#it could check if salesperson is already a key in the dictionary and update the value of melons sold.
    #if salesperson in salespeople:
        #position = salespeople.index(salesperson)

        #melons_sold[position] += melons
    if salesperson in melon_sales_dict.keys():
        melon_sales_dict[salesperson] += melons
#instead of using append (which is for lists), set the dictionary key to the value of melons sold.
    else:
        #salespeople.append(salesperson)
        #melons_sold.append(melons)
        melon_sales_dict[salesperson] = melons

#print a list of how many melons each salesperson sold
#if it's not sorted, this can loop through keys in the dictionary to print their values
#for i in range(len(salespeople)):
    #print(f'{salespeople[i]} sold {melons_sold[i]} melons')
for key in melon_sales_dict:
    print(f'{key} sold {melon_sales_dict[key]} melons')
