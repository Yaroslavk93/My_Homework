import os


def find_path(my_path: str) -> list:
    with os.scandir(my_path) as file:
        for i in file:
            i_path = os.path.abspath(os.path.join(i))
            if os.path.isfile(i_path) and i_path.endswith('.py'):
                yield i_path
            else:
                pass
            if os.path.isdir(i_path):
                yield from find_path(i_path)


def count_code(file_open: list):
    count = 0
    for i_file in file_open:
        with open(i_file, 'r', encoding='utf-8') as file:
            text = file.read().split('\n')

            for line in text:
                if not line.strip() == '' \
                        and not line.strip().startswith('#') \
                        and not line.strip().startswith('"'):
                    count += 1
            yield count


file_path = os.path.abspath(os.path.join('../..'))
file_dir = find_path(file_path)
count_line = count_code(file_dir)
print([next(count_line) for _ in count_line][-1])
