import random
class Card:
    def __init__(self, user):
        self.user = user
        self.number = sorted(random.sample(range(1, 91), 15))
        self.card = [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]
        count = 0
        j = 0
        for i in self.card:
            while count < 5:
                i.append(self.number[j])
                count += 1
                j += 1
            count = 0
            random.shuffle(i)
        count = 0

    def __str__(self):
        pull_card = f'{self.user}: \n' + '\n'.join(['   '.join([str(i) for i in a]) for a in self.card]) + '\n'

        return pull_card

    def __getitem__(self, index):
        return self.number[index]



class Game():
    def __init__(self, name_user, name_computer):
        self.name_user = name_user
        self.name_computer = name_computer


    def game(self):
        a = [i for i in range(1, 91)]
        total = 90
        score_computer = 15
        score_user = 15
        while total > 0:
            self.result = random.choice(a)
            print('бочонок с номером ', self.result)
            answer_person = int(input('введите либо 0 если нет или 1 если есть это число:'))
            if self.result in self.name_computer.number:
                # self.name_computer[self.name_computer.number.index(self.result)] = 'x'
                score_computer -= 1
                print('у компьютора осталось ', score_computer, 'чисел')
                if score_computer == 0:
                    print('победил компьютер')
                    break
            print(self.name_computer)
            total -= 1

            if answer_person == 1:
                if self.result in self.name_user.number:
                    a.remove(self.result)
                    self.name_user.number.remove(self.result)
                    score_user -= 1
                    print('у вас осталось ', score_user, 'чисел')
                    if score_user == 0:
                        print('вы победили')
                        break

                else:
                    print('вы проиграли')
                    break
            if answer_person == 0:
                if self.result in self.name_user.number:
                    print('вы проиграли')
                    break
                else:
                    a.remove(self.result)
            print(self.name_user)


computer = Card('КОМПЬЮТЕР')
person = Card('ПОЛЬЗОВАТЕЛЬ')
print(computer)
print(person)
game = Game(person, computer)
game.game()
