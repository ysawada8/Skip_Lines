import io
import sys

def skip_line_1(file): # ファイルの内容を文字列で返す
    with io.StringIO() as f:
        sys.stdout = f
        with open(file) as i:
            for line in i:
                print(line.strip("\n"))
            file_str = f.getvalue()
            sys.stdout = sys.__stdout__
            return file_str

def skip_line_2(file): # ファイルの内容（2行目以降）を文字列で返す
    with io.StringIO() as f:
        sys.stdout = f
        with open(file) as i:
            next(i)
            for line in i:
                print(line.strip("\n"))
            file_str = f.getvalue()
            sys.stdout = sys.__stdout__
            return file_str

def skip_line_3(file): # ファイルの内容（3行目以降）を文字列で返す
    with io.StringIO() as f:
        sys.stdout = f
        with open(file) as i:
            next(i)
            next(i)
            for line in i:
                print(line.strip("\n"))
            file_str = f.getvalue()
            sys.stdout = sys.__stdout__
            return file_str