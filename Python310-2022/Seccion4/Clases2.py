class Clase2():
    def __init__(self, num):
        self.num = num

    def comparar(self):
        if self.num > 0:
            print(self.num, 'es positivo.')
        elif self.num < 0:
            print(self.num, 'es negativo')
        elif self.num == 0:
            print('es cero')

    def repeat(self):
        for x in range(self.num):
            print("Hola mundo")


objeto = Clase2(5)

objeto.repeat()
objeto.comparar()