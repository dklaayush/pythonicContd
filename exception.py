# Exception handling responds to unwanted events during execution 
# to prevent the program from crashing abruptly.

a = input("Enter a number: ")

try:
    num = int(a)  # Convert to int inside try block
    print(f"\nMultiplication table of {num} is:")
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")

except ValueError:
    # Specific error catches non-numeric inputs first
    print("Error: The value entered is not a valid integer!")

except Exception as e:
    # Catch-all for any other unexpected errors
    print(f"An unexpected error occurred: {e}")

print("\nEnd of code")