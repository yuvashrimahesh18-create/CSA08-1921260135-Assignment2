
def normalise(text):
    """Remove spaces and hyphens, and convert to uppercase."""
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.upper()
    return text
print(normalise("tn 09 ab 1234"))
print(normalise("KA-01-M-0007"))

def is_valid(reg):
    # Registration number must have 9 or 10 characters
    if len(reg) != 9 and len(reg) != 10:
        return False

    # First two characters must be letters
    if not reg[0:2].isalpha():
        return False

    # Next two characters must be digits
    if not reg[2:4].isdigit():
        return False

    # Last four characters must be digits
    if not reg[-4:].isdigit():
        return False

    # Characters in the middle must be letters
    if not reg[4:-4].isalpha():
        return False

    return True
test_numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB"
]

for number in test_numbers:
    cleaned = normalise(number)

    if is_valid(cleaned):
        print(cleaned, "- VALID")
    else:
        print(cleaned, "- INVALID")
        
def format_registration(reg):
    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]
number = "tn 09 ab 1234"

cleaned = normalise(number)

if is_valid(cleaned):
    print("Formatted number:", format_registration(cleaned))
else:
    print("Invalid registration number")