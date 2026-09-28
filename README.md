# algomate
Python-based algorithmic utility for quick validation of mathematical computations  and list processing operations.
AlgoMate

A Comprehensive Algorithmic Problem-Solving Utility

Project Overview

AlgoMate is an interactive command-line application designed to provide students and professionals with quick access to essential mathematical and list manipulation algorithms. The tool consolidates commonly used number theory operations and list processing functions into a user-friendly menu-driven interface, making it ideal for learning, prototyping, and testing algorithmic solutions.

Features
Number Tools Module
GCD & LCM Calculation: Compute Greatest Common Divisor and Least Common Multiple for two numbers
Prime Number Checker: Verify if a number is prime using trial division optimization
Prime Factorization: Decompose a number into its prime factors
Fibonacci Generator: Calculate Fibonacci numbers at specific indices and generate sequences
Factorial Calculator: Compute factorial of non-negative integers
Square Root Calculator: Calculate precise square roots with error handling
Power Function: Compute base raised to exponent with validation
List Tools Module
List Reversal: Reverse a list of integers
Duplicate Removal: Remove duplicates while preserving order
Maximum Finder: Identify the largest element in a list
Occurrence Counter: Count how many times a value appears in a list
Kth Smallest Element: Find the k-th smallest unique element in a list
List Sorting: Sort a list in ascending order
Technologies & Tools Used
Language: Python 3.8+
Libraries: math module (standard library)
Architecture: Modular function-based design with menu-driven CLI
Error Handling: Comprehensive try-catch blocks with custom ValueError messages
Prerequisites
Python 3.8 or higher
No external dependencies required (uses only Python standard library)
Installation & Setup
Step 1: Clone or Download the Project
bash
# If using git
git clone <repository-url>
cd algomate

# Or simply extract the project folder
Step 2: Verify Python Installation
bash
python --version
# or
python3 --version
Step 3: Run the Application
bash
python algomate.py
# or
python3 algomate.py
How to Use
Starting the Application
$ python algomate.py

AlgoMate
1. Number tools
2. List tools
0. Exit

Choose:
Number Tools Example
Choose: 1

Number Tools
1. GCD and LCM
2. Prime check
3. Prime factorization
4. Fibonacci
5. Factorial
6. Square root
7. Power
0. Back

Choose: 1
First number: 48
Second number: 18
GCD: 6
LCM: 144
List Tools Example
Choose: 2

List Tools
1. Reverse list
2. Remove duplicates
3. Find maximum
4. Count occurrences
5. Find kth smallest
6. Sort list
0. Back

Choose: 1
Enter numbers separated by commas: 1, 2, 3, 4, 5
Reversed: [5, 4, 3, 2, 1]
Instructions for Testing
Test Case 1: Prime Factorization

Input: Number: 60
Expected Output: Factors: [2, 2, 3, 5]
Verification: 2 × 2 × 3 × 5 = 60 ✓

Test Case 2: Fibonacci Sequence

Input: Fibonacci index: 5
Expected Output:

Value: 5
Sequence: [0, 1, 1, 2, 3, 5]
Test Case 3: Remove Duplicates

Input: Enter numbers: 1, 2, 2, 3, 3, 3, 4
Expected Output: Without duplicates: [1, 2, 3, 4]

Test Case 4: Find Kth Smallest

Input: Numbers: 5, 2, 8, 1, 9; k: 3
Expected Output: 3rd smallest value: 5

Test Case 5: Error Handling

Input: Negative number for factorial
Expected Output: Error: Factorial is not available for negative numbers.

Automated Testing

Run the test suite:

bash
python -m unittest discover -s tests -p "test_*.py"
Project Structure
algomate/
├── algomate.py                 
├── README.md               
├── statement.md              
├── tests/
│   ├── test_number_tools.py   
│   └── test_list_tools.py    
└── docs/
    └── architecture.md        
Code Quality Standards
Modular Design: Separate functions for each algorithm
Error Handling: Comprehensive input validation with descriptive error messages
Code Documentation: Docstrings for all major functions
Naming Conventions: Clear, descriptive function and variable names
Performance: Optimized algorithms (e.g., trial division up to √n for primality testing)
Key Algorithms Implemented
Euclidean Algorithm: GCD calculation
Trial Division: Prime checking and factorization
Fibonacci Iteration: Efficient sequence generation
Merge/Quick Sort Concepts: List sorting
Hash-based Approach: Duplicate removal using dictionaries
Non-Functional Requirements
Performance: Handles numbers up to 10^9 efficiently; prime checking completes in < 1 second
Usability: Intuitive menu-driven interface with clear prompts and error messages
Reliability: Robust error handling for invalid inputs and edge cases
Maintainability: Well-commented code with consistent structure for easy future enhancements
Scalability: Can be extended with additional mathematical and list operations
Future Enhancements
Add GCD/LCM for multiple numbers
Implement matrix operations module
Add permutation and combination calculators
Create graphical user interface (GUI)
Support for large number arithmetic
Data persistence (save/load operation history)
Performance benchmarking module
Learning Outcomes

After using AlgoMate, you will understand:

Implementation of fundamental number theory algorithms
List manipulation techniques in Python
Menu-driven application design
Input validation and error handling
Code organization and modularity

