sum = 0
while True:
    userInput = input("Enter the item price or press q to quit: ")
    if userInput != 'q':
      sum = sum + int(userInput)
      print(f"Order total so far {sum}")
    else:
       print(f"Your Total Bill is {sum}. Thanks for shopping with us")
       break