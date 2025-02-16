import random
import time


class Game():
    def __init__(self):
        self.location = None
        self.bls = int(100) #speed of cultivation
        self.cue = int(0) # cultivation *points*
        self.ct = int(0) #time picked to train
        self.rea =int(1) #cultivation realm in number
        self.rsn = int(1) #cultivation lvl in a realm
        self.step = "Qi Gathering" # realm name
        self.cr = 100
        self.acr = int(100)
        self.psc = None #part of a sect
        self.sfr_HSS = int(0) #relation to Heavenly Sword Sect
        self.sfr_DBS = int(0) #same Demonic
        self.sfr_MLS = int(0) # Lotus
        self.rwsi = int(0) #the relation with the sect you are currently in
        self.otu = int(0) #if you reach 100 relations goes to 1 to stop infinite gain
        self.rw25 = int(0)
        self.rw50 = int(0)
        self.rw100 = int(0)


    def sects(self):
        if self.psc != None:
            if self.otu == 1:
                print("You reached max relations with your sect")
                game.control()
            ri = random.randrange(5,20)
            self.rwsi += ri
            print(f"You were able to improve your relation with {self.psc} to {self.rwsi}")
            if 1 <= self.rwsi < 25:
                print(f"If you reach 25 relations with {self.psc} you will be able to reach a new cultivation level")
            elif 25 <= self.rwsi < 50:
                if self.rw25 == 1:
                    print("If you are able to reach 50 relations a wise elder will teach you")
                else:
                    print("Congratulation you reached relations up to 25."
                          " You are getting toughed by a new elder and you try to reach a new cultivation level")
                    self.rw25 = 1

                    if self.rsn == 9:
                        print(f"As you are currently in the peek of {self.step}"
                              f" the elder was not able to help you break through but you got 1000 cultivation xp")
                        self.cue += 1000
                    else:
                        self.rea += 1
                        self.rsn += 1
                        print("You were able to reach a new cultivation level")
            elif 50 <= self.rwsi <100:
                if self.rw50 == 1:
                    print("If you reach 100 relations the sect master will teach you personally")
                else:
                    print("Fabulous you reached 50 relations."
                          " A wise elder guided you on your way and you broke through 2 cultivation levels.")
                    self.rw50 = 1
                    if self.rsn >= 8:
                        print(f"As you are currently in the {self.rsn} of {self.step}"
                              f" the elder was not able to help you break through but you got 2500 cultivation xp")
                        self.cue += 2500
                    else:
                        self.rea += 2
                        self.rsn += 2
            elif self.rwsi >= 100:
                if self.rw100 ==1:
                    print("The sect master already guided you")
                else:
                    print(f"Magnificent you reached 100 relations with the {self.psc}."
                          f"The sect master taught you and you were able to reach the peak in the {self.step} realm.")
                    nfm = 9 - self.rsn
                    self.rsn += nfm
                    self.rea += nfm
                    self.rw100 = 1
                    if nfm == 0:
                        print("You are already at the peak "
                              "but the sect master was able to teach you so much that now you can break through on your own")
                        self.cue += self.acr

                    self.otu = 1

            game.control()
        nsc = ["1 Heavenly Sword Sect","2 Demonic Blood Sect","3 Mystic Lotus Sect"] #names of the sects
        print("")
        for sect in nsc:
            print(sect)
        c = int(input("Choice:"))
        if c == 1:
            self.psc = "Heavenly Sword Sect"
            rws = self.sfr_HSS
        elif c == 2:
            self.psc = "Demonic Blood Sect"
            rws = self.sfr_DBS
        elif c == 3:
            self.psc = "Mystic Lotus Sect"
            rws = self.sfr_MLS
        print(f"You joined {self.psc}")
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
            print("")
            print("What do you want to do?")
            print("")
            print("1 Visit a place")
            print("2 let time pass")
            print("3 try to reach a new realm")
            if self.psc == None:
                print("4 join a sect")
            elif self.otu < 1:
                print(f"4 Improve relations with {self.psc}")
            print("")
            print(f"Your cultivation is {self.rsn} in the {self.step} realm")
            print(f"Cultivation Xp: {self.cue}")
            print(f"required for next level: {self.acr}")
            d = int(input("Choice:"))

            if d == 1:
                print("")
                print("You can visit:")
                print("")
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
            elif d == 4:
                game.sects()
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