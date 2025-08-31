
def count_lines(file_path):
    f = open(file_path, 'r')
    line = f.readlines()
    f.close()
    return len(line)

def count_char(file_path):
    f = open(file_path, 'r')
    text = f.read()
    f.close()
    return len(text)

def test(file_path):
    line = count_lines(file_path)
    text = count_char(file_path)
    return line , text

def count_words(file_path):
    f = open(file_path, 'r')
    text = f.read()
    text = text.split()

    f.close()
    return len(text)

