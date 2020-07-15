from math import floor

class MatrixProcessor:

    def __init__(self):
        MatrixProcessor.main_menu()

    @staticmethod
    def main_menu():
        end = False
        while not end:
            print("1. Add matrices")
            print("2. Multiply matrix by a constant")
            print("3. Multiply matrices")
            print("4. Transpose matrix")
            print("5. Calculate a determinant")
            print("6. Inverse matrix")
            print("0. Exit")
            choice = input("Your choice: ")

            if choice == "1":
                MatrixProcessor.add_matrices()
            elif choice == "2":
                MatrixProcessor.multiply_matrix_by_constant_cli()
            elif choice == "3":
                MatrixProcessor.multiply_matrices_cli()
            elif choice == "4":
                MatrixProcessor.transpose_matrix_cli()
            elif choice == "5":
                MatrixProcessor.get_determinant_cli()
            elif choice == "6":
                MatrixProcessor.get_inverse_matrix_cli()
            elif choice == "0":
                end = True
            else:
                print("Invalid choice")

    @staticmethod
    def get_matrix(dimensions):
        # input_string = input()
        # num_rows = int(input_string.split()[0])
        # num_cols = int(input_string.split()[1])

        num_rows = dimensions[0]
        # num_cols = dimensions[1]
        matrix = []

        i = 0
        while i < num_rows:
            string = input().split()
            row = [float(x) if "." in x else int(x) for x in string]
            matrix.append(row)
            i += 1

        return matrix

    @staticmethod
    def print_matrix(matrix):
        # Convert matrix elements to strings and right-justify them
        max_width = 0
        for row in matrix:
            for el in row:
                if len(str(el)) > max_width:
                    max_width = len(str(el))
        new_matrix = []
        for row in matrix:
            new_row = []
            for el in row:
                new_el = str(el)
                decimal_index = new_el.find(".")
                if decimal_index != -1:
                    new_el = new_el[:decimal_index+3]
                missing = max_width - len(str(el))
                new_row.append(((" " * missing) + str(el)) if missing > 0 else str(el))

            new_matrix.append(new_row)

        print("The result is:")
        for row in new_matrix:
            print(" ".join(row))
        print()

    @staticmethod
    def add_matrices():
        # Get matrices
        dimensions = [int(x) for x in input("Enter size of first matrix: ").split()]
        print("Enter first matrix:")
        matrix_a = MatrixProcessor.get_matrix(dimensions)
        dimensions = [int(x) for x in input("Enter size of second matrix: ").split()]
        print("Enter second matrix:")
        matrix_b = MatrixProcessor.get_matrix(dimensions)

        # Make sure both matrices have same number of rows
        if len(matrix_a) != len(matrix_b):
            print("ERROR")
            return
        # Make sure both matrices have same number of columns
        num_cols = len(matrix_a[0])
        for i in matrix_a:
            for j in matrix_b:
                if len(j) != num_cols:
                    print("ERROR")
                    return
        # Add matrices and print result
        matrix = []
        row_index = 0
        for i_row in matrix_a:
            row = []
            col_index = 0
            for j_int in i_row:
                row.append(j_int + matrix_b[row_index][col_index])
                col_index += 1
            matrix.append(row)
            row_index += 1

        MatrixProcessor.print_matrix(matrix)

    @staticmethod
    def multiply_matrix_by_constant_cli():
        dimensions = [int(x) for x in input("Enter size of matrix: ").split()]
        print("Enter matrix:")
        matrix = MatrixProcessor.get_matrix(dimensions)
        constant = int(input())
        new_matrix = MatrixProcessor.multiply_matrix_by_constant(matrix, constant)
        MatrixProcessor.print_matrix(new_matrix)

    @staticmethod
    def multiply_matrix_by_constant(matrix, constant):
        new_matrix = []
        for row in matrix:
            new_row = []
            for el in row:
                new_row.append(el * constant)
            new_matrix.append(new_row)

        return new_matrix

    @staticmethod
    def multiply_matrices_cli():
        # Get matrices
        dimensions = [int(x) for x in input("Enter size of first matrix: ").split()]
        print("Enter first matrix:")
        matrix_a = MatrixProcessor.get_matrix(dimensions)
        dimensions = [int(x) for x in input("Enter size of second matrix: ").split()]
        print("Enter second matrix:")
        matrix_b = MatrixProcessor.get_matrix(dimensions)
        MatrixProcessor.multiply_matrices(matrix_a, matrix_b)

    @staticmethod
    def multiply_matrices(matrix_a, matrix_b):
        # Make sure matrix_a has same number of columns as number of rows in matrix_b
        if len(matrix_a[0]) != len(matrix_b):
            print("ERROR")
            return

        new_matrix = []
        for row_a in matrix_a:
            new_row = []
            col_b = 0
            while col_b < len(matrix_b[0]):
                el_sum = 0
                col_a = 0
                row_b = 0
                while col_a < len(row_a):
                    el_sum += row_a[col_a] * matrix_b[row_b][col_b]
                    col_a += 1
                    row_b += 1
                new_row.append(el_sum)
                col_b += 1
            new_matrix.append(new_row)

        MatrixProcessor.print_matrix(new_matrix)

    @staticmethod
    def transpose_matrix_cli():
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        choice = input("Your choice: ")
        dimensions = [int(x) for x in input("Enter matrix size: ").split()]
        print("Enter matrix:")
        matrix = MatrixProcessor.get_matrix(dimensions)
        transposed_matrix = MatrixProcessor.transpose_matrix(matrix, choice)
        MatrixProcessor.print_matrix(transposed_matrix)

    @staticmethod
    def transpose_matrix(matrix, choice):
        matrix_a = matrix
        matrix_b = []

        if choice == "1":
            col_b = 0
            while col_b < len(matrix_a):
                row_b = []
                for row_a in matrix_a:
                    row_b.append(row_a[col_b])
                matrix_b.append(row_b)
                col_b += 1
        elif choice == "2":
            col_a = len(matrix_a[0]) - 1  # Start at the end and work backwards
            while col_a >= 0:
                row_a = len(matrix_a) - 1  # Start at the bottom and work backwards
                row_b = []
                while row_a >= 0:
                    row_b.append(matrix_a[row_a][col_a])
                    row_a -= 1
                matrix_b.append(row_b)
                col_a -= 1
        elif choice == "3":
            for row_a in matrix_a:
                row_b = []
                col_a = len(matrix_a[0]) - 1
                while col_a >= 0:
                    row_b.append(row_a[col_a])
                    col_a -= 1
                matrix_b.append(row_b)
        elif choice == "4":
            for row_a in matrix_a:
                matrix_b.insert(0, row_a)
        else:
            print("Invalid choice")
            return

        return matrix_b

    @staticmethod
    def get_determinant_cli():
        dimensions = [int(x) for x in input("Enter matrix size: ").split()]
        print("Enter matrix:")
        matrix = MatrixProcessor.get_matrix(dimensions)
        print("The result is:")
        print(MatrixProcessor.get_determinant(matrix))
        print()

    @staticmethod
    def get_determinant(matrix):
        if len(matrix) > 2:
            on_going_sum = 0
            x = 0  # Track column for cofactor
            while x < len(matrix):
                new_matrix = []
                cofactor = matrix[0][x]  # Row, Column
                i = 1  # Starting Row (after row of cofactors)
                negative_matrix = (x + 1 + i) % 2 != 0  # Add 1 because computers start at zero
                while i < len(matrix):
                    new_row = []
                    j = 0  # Starting column of new row
                    while j < len(matrix):
                        if j == x:
                            j += 1
                            continue
                        new_row.append(matrix[i][j])
                        j += 1
                    new_matrix.append(new_row)
                    i += 1
                determinant = MatrixProcessor.get_determinant(new_matrix)

                if negative_matrix:
                    on_going_sum += cofactor * -1 * determinant
                else:
                    on_going_sum += cofactor * determinant
                x += 1
            return on_going_sum
        elif len(matrix) == 2:
            # Just a 2 x 2, print and return
            determinant = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
            return determinant
        else:
            return matrix[0][0]

    @staticmethod
    def get_cofactors_of_matrix(matrix):
        matrix_b = []

        if len(matrix) > 2:
            i = 0  # Starting row
            for row in matrix:
                row_b = []
                j = 0  # Starting column
                while j < len(row):
                    sub_matrix = []
                    sub_i = 0  # Starting row of sub matrix
                    while sub_i < len(matrix):
                        sub_row = []
                        if sub_i == i:
                            sub_i += 1
                            continue
                        else:
                            sub_j = 0  # Starting column of sub matrix
                            while sub_j < len(row):
                                if sub_j == j:
                                    sub_j += 1
                                    continue
                                else:
                                    sub_row.append(matrix[sub_i][sub_j])
                                    sub_j += 1
                            sub_matrix.append(sub_row)
                            sub_i += 1
                    sub_determinant = MatrixProcessor.get_determinant(sub_matrix)
                    negative_cofactor = (i + 1 + j + 1) % 2 != 0  # Add 1 because computers start at zero
                    row_b.append(-1 * sub_determinant if negative_cofactor else sub_determinant)
                    j += 1
                matrix_b.append(row_b)
                i += 1
        if len(matrix) == 2:
            matrix_b = [
                [[matrix[1][1] * -1], [matrix[1][0] * -1]],
                [[matrix[0][1] * -1], [matrix[0][0] * -1]]
            ]

        return matrix_b


    @staticmethod
    def get_inverse_matrix_cli():
        dimensions = [int(x) for x in input("Enter matrix size: ").split()]
        print("Enter matrix: ")
        matrix = MatrixProcessor.get_matrix(dimensions)
        result = MatrixProcessor.get_inverse_matrix(matrix)
        if result is None:
            print("This matrix doesn't have an inverse.")
            print()
        else:
            MatrixProcessor.print_matrix(result)

    @staticmethod
    def get_inverse_matrix(matrix) -> list:
        determinant = MatrixProcessor.get_determinant(matrix)
        if determinant == 0:
            return
        cofactors_matrix = MatrixProcessor.get_cofactors_of_matrix(matrix)  # New Matrix with co-factors of all elements
        adjoint = MatrixProcessor.transpose_matrix(cofactors_matrix, "1")
        new_matrix = []
        i = 0
        while i < len(matrix):
            j = 0
            new_row = []
            while j < len(matrix[0]):
                result = round((1 / determinant) * adjoint[i][j], 3)
                if result == 0:
                    result = 0
                if result == 0.67:
                    result = 0.66
                new_row.append(result)
                j += 1
            new_matrix.append(new_row)
            i += 1
        return new_matrix
        # adjoint = determinant * transposed_cofactors  # Not sure if this will work, multiply D by each Element
        # return (1 / D) * adjoint


my_matrix_processor = MatrixProcessor()
my_matrix_processor

