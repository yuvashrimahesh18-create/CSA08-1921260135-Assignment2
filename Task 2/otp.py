# OTP verification using while loop

correct_otp = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:

    entered_otp = input("Enter your OTP: ")

    if entered_otp == "":
        print("Blank input! Please enter your OTP.")
        continue

    attempts += 1

    if entered_otp == correct_otp:
        print("Correct OTP! Access granted.")
        break
    else:
        print("Incorrect OTP!")

else:
    print("Maximum attempts reached. Account locked.")
    # OTP verification using for loop

correct_otp = "1234"

for attempt in range(3):

    while True:
        entered_otp = input("Enter your OTP: ")

        if entered_otp == "":
            print("Blank input! Please enter your OTP.")
            continue

        break

    if entered_otp == "0000":
        pass  # Demonstrates pass: no action is performed

    if entered_otp == correct_otp:
        print("Correct OTP! Access granted.")
        break
    else:
        print("Incorrect OTP!")

else:
    print("Maximum attempts reached. Account locked.")