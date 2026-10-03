"""
RECORD CHECK  -  my version
===========================

Name  : Vijaytharun
Lane  :  AI
Date  : 01/10/2026

Run it:   python template.py
"""

# Tracks over limit records
over_limit_count = 0

# Loops until the user decides to quit
while True:
    dataset_name = input("Enter dataset name (or 'quit' to stop): ")
    if dataset_name.lower() == "quit":
        break

    rows_loaded = float(input("Enter rows loaded: "))
    rows_expected = float(input("Enter rows expected: "))

    difference = rows_expected - rows_loaded
    percent = (rows_loaded / rows_expected) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1  # Add 1 to the count if the percent is over 100
    elif percent >= 90:
        status = "WARNING" # prints warning if the percent is between 90 and 100
    else:
        status = "OK" # prints ok if the percent is below 90

    print() #gives a space between the input and the output
    print("=" * 34) # prints a line of 34 equal signs
    print(f"  RECORD CHECK  -  {dataset_name}") # prints the dataset name
    print("=" * 34  ) # prints a line of 34 equal signs
    print(f"  Loaded      : {rows_loaded:>10.2f}")
    print(f"  Expected    : {rows_expected:>10.2f}")
    print(f"  Difference  : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f}%")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()

print(f"Session finished. Total OVER LIMIT records: {over_limit_count}") # prints the total number of over limit records at the end of the session