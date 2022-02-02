# Create a thing called "log_file" to hold the contents of the log text file.
log_file = open("um-server-01.txt")

#Define a function for printing sales by day that takes the log_file as a parameter
def sales_reports(log_file):
#go through each line in the file output
    for line in log_file:
#strip blank trailing characters
        line = line.rstrip()
#splice the first three characters from the line and assign them to the variable "day"
        day = line[0:3]
#select just the lines that match the specified day and print them.
        if day == "Mon":
            print(line)

#call the function to make it execute and pass in 'log_file'
sales_reports(log_file)
