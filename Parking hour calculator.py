# prompt the user to enter the number of hours they parked 

hours_parked = float(input("Enter number of hours parked: "))

#  base fee and hourly rate 
base_fee = 5.0
hourly_rate =2.50

#Calculate the total fee of parked hours
total_fee = base_fee + (hourly_rate * hours_parked)

# Display the result 
print(f" total parking fee: ${total_fee:.2f})")
