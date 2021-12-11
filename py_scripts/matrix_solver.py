def matrix_extractor(matrix, row, col, move_range):

    result = []
    for i in range(move_range + 1):
        negative_row = (row - move_range + i) < 0
        negative_col = col - i < 0
        if negative_row:
            continue
        elif negative_col:
            try:
                result.extend(matrix[row - move_range + i][0:col + i + 1])
            except IndexError:  # solves problems with reaching outside the matrix for rows
                continue
        else:
            try:
                result.extend(matrix[row - move_range + i][col - i:col + i + 1])
            except IndexError:
                continue
    for i in range(move_range):
        negative_col = col - i - 1 < 0
        if negative_col:
            try:
                result.extend(matrix[row + i + 1][0:col - i + 2])
            except IndexError:
                continue
        else:
            try:
                result.extend(matrix[row + i + 1][col + i - 1:col - i + 2])
            except IndexError:
                continue
    result.remove(matrix[row][col])
    return result


def condition_passed(extracted_vals, condition):
    return condition in extracted_vals


def matrix_solver(matrix: list, conditions: list):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = []

    for row in range(num_rows):
        for col in range(num_cols):
            assesor = 0
            for move_range, condition in conditions:
                extracted = matrix_extractor(matrix, row, col, move_range)
                passed = condition_passed(extracted, matrix[row][col] + condition)
                if passed:
                    assesor += 1
                else:
                    break
            if assesor == len(conditions):
                result.append(matrix[row][col])
    return result

# to do, convert strings to ints: def ensure_ints(matrix), ensure_matrix, ensure_dict_conditions

string = '''52 9 35 11 18 16 80 7 21
29 15 70 89 75 9 78 86 4
58 26 4 6 70 52 15 72 84
17 37 85 54 53 87 38 97 9
72 21 92 83 38 2 39 56 84
43 61 25 96 33 19 48 39 56
54 62 4 47 53 17 49 31 61
31 94 29 7 46 11 4 75 88
46 8 74 96 83 51 65 36 5'''

matrix = [rows.split() for rows in string.split("\n")]
matrix = [[int(a) for a in r] for r in matrix]

m2 = [[column for column in row[:5]] for row in matrix[:5]]


conditions = [(6,5), (2,-12), (7, -4), (3,15)]
c2 = [(1, 17), (1,1), (2,22)]

print(matrix_solver(matrix, conditions))
print(matrix_solver(m2, c2))