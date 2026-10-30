def subsidy_separate(units, ration_card, elderly):

    if units <= 100:
        print("Full subsidy")

    if 101 <= units <= 200 and ration_card:
        print("Partial subsidy")

    if units > 200 and elderly:
        print("Elderly exception subsidy")

    if 101 <= units <= 200 and not ration_card:
        print("No subsidy")

    if units > 200 and not elderly:
        print("No subsidy")


# Test households
households = [
    (100, False, False),
    (101, True, False),
    (101, False, False),
    (150, True, False),
    (200, False, False),
    (200, True, False),
    (201, False, True),
    (201, True, False)
]

for i, household in enumerate(households, start=1):
    print("Household", i, end=": ")
    subsidy_separate(*household)

    # Second implementation using if-elif-else

def subsidy_elif(units, ration_card, elderly):

    if units <= 100:
        return "Full subsidy"

    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"

    elif units > 200:
        if elderly:
            return "Elderly exception subsidy"
        else:
            return "No subsidy"


print("\nUsing if-elif-else:")

for i, household in enumerate(households, start=1):
    decision = subsidy_elif(*household)
    print("Household", i, ":", decision)
    # Alternative using match-case

def subsidy_match(units, ration_card, elderly):

    if units <= 100:
        category = 1
    elif 101 <= units <= 200 and ration_card:
        category = 2
    elif 101 <= units <= 200:
        category = 3
    elif units > 200 and elderly:
        category = 4
    else:
        category = 3

    match category:
        case 1:
            return "Full subsidy"
        case 2:
            return "Partial subsidy"
        case 3:
            return "No subsidy"
        case 4:
            return "Elderly exception subsidy"


print("\nUsing match-case:")

for i, household in enumerate(households, start=1):
    decision = subsidy_match(*household)
    print("Household", i, ":", decision)