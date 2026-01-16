
class Player():
    def __init__(self, name=None, name_2=None, age=None):
        self.player = {
        "Ваше имя": name,
        "Ваш позывной": name_2,
        "Возраст":age,
        "Здоровье": 100,
        "Броня": 0}

    def registr_persa(self, a=None, b=None, c=None):
        print("Давайте сделаем всё по вашему вкусу!")
        self.a = input(str("Введите имя персонажа: "))
        self.b = input(str("Введите ваш позывной: "))
        self.c = int(input("Введите ваш возраст(от 18): "))
        return
    
    def print_player(self):
        for key, value in self.player.items():
            print(f"{key}: {value}")
        # print(self.player)
        return
        

persona = Player()
persona.registr_persa()
persona.print_player()

#Я уже заебался эту хуйню писать, утром буду фиксить и переделывать