def print_main_file_lines(n:int) -> None:
    '''
    Function to print the first n
    lines of the main.py

    Arguments:
    - n: first n lines of main.py to print

    Return: None
    '''

    with open('test/main.py', 'r') as f:
        lines = f.readlines()
        num_rows = len(lines)

    if num_rows < n:
        print(f'File has less than {n} lines; printing {num_rows} lines')
        print('-----------------------------------------------')
        lines_to_print = num_rows
    else:
        lines_to_print = n

    for i in range(lines_to_print):
        print(f'line {i+1}: {lines[i].strip()}')

if __name__ == '__main__':
    print_main_file_lines(26)