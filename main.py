print("This is a currency converter, you can convert your euros into pounds.")

while True:
    euro = input("Type your euros here:")

    euro= euro.replace( ",",".")

    pounds = float(euro) * 0.88

    print("{0} euros is {1} pounds.".format(euro,pounds))

    question = input("Would you like to convert again? (yes/no)")

    if question.lower() != "yes":
        print("Okay, goodbye.")
        break