# Function to print the pattern
def print_pattern(size, initial):
    if size < 3:
        print("Size should be 3 or more for a meaningful pattern.")
        return

    for i in range(1, size + 1):
        for j in range(1, i + 1):
            if j % 2 == 0:
                print(initial, end=" ")
            else:
                print("*", end=" ")
        print()  # Move to the next line

# Get user input
try:
    size = int(input("Enter the size of the pattern (integer >= 3): "))
    initial = input("Enter the first letter of your name: ").strip().upper()

    if len(initial) != 1 or not initial.isalpha():
        print("Please enter a single valid letter for the initial.")
    else:
        print_pattern(size, initial)

except ValueError:
    print("Invalid input. Please enter a valid integer for the size.")
