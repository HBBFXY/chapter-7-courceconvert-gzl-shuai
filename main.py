import tokenize
from io import StringIO

def convert_python_file(source_filename, output_filename):
    """
    读取一个Python源文件，将所有非保留字的标识符转换为大写，并保存到新文件。

    :param source_filename: 输入的Python源文件路径
    :param output_filename: 输出的Python源文件路径
    """
    try:
        # 1. 读取源文件内容
        with open(source_filename, 'r', encoding='utf-8') as f_in:
            source_code = f_in.read()

        # 2. 使用tokenize模块处理代码
        # StringIO将字符串包装成一个类文件对象，供tokenize使用
        tokens = tokenize.generate_tokens(StringIO(source_code).readline)

        converted_code = []
        for token_type, token_string, _, _, _ in tokens:
            # tokenize.NAME 类型包括了变量名、函数名、类名等标识符
            if token_type == tokenize.NAME:
                # 如果这个标识符不是Python关键字，则转换为大写
                if token_string not in tokenize.keyword.kwlist:
                    converted_code.append(token_string.upper())
                else:
                    converted_code.append(token_string)
            else:
                # 对于其他类型的令牌（如关键字、字符串、数字、运算符、空格等），直接保留原样
                converted_code.append(token_string)

        # 3. 将处理后的令牌列表重新组合成字符串
        final_code = ''.join(converted_code)

        # 4. 将结果写入输出文件
        with open(output_filename, 'w', encoding='utf-8') as f_out:
            f_out.write(final_code)

        print(f"文件转换成功！结果已保存到 {output_filename}")

    except FileNotFoundError:
        print(f"错误：找不到源文件 '{source_filename}'。请确保文件存在于正确的位置。")
    except Exception as e:
        print(f"处理文件时发生错误: {e}")

# --- 主程序入口 ---
if __name__ == "__main__":
    input_file = "random_int.py"
    output_file = "RANDOM_INT.PY"

    convert_python_file(input_file, output_file)# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
