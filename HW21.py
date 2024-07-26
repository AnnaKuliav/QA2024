import os


def combine_text_files(source_directory):
    combined_filename = 'combined_files.txt'
    with open(combined_filename, 'w') as combined_file:
        for root, _, files in os.walk(source_directory):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    if os.path.getsize(file_path) <= 120:
                        with open(file_path, 'r') as f:
                            content = f.read()
                            combined_file.write(f"{file}\n{content}\n")


if __name__ == "__main__":
    source_directory = '/Users/annakuliavets/Documents/pythonQA2024'
    combine_text_files(source_directory)