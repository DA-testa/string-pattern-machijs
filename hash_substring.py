def read_input():
    input_type = input("I or F: ").strip().upper()

    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        file_name = input("File: ").strip()
        file_path = f'tests/{file_name}'
        
        with open(file_path, 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    else:
        print("Invalid input type.")
        return

    return (pattern, text)

def print_occurrences(output):
    print('\n'.join(map(str, output)))

def get_occurrences(pattern, text):
    result = []
    pattern_len = len(pattern)
    text_len = len(text)

    if pattern_len > text_len:
        return result

    for i in range(text_len - pattern_len + 1):
        if text[i:i + pattern_len] == pattern:
            result.append(i)

    return result

if __name__ == '__main__':
    pattern, text = read_input()
    if pattern and text:
        print_occurrences(get_occurrences(pattern, text))
