import time


class Game():
    def __init__(self):
        self.location = None
        self.bls = int(100) #speed of cultivation
        self.cue = int(0) # cultivation *points*
        self.ct = int(0) #time picked to train
        self.rea =int(1) #cultivation realm in number
        self.rsn = int(1) #cultivation lvl in a realm
        self.step = None
        self.cr = 100
        self.acr = int(100)
        self.psc = None #part of a sect
        self.sfr_HSS = int(0) #relation to Heavenly Sword Sect
        self.sfr_DBS = int(0) #same Demonic
        self.sfr_MLS = int(0) # Lotus


    def sects(self):
        nsc = ["Heavenly Sword Sect","Demonic Blood Sect","Mystic Lotus Sect"] #names of the sects
        pass
    def realms(self):
        acr = self.cr*self.rea #required
        self.acr = acr
        if self.cue >= acr:
            self.rsn += 1
            self.rea += 1
            self.cue -= acr
            if 1 <= self.rea <= 9:
                self.step = "Qi Gathering"
            elif 10 <= self.rea <= 18:
                self.step = "Foundation Establishment"
            elif 19 <= self.rea <= 27:
                self.step = "Core Formation"
            elif 28 <= self.rea <= 36:
                self.step = "Nascent Soul"
            elif 37 <= self.rea <= 45:
                self.step = "Soul Formation"
            elif 46 <= self.rea <= 54:
                self.step = "Void Refinement"
            if self.rsn == 10:
                print("You advance to the next realm")
                self.rsn = 1
            print(f"Your  cultivation increased and reached the {self.rsn} of {self.step}")
        else: print("You do not have enough Xp")

    def places(self):
        village = 10
        mine = 30
        sect_mid = 200
        godly_artifact = 1000
        return village,mine,sect_mid,godly_artifact

    def control(self):
        q,w,e,r = game.places()
        while True:
            acr = self.cr * self.rea # required
            self.acr = acr
            print("What do you want to do?")
            print("")
            print("1 Visit a place")
            print("2 let time pass")
            print("3 try to reach a new realm")
            print("")
            print(f"Cultivation Xp: {self.cue}")
            print(f"required for next level: {self.acr}")
            d = int(input("Choice:"))

            if d == 1:
                print("You can visit")
                print("1 the village")
                print("2 the mine")
                print("3 sect middle")
                print("4 a goldy artifact")
                print("5 back")
                c = int(input("Choice:"))
                if c == 1:
                    self.location = "village"
                    self.bls += q

                elif c == 2:
                    self.location = "mine"
                    self.bls += w
                elif c == 3:
                    self.location = "sect middle"
                    self.bls += e
                elif c == 4:
                    self.location = "a godly artifact"
                    self.bls += r
                elif c == 5:
                    game.control()
            elif d == 2:
                print("How long do you want time to pass?")
                print("")
                print("10 days")
                print("50 days")
                print("100 days")
                z = int(input("Choice:"))
                if z == 1:
                    self.ct = 10
                    game.time()
                elif z == 2:
                    self.ct = 50
                    game.time()
                elif z == 3:
                    self.ct = 100
                    game.time()
            elif d == 3:
                game.realms()

    def time(self):

        print(self.ct)

        day = 1
        while self.ct >0:
            time.sleep(0.5)
            day += 1
            self.ct -= 1
            print(self.ct)
            self.cue += self.bls
            print(self.cue)





game = Game()
game.control()
