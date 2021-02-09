import core
from TP2.Bille import Bille
from TP2.Creep import Creep
from TP2.Player import Player

#Variables globales
player1 = None
creep1 = []
bille1 = Bille()


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    global player1 , creep1
    player1 = Player()

    for i in range(0, 1000):
        creep1.append(Creep())



    print("Setup END-----------")

def run():
    print("Run")

    for c in creep1:
        c.afficher(core)

    player1.afficher(core)
    if core.getMouseLeftClick() is not None:
       player1.deplacer(core.getMouseLeftClick())





if __name__ == '__main__':


    core.main(setup, run)