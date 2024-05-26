def sort_columns(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    columns = [[] for _ in range(num_cols)]

    for row in matrix:
        for col_index in range(num_cols):
            columns[col_index].append(row[col_index])

    for col in columns:
        col.sort()

    sorted_matrix = [[columns[col_index][row_index] for col_index in range(num_cols)] for row_index in range(num_rows)]

    return sorted_matrix


# Example
matrix = [
    ['a', 'c', 'e'],
    ['f', 'b', 'a'],
    ['a', 'n', 'k'],
    ['e', 'l', 'i']
]

sorted_matrix = sort_columns(matrix)

for row in sorted_matrix:
    print(row)
