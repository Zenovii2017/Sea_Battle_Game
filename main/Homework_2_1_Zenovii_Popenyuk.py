def read_file(path):
    """
    read file and make field for sea battle
    (str) -> data
    :param path: file
    :return: dict
    """
    import string
    field = dict()
    letters = string.ascii_uppercase[:10]
    with open(path, 'r', errors='ignore') as open_file:
        i = 0
        for readline in open_file:
            key = letters[i]
            field[key] = []
            for symbol in readline:
                if len(field[key]) < 10:
                    if symbol == '' or symbol == '*' or symbol == 'x':
                        if symbol == ' ':
                            field[key] = ' '
                        else:
                            field[key].append(symbol)
                    else:
                        field[key].append(' ')
                    if symbol == readline[-1] and len(field[key]) != 10:
                        while len(field[key]) != 10:
                            field[key].append(' ')
                else:
                    break
            i += 1
    return field


def has_ship(data, input_tuple):
    """
    check if in this cellule
    :param data: dict
    :param tuple: tuple
    :return: bool
    """
    if data[input_tuple[0]][input_tuple[1]] == 'x' or \
            data[input_tuple[0]][input_tuple[1]] == '*':
        return True
    else:
        return False


def ship_size(data, input_tuple):
    """
    calcute lenght for boat of coordinate x and y.
    function check if under or left is boat if no then calcute
    lenght if yes return None because lenght thisboat we exactly calculate
    :param data: dict
    :param input_tuple: tuple
    :return: tuple
    """
    output_lst = [1, 1]
    try:
        if data[chr(ord(input_tuple[0]) - 1)][input_tuple[1]] == '*' or \
                                    data[chr(ord(input_tuple[0]) - 1)][
            input_tuple[1]] == 'x':
            return None
    except:
        pass
    try:
        if data[input_tuple[0]][input_tuple[1] - 1] == '*' or \
            data[input_tuple[0]][input_tuple[1] - 1] == 'x':
            return None
    except:
        pass
    for i in range(1, 4):
        try:
            if output_lst[0] == 4 or output_lst[1] == 4:
                break
            elif data[chr(ord(input_tuple[0]) + i)][input_tuple[1]] == ' ':
                break
            else:
                output_lst[1] += 1
        except:
            break
    for i in range(1, 4):
        try:
            if output_lst[0] == 4 or output_lst[1] == 4:
                break
            elif data[input_tuple[0]][input_tuple[1] + i] == ' ':
                break
            else:
                output_lst[0] += 1
        except:
            break
    return tuple(output_lst)


def is_valid(data):
    """
    check if our fild is valid for game
    :param data: dict
    :return: bool
    """
    all_ships = []
    lenght = len(data['A'])
    for key in data:
        if lenght != len(data[key]):
            print()
            return False
        for x in range(0, len(data[key])):
            if has_ship(data, (key, x)):
                size_ship = ship_size(data, (key, x))
                if size_ship is not None:
                    if size_ship[0] > 1 and size_ship[1] > 1:
                        return False
                    all_ships.append(size_ship)
    four_long_ship = all_ships.count((4, 1)) + all_ships.count((1, 4))
    three_long_ship = all_ships.count((3, 1)) + all_ships.count((1, 3))
    two_long_ship = all_ships.count((2, 1)) + all_ships.count((1, 2))
    one_long_ship = all_ships.count((1, 1))
    if four_long_ship != 1 or three_long_ship != 2 or two_long_ship != 3 or \
                                                            one_long_ship != 4:
        return False
    return True


def field_to_str(data):
    """
    make sentence to print
    :param data: dict
    :return: str
    """
    sentence = 'The field is:\n'
    for key in data:
        sentence += '{} : {}\n'.format(key, data[key])
    return sentence


def generate_field():
    """
    make field for game with 10x10 cellebe
    :return: dict
    """
    import string
    import random
    field = dict()
    letters = string.ascii_uppercase[:10]
    all_format = ['horisontal', 'vertical']
    for key in letters:
        field[key] = []
        for x in range(0, 10):
            field[key].append(' ')
    for i in range(1, 5):
        count_ship = 0
        lenght_ship = i
        ship_count = 5 - i
        if i == 1:
            place = 9
        elif i == 2:
            place = 12
        elif i == 3:
            place = 15
        elif i == 4:
            place = 18
        while count_ship != ship_count:
            format = random.choice(all_format)
            if format == 'horisontal':
                max_x = 9 - i
                max_y = 9
            else:
                max_x = 9
                max_y = 9 - i
            poz_x = random.randint(0, max_x)
            poz_y = random.randint(0, max_y)
            k = 0
            if format == 'horisontal':
                for j in range(-1, lenght_ship + 1, +1):
                    try:
                        if field[letters[poz_y - 1]][poz_x + j] == ' ':
                            k += 1
                    except:
                        k += 1
                    try:
                        if field[letters[poz_y]][poz_x + j] == ' ':
                            k += 1
                    except:
                        k += 1
                    try:
                        if field[letters[poz_y + 1]][poz_x + j] == ' ':
                            k += 1
                    except:
                        k += 1
            else:
                for j in range(-1, lenght_ship + 1, +1):
                    try:
                        if field[letters[poz_y + j]][poz_x - 1] == ' ':
                            k += 1
                    except:
                        k += 1
                    try:
                        if field[letters[poz_y + j]][poz_x] == ' ':
                            k += 1
                    except:
                        k += 1
                    try:
                        if field[letters[poz_y + j]][poz_x + 1] == ' ':
                            k += 1
                    except:
                        k += 1
            if k == place:
                count_ship += 1
                for z in range(0, lenght_ship):
                    if format == 'horisontal':
                        field[letters[poz_y]][poz_x + z] = '*'
                    else:
                        field[letters[poz_y + z]][poz_x] = '*'
    while not is_valid(field):
        return generate_field
    return field


def test(path):
    """
    make some tests of our module
    :param path: file
    :return: None
    """
    readed_file = read_file('Field.txt')
    print('This field is valid: {}'.format(is_valid(readed_file)))
    print(field_to_str(readed_file))
    print('There are ships with lenght:\n(First number is lenght of x')
    print('coordinate, second is lenght of y )')
    for key in readed_file:
        for x in range(0, len(readed_file[key])):
            if has_ship(readed_file, (key, x)):
                size_ship = ship_size(readed_file, (key, x))
                if size_ship is not None:
                    print(size_ship)
    field = generate_field()
    print(is_valid(field))
    print(field_to_str(field))

if __name__ == "__main__":
    test('field.txt')
