# calculator_with_search.py
# Smart Calculator with Equation Solver
# Uses search concepts from Chapter 3

import operator
import math

class SmartCalculator:
    """
    A calculator that can solve simple equations using search
    """

    def __init__(self):
        # Create a dictionary of basic math operations
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        }

    def basic_calculate(self, num1, op, num2):
        """
        Perform basic calculation
        """
        # Check if operation is valid and perform calculation
        if op in self.operations:
            try:
                return self.operations[op](num1, num2)
            except ZeroDivisionError:
                return "Error: Division by zero"
        else:
            return "Error: Unsupported operation"

    def solve_for_x(self, target, operation, known_value, x_position='left'):
        """
        Solve simple equations like: x + 5 = 10 or 3 * x = 15
        Uses a simple search approach to find x
        """
        min_x = -100
        max_x = 100
        step = 0.1
        current_x = min_x
        best_x = None
        best_difference = float('inf')

        while current_x <= max_x:
            if x_position == 'left':
                result = self.operations[operation](current_x, known_value)
            else:
                result = self.operations[operation](known_value, current_x)

            difference = abs(result - target)
            if difference < 0.0001:
                return round(current_x, 4)

            if difference < best_difference:
                best_difference = difference
                best_x = current_x

            current_x += step

        return round(best_x, 4)

    def visualize_search(self, target, operation, known_value, x_position='left'):
        """
        Show the search process step by step
        """
        print("\n🔍 SEARCHING FOR SOLUTION...")
        print(f"Goal: Find x where ", end="")
        if x_position == 'left':
            print(f"x {operation} {known_value} = {target}")
        else:
            print(f"{known_value} {operation} x = {target}")

        test_values = [-10, -5, 0, 5, 10, 15, 20]
        print("\nTesting values:")
        print("-" * 40)
        for x in test_values:
            if x_position == 'left':
                result = self.operations[operation](x, known_value)
            else:
                result = self.operations[operation](known_value, x)
            distance = abs(result - target)
            print(f"x = {x:>5} → result = {result:>8.4f} → distance = {distance:.4f}")

    def equation_solver_menu(self):
        """
        Interactive menu for equation solving
        """
        print("\n" + "="*50)
        print("EQUATION SOLVER (using search)")
        print("="*50)
        print("I can solve equations like:")
        print(" x + 5 = 10")
        print(" x * 3 = 15")
        print(" 10 - x = 7")
        print(" 20 / x = 4")

        # Get equation parts from user
        try:
            left = input("\nEnter left side (e.g., x + 5 or 10 - x): ").strip()
            right = float(input("Enter right side (e.g., 10): ").strip())

            if 'x' not in left:
                print("Equation must contain 'x'")
                return

            parts = left.split()
            if len(parts) != 3:
                print("Invalid format. Use format like 'x + 5'")
                return

            if parts[0] == 'x':
                x_position = 'left'
                operation = parts[1]
                known_value = float(parts[2])
            elif parts[2] == 'x':
                x_position = 'right'
                operation = parts[1]
                known_value = float(parts[0])
            else:
                print("Invalid equation format.")
                return

            self.visualize_search(right, operation, known_value, x_position)
            solution = self.solve_for_x(right, operation, known_value, x_position)
            print(f"\n✅ Solution: x = {solution}")

        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    calc = SmartCalculator()
    calc.equation_solver_menu()
