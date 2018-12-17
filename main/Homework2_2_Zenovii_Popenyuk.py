class Game():
    """
    class that represent game see battle
    have functions:
        read_position - read position of course
        field_without_ships - make empty field
        field_with_ships - make full field
        __greetings - welcome for player
        run - run the game
        print_field - print field without ships
        is_good_attack - check if player can do this attack
        __congratulions - congratulions to player
    """
    def __init__(self):
        """
        represent class
        """
        self.__unvisible_fields = list()
        self.__visible_fields = list()
        self.__players = list()
        self.__current_player = 0
        self.__is_active = True

    def read_position(self):
        """
        read position where player had attacked
        :return: tuple
        """
        return self.__players[self.__current_player].get_position()

    def field_without_ships(self):
        """
        make field with ships with composition
        :return: list
        """
        return [Field().create_unvisible_field(),\
                Field().create_unvisible_field()]

    def field_with_ships(self):
        """
        make filds without ships with composition
        :return: list
        """
        return [Field().create_visible_ships(), Field().create_visible_ships()]

    def __greetings(self):
        """
        print welcome for player
        :return: None
        """
        print('Hello!Let`s play see battle')
        name1 = input('Please input nane of first player: ')
        player1 = Player(name1)
        self.__players.append(player1)
        name2 = input('Please input name of second player: ')
        player2 = Player(name2)
        self.__players.append(player2)

    def run(self):
        """
        run the game and this is main method
        :return: None
        """
        self.__greetings()
        print('Please wait we create your field`s...')
        self.__unvisible_fields = self.field_without_ships()
        self.__visible_fields = self.field_with_ships()
        print('This is field of O, X and * if there X you shut boat if')
        print('there * you shot there but there no boat')
        print('You can input like 11 or a1 or A1!')
        while self.__is_active:
            position = self.read_position()
            while not self.is_good_attack(position):
                print('You input wrong position for attack!')
                position = self.read_position()
            if self.__unvisible_fields[self.__current_player][position[1]]\
                                                    [position[0]] == 'X':
                self.__visible_fields[self.__current_player][position[1]]\
                                                        [position[0]] = 'X'
                print(self.print_field())
            else:
                self.__visible_fields[self.__current_player][position[1]]\
                                                        [position[0]] = '*'
                if self.__current_player == 1:
                    print(self.print_field())
                    if self.is_end():
                        self.__Congratulations()
                    self.__current_player = 0
                else:
                    print(self.print_field())
                    if self.is_end():
                        self.__Congratulations()
                    self.__current_player = 1

    def is_end(self):
        """
        check if this course is end of game
        :return: bool
        """
        if self.__unvisible_fields[self.__current_player] == \
                        self.__visible_fields[self.__current_player]:
            self.__is_active = False
            return True

    def print_field(self):
        """
        make sentence to print very pretty field
        :return: str
        """
        sentence = ''
        for field in self.__visible_fields[self.__current_player]:
            for i in field:
                sentence += i + ' '
            sentence += '\n'
        return sentence

    def is_good_attack(self, position):
        """
        check if this is good course to attack
        :param position: tuple
        :return: bool
        """
        try:
            if self.__visible_fields[self.__current_player]\
                            [position[1]][position[0]] != 'O':
                return False
        except:
            return False
        return True

    def __congratulions(self):
        """
        End of the game.Congratulions one of the players
        i dont sure in this method because I dont win anytime
        :return: None
        """
        import sys
        print('Yeah!!! The player {} is win!!!My congratulions!!!'.format(\
                                self.__players[self.__current_player].name))
        sys.Exit()


class Player():
    '''
    Class Person
    have functions:
        get_postion - get the position of input player
    '''
    def __init__(self, name):
        '''
        represent the class
        :param name: str
        '''
        self.name = name

    def get_position(self):
        '''
        get the position of input player
        :return: tuple
        '''
        import string
        letters = string.ascii_uppercase
        input_sentence = input('{}, enter move: '.format(self.name))
        input_sentence = input_sentence.upper()
        if input_sentence[0].isalpha():
            poz_y = letters.find(input_sentence[0])
        else:
            poz_y = int(input_sentence[0])
        poz_x = int(input_sentence[1]) - 1
        return (poz_x, poz_y)


class Field():
    '''
    class Field
    have functions:
        create_unvisible_field - create unvisible field - field that players
        dont know
        create_visible_ships - create visible ships - field that players know
        and it is empty in some case
    '''
    def __init__(self):
        '''
        represent the class
        '''
        self.__ships = list()

    def create_unvisible_field(self):
        """
            make field for game with 10x10 cellebe
            players dont know it
            :return: list
            """
        import random
        field = list()
        all_format = ['horisontal', 'vertical']
        for x in range(0, 10):
            field.append(list())
            for y in range(0, 10):
                field[x].append('O')
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
                            if field[poz_y - 1][poz_x + j] == 'O':
                                k += 1
                        except:
                            k += 1
                        try:
                            if field[poz_y][poz_x + j] == 'O':
                                k += 1
                        except:
                            k += 1
                        try:
                            if field[poz_y + 1][poz_x + j] == 'O':
                                k += 1
                        except:
                            k += 1
                else:
                    for j in range(-1, lenght_ship + 1, +1):
                        try:
                            if field[poz_y + j][poz_x - 1] == 'O':
                                k += 1
                        except:
                            k += 1
                        try:
                            if field[poz_y + j][poz_x] == 'O':
                                k += 1
                        except:
                            k += 1
                        try:
                            if field[poz_y + j][poz_x + 1] == 'O':
                                k += 1
                        except:
                            k += 1
                if k == place:
                    count_ship += 1
                    for z in range(0, lenght_ship):
                        if format == 'horisontal':
                            field[poz_y][poz_x + z] = 'X'
                        else:
                            field[poz_y + z][poz_x] = 'X'
        return field

    def create_visible_ships(self):
        '''
        create visible for players field
        :return: list
        '''
        field = []
        for x in range(0, 10):
            field.append(list())
            for y in range(0, 10):
                field[x].append('O')
        return field


class Ship():
    '''
    i didnt use this class so i dont write anything in this class
    but it represent class of ship
    '''
    def __init__(self, bow, horisontal):
        '''
        represent the class
        :param bow: tuple
        :param horisontal: bool
        '''
        self.bow = bow
        self.horisontal = horisontal
        self.__lenght = 0
        self.__hit = bool

    def shoot_at(self, tuple):
        pass

if __name__ == "__main__":
    game = Game()
    game.run()
