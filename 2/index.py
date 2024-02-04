
def calculate_amount_per_person(bill_amount, tip_percentage, amount_of_people):
    amount_per_person = (bill_amount / amount_of_people) * (1 + tip_percentage / 100)
    return amount_per_person

inputs_array = ['amount_of_people', 'bill_amount', 'tip_percentage']

questions = {
    'amount_of_people': 'How many people are in your dinner group? ',
    'bill_amount': 'How much is the bill? ',
    'tip_percentage': 'What percentage would you like to tip? '
}

errorMessages = {
    'amount_of_people': 'Please enter a valid number.',
    'bill_amount': 'Please enter a valid number.',
    'tip_percentage': 'Please enter a valid number with no % sign.'
}

translators = {
    'amount_of_people': int,
    'bill_amount': float,
    'tip_percentage': float
}

def getInputs(inputs: dict):

    for item in inputs_array:
        if inputs.get(item) == None:
            try:
                inputs[item] = translators[item](input(questions[item]))
            except ValueError:
                print(errorMessages[item])
                return getInputs(inputs)

    return inputs



inputs = getInputs({})

amount_per_person = calculate_amount_per_person(inputs["bill_amount"], inputs["tip_percentage"], inputs["amount_of_people"])

print(f"Each person should pay: ${amount_per_person:.2f}")





