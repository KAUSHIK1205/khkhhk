# Function to separate and square even and odd numbers
def separate_and_square(start, end):
    odd_squares = {}
    even_squares = {}
    
    for number in range(start, end + 1):
        square = number ** 2
        
        if number % 2 == 0:
            even_squares[number] = square
        else:
            odd_squares[number] = square
    
    return odd_squares, even_squares

# Get user input for the range of numbers
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Get the odd and even squares
odd_squares, even_squares = separate_and_square(start, end)

print("\nOdd square numbers and their values:")
for number, square in odd_squares.items():
    print(f"{number}: {square}")

print("\nEven square numbers and their values:")
for number, square in even_squares.items():
    print(f"{number}: {square}")
