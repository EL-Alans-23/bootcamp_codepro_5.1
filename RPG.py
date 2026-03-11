
class personaje():
    
    def __init__(self,nombre,ataque,vida):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida

    def atributos (self):
        print(self.nombre )
        print("vida:",self.vida)
        print("ataque:",self.ataque)
    
    def morir (self,enemigo):
        if self.vida <= 0 or enemigo.vida <= 0:
            print('esta muerto')
        else:
            print('esta vivo')
    
    

class mago(personaje):
    def __init__(self, nombre, ataque, vida,inteligencia):
        super().__init__(nombre, ataque, vida)
        self.inteligencia = inteligencia
    
    def atributos(self):
        print(self.nombre )
        print("vida:",self.vida)
        print("ataque:",self.ataque)
        print('inteligencia:',self.inteligencia)

    def poder_aumentado(self):
        return self.ataque * self.inteligencia

    def atacar (self,enemigo):
        enemigo.vida -= self.poder_aumentado()

class barbaro(personaje):
    def __init__(self, nombre, ataque, vida,espada):
        super().__init__(nombre, ataque, vida)
        self.espada = espada 

    def poder_aumentado(self):
        return  self.ataque * self.espada
    
    def atacar (self,enemigo):
        enemigo.vida -= self.poder_aumentado()
    
    def atributos(self):
        print(self.nombre )
        print("vida:",self.vida)
        print("ataque:",self.ataque)
        print('espada:',self.espada)

class arquero(personaje):
    def __init__(self, nombre, ataque,vida,arco):
        super().__init__(nombre, ataque, vida)
        self.arco = arco 

    def poder_aumentado(self):
        return  self.ataque * self.arco
    
    def atacar (self,enemigo):
        enemigo.vida -= self.poder_aumentado()
    
    def atributos(self):
        print(self.nombre )
        print("vida:",self.vida)
        print("ataque:",self.ataque)
        print('espada:',self.arco)

class tablero():
    def morir (self,enemigo):
        if self.vida <= 0 or enemigo.vida <= 0:
            print('esta muerto')
        else:
            print('esta vivo')

    def turnos(self,jugador1,jugador2):
        intentos = 0
        while True:
            print(f"Los intetos es {intentos}")
            jugador1.atacar(jugador2)
            jugador2.atacar(jugador1)

            jugador1.atributos()
            print("")
            jugador2.atributos()
            print("")
            intentos = intentos + 1

            if jugador1.vida <= 0 :
                jugador1.morir(jugador2)
                print(f'El {jugador1.nombre} ha muerto')
                break

            elif jugador2.vida <= 0:
                jugador2.morir(jugador1)
                print(f'El {jugador2.nombre} ha muerto')
                break


jugador1 = mago('mago',3,60,5)
jugador2 = barbaro('barbaro',5,50,2)
juagdor3 = arquero('arquero',7,20,4)
mapa = tablero()
mapa.turnos(jugador1,jugador2)