# Identical Snowflake Finder
This Python program is designed to identify identical snowflakes based on the lengths of their arms. It reads a list of snowflake vectors, searches for identical pairs, and returns their indices from the input list.

## Prerequisites
- Python 3.10.12 (Install Python: sudo apt install python3)
- NumPy library (Install NumPy: pip install numpy)

## File Format

The input file (vectors.txt) should contain snowflake vectors, each represented as a comma-separated list. Each vector should be on a new line in the file.

### Example vectors.txt file:

3,10,9,6,4,8

4,7,8,5,6,10

4,3,2,10,2,10

...

## Running the Program
- Make sure Python 3.10.12 is installed on your system.
- Install the required NumPy library by running: pip install numpy
- Place the vectors.txt file in the same directory as the program.
- Open a terminal and navigate to the program's directory.
- Run the program using the following command: python3 main.py

## Output
The program will print a dictionary containing identical snowflakes and their corresponding indices in the input list.

Note: The program assumes that the input file (vectors.txt) is properly formatted, with values separated by commas and each vector on a new line. Ensure the correct format to obtain accurate results.