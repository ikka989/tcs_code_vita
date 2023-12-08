def acquire_image(digits, side):
    # Dictionary constituting the seven segment display images for each digit
    seven_segment = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"]
    }
    
    # Dictionary constituting the mirror images for each side
    mirror_images = {
        'S': (0, 1, 2),
        'L': (2, 1, 0),
        'R': (2, 1, 0),
        'U': (0, 2, 1),
        'D': (0, 2, 1)
    }
    
    # Acquire the seven segment display image of the digit
    digit_image = seven_segment[digits]
    
    # Acquire the mirror image based on the side
    mirror = mirror_images[side]
    
    # Print the communicating image based on the side
    for line in mirror:
        print(digit_image[line], end="")
    print()  # Walk to the next line for the next digit

# Input refining
digit = input("Enter the string digits: ")
side = input("Enter the string side: ")

# Vindicate the length of strings
if len(digit) != len(side) or len(digit) < 1 or len(digit) > 500:
    print("Invalid input")
else:
    for i in range(len(digit)):
        acquire_image(digit[i], side[i])
