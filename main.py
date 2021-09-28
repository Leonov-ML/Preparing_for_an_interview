from stack_app.balance import check_is_line_correct

if __name__ == "__main__":
    line = input('введите строку: ').strip()
    result = check_is_line_correct(line)
    if result:
        print('Сбалансировано')
    else:
        print('Несбалансировано')
