def read_string_as_array(row_text):
    output = []
    for char in row_text.replace("\n", ''):
        output.append(1 if char == '*' else 0)
    return output


def read_input_as_matrix(file_name):
    result = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            result.append(read_string_as_array(line))
    return result


def get_matrix_without_exception(matrix, i, j):
    if i < 0 or j < 0 or i > 79 or j > 79:
        return 0
    return matrix[i][j]


def get_neighbor_count(matrix, i, j):
    count = 0
    count += get_matrix_without_exception(matrix, i - 1, j - 1)
    count += get_matrix_without_exception(matrix, i - 1, j)
    count += get_matrix_without_exception(matrix, i - 1, j + 1)
    count += get_matrix_without_exception(matrix, i, j - 1)
    count += get_matrix_without_exception(matrix, i, j + 1)
    count += get_matrix_without_exception(matrix, i + 1, j - 1)
    count += get_matrix_without_exception(matrix, i + 1, j)
    count += get_matrix_without_exception(matrix, i + 1, j + 1)
    return count


# converted = read_input_as_matrix('../input.txt')


# print(get_neighbor_count(converted, 79, 79))
# print(get_neighbor_count(converted, 0, 79))
# print(get_neighbor_count(converted, 79, 0))
# print(get_neighbor_count(converted, 0, 0))


def dead_or_alive(cell_state, neighbor_count):
    if neighbor_count == 0 or neighbor_count == 1:
        return 0
    elif neighbor_count == 3:
        return 1
    elif neighbor_count == 2 or neighbor_count == 3:
        return cell_state
    elif neighbor_count >= 4:
        return 0


def convert_matrix_to_text(matrix):
    text = ""
    for row in matrix:
        for element in row:
            text += ' ' if element == 0 else '*'
        text += "\n"
    return text

#
# converted = read_input_as_matrix('input.txt')
# original = converted.copy()
# text = ''
# for _ in range(2):
#     next_step = []
#     for _ in range(80):
#         next_step.append([-1]*80)
#     for i in range(80):
#         for j in range(80):
#             count = get_neighbor_count(original, i, j)
#             next_step[i][j] = dead_or_alive(original[i][j], count)
#             if i == 1 and j == 2:
#                 print(count, ' ', next_step[i][j])
#     text += convert_matrix_to_text(next_step)
#     original = next_step.copy()
# with open('output.txt', 'w') as file:
#     file.write(text)


class Cellular_Automaton:
    def __init__(self, input_file_path):
        self.converted = read_input_as_matrix(input_file_path)

    def processing(self, output_file_path, steps=1):
        original = self.converted.copy()
        text = ''
        for _ in range(steps):
            next_step = []
            for _ in range(80):
                next_step.append([-1]*80)
            for i in range(80):
                for j in range(80):
                    count = get_neighbor_count(original, i, j)
                    next_step[i][j] = dead_or_alive(original[i][j], count)
            text += convert_matrix_to_text(next_step)
            original = next_step.copy()
        with open(output_file_path, 'w') as file:
            file.write(text[:-1])
