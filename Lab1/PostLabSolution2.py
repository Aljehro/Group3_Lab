# CPE106L-4/E01
# Lab1 || Postlab #2
# Group #3 Members: Abante, Alarilla, Fernandez

import os

def navigate_file():
    filename = input("Enter the filename: ")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        num_lines = len(lines)
        print(f"The file contains {num_lines} lines.")

        while True:
            try:
                line_num = int(input("Enter a line number (0 to quit): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if line_num == 0:
                print("Exiting the program.")
                break
            elif 1 <= line_num <= num_lines:
                print(f"Line {line_num}: {lines[line_num - 1].strip()}")
            else:
                print(f"Please enter a line number between 1 and {num_lines}.")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found in the current directory.")
    except IOError:
        print("An error occurred while reading the file.")

navigate_file()
