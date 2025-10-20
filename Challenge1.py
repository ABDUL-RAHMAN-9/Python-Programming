'''
Write a function to split the restaurant bill among friends.

   - Take the subtotal of the bill and the number of friends as inputs.
   - Calculate the total bill by adding 20% tax to the subtotal and then divide it by the number of friends.
   - Return the amount each friend has to pay, rounded off to two decimal places.
'''

# Function to split the restaurant bill among friends
def split_bill(subtotal, number_of_friends):
    # Step 1: Add 20% tax to the subtotal
    total = subtotal + (subtotal * 0.20)
    
    # Step 2: Divide total bill equally among friends
    each_friend_pays = total / number_of_friends
    
    # Step 3: Round off the amount to two decimal places
    return round(each_friend_pays, 2)


# --- Main Program ---
# Taking input from the user
subtotal = float(input("Enter the subtotal of the bill: "))
number_of_friends = int(input("Enter the number of friends: "))

# Calculating the split amount
amount_per_person = split_bill(subtotal, number_of_friends)

# Displaying the result
print("Each friend has to pay: ₹", amount_per_person)
