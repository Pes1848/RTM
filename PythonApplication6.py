def read_matrix_and_fill_rectangle(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    rows, coord = map(int, lines[0].split())
    matrix = [[0 for _ in range(coord)] for _ in range(rows)]

    x1, y1, x2, y2 = map(int, lines[1].split())

    r1, c1 = x1 - 1, y1 - 1
    r2, c2 = x2 - 1, y2 - 1

    row_start, row_end = min(r1, r2), max(r1, r2)
    col_start, col_end = min(c1, c2), max(c1, c2)

    for r in range(row_start, row_end + 1):
        for c in range(col_start, col_end + 1):
            if 0 <= r < rows and 0 <= c < coord:
                matrix[r][c] = 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
def count_zeros(matrix):
    return sum(cell == 0 for row in matrix for cell in row)

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

matrix = read_matrix_and_fill_rectangle('test1.txt')
print_matrix(matrix)

zero_count = count_zeros(matrix)
print(f"\nCount of zero_cubes: {zero_count}")
# Пример использования
matrix = read_matrix_and_fill_rectangle('test1.txt')
print_matrix(matrix)



