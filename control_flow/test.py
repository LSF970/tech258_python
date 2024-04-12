user_prompt = True
while user_prompt:
    age = input("What is your age? ")
    # Note that input is always str, we need to convert it before we can compare it
    if age.isdigit() and int(age) <= 117:
        user_prompt = False
    else:
        print("Please provide your answer in digits, below 117")

print(f"Your age is {age}")