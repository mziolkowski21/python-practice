class WrongMatrix(Exception):
    """Raised when matrix has wrong formatting"""
    pass


class WrongMatrixType(WrongMatrix):
    """Raised when matrix has wrong type"""
    pass


class WrongMatrixDimensions(WrongMatrix):
    """Raised when matrix has wrong dimensions"""
    pass


def ensure_correct_matrix(matrix):
    """Ensures matrix has correct type, each row has the same amount of columns and contains only integers"""
    if type(matrix) == str:
        matrix = [rows.split() for rows in matrix.split("\n")]
        matrix = [[int(col) for col in row] for row in matrix]
    elif type(matrix) != str and type(matrix) != list:
        raise WrongMatrixType(f"Matrix has to be either a string or a list but it is a {type(matrix)}")
    else:
        matrix = [[int(col) for col in row] for row in matrix]
    col_length = len(matrix[0])
    for row in matrix:
        if len(row) != col_length:
            raise WrongMatrixDimensions("At least one row has different amount of columns")
    return matrix


def matrix_extractor(matrix, row, col, move_range):
    """Extracts a list of numbers that are in move range from a number at position [row][column]."""
    result = []
    row_helper = move_range

    for i in range(move_range + 1):
        negative_row = (row - move_range + i) < 0
        negative_col = col - i < 0
        if negative_row:
            continue
        else:
            try:
                matrix[row - move_range + i]
            except IndexError:
                continue
            else:
                if negative_col:
                    result.extend(matrix[row - move_range + i][0:col + i + 1])
                else:
                    result.extend(matrix[row - move_range + i][col - i:col + i + 1])

    for i in range(move_range):
        negative_col = col - i < 0
        try:
            matrix[row+row_helper]
        except IndexError:
            continue
        else:
            if negative_col:
                result.extend(matrix[row+row_helper][0:col+i+1])
            else:
                result.extend(matrix[row+row_helper][col-i:col + i + 1])
        row_helper -= 1

    result.remove(matrix[row][col])
    return result


def condition_passed(extracted_vals, condition):
    """Returns True if there is at least one extracted number that is equal to the condition"""
    return condition in extracted_vals


def matrix_solver(matrix: list, conditions: list):
    """
    Given 2D integer array (nested python lists) and list of tuples with conditions in form (move_range,
    condition_to_meet) returns a list of numbers from 2D array that meet these conditions.

    By condition one means that in move_range from number n at [row][column] there is at least one number that is equal
    to n+y where move can only be taken in vertical and horizontal steps.
    """

    matrix = ensure_correct_matrix(matrix)
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = []

    for row in range(num_rows):
        for col in range(num_cols):
            assessor = 0
            for move_range, condition in conditions:
                extracted = matrix_extractor(matrix, row, col, move_range)
                passed = condition_passed(extracted, matrix[row][col] + condition)
                if passed:
                    assessor += 1
                else:
                    break
            if assessor == len(conditions):
                result.append(matrix[row][col])
    return result



if __name__ == "__main__":

    string = '''52 9 35 11 18 16 80 7 21
                29 15 70 89 75 9 78 86 4
                58 26 4 6 70 52 15 72 84
                17 37 85 54 53 87 38 97 9
                72 21 92 83 38 2 39 56 84
                43 61 25 96 33 19 48 39 56
                54 62 4 47 53 17 49 31 61
                31 94 29 7 46 11 4 75 88
                46 8 74 96 83 51 65 36 5'''

    matrix = ensure_correct_matrix(string)
    m2 = [[column for column in row[:5]] for row in matrix[:5]]

    conditions = [(6,5), (2,-12), (7, -4), (3,15)]
    c2 = [(1, 17), (1,1), (2,22)]

    print(matrix_solver(matrix, conditions))
    print(matrix_solver(m2, c2))

    a = matrix_extractor(matrix, 4, 3, 3)
    b = matrix_extractor(matrix, 1, 1, 3)

    expected = [89, 4, 6, 70, 37, 85, 54, 53, 87, 72, 21, 92, 38, 2, 39, 61, 25, 96, 33, 19, 4, 47, 53, 7]
    expected2 = [52, 9, 35, 11, 29, 70, 89, 75, 58, 26, 4, 6, 17, 37, 85, 21]
    print(sorted(a))
    print(sorted(expected))
    print(b)
    print(sorted(a) == sorted(expected))
    print(sorted(b) == sorted(expected2))