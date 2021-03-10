odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
#while number:  #shorthand version of line above, if true, so value = 1 or any other non zero number
    # Check if the number is odd.
    if number % 2 == 1:
#if number % 2:  #shorthand version of line above, if true, so value =1, so odd numbers
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

counter = 5
while counter: #shorthand version, counter is true, so 1 or above. keep looping.
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)