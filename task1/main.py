# Function to print multiplication table
def multiplication_table(n, upto=10):
    print "Multiplication table for", n
    for i in range(1, upto + 1):
        print "{} x {} = {}".format(n, i, n * i)

# Get user input and generate the table
number = int(raw_input("Enter a number to generate its multiplication table: "))
multiplication_table(number)