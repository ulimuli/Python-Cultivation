import random
import sys
import time
import tkinter as tk
from Map import Map


class Game():
    def __init__(self):
        self.location = None
        self.bls = int(100)  #speed of cultivation percent
        self.cue = int(0)  # cultivation *points*
        self.ct = int(0)  #time picked to train
        self.rea = int(1)  #cultivation realm in number
        self.rsn = int(1)  #cultivation lvl in a realm
        self.step = "Qi Gathering"  # realm name
        self.cr = 100
        self.acr = int(100)
        self.psc = None  #part of a sect
        self.sfr_HSS = int(0)  #relation to Heavenly Sword Sect
        self.sfr_DBS = int(0)  #same Demonic
        self.sfr_MLS = int(0)  # Lotus
        self.sfr_ALS = int(0)  # Azure Cloud Sect
        self.rwsi = int(0)  #the relation with the sect you are currently in
        self.otu = int(0)  #if you reach 100 relations goes to 1 to stop infinite gain
        self.rw25 = int(0)
        self.rw50 = int(0)
        self.rw100 = int(0)
        self.gs = None  #gender
        self.nm = None  #name
        self.cp = int(0)  #combat power
        self.sps = int(10)  #size of the spirit sea
        self.qq = int(1)  #quality of Qi
        self.pc = int(0)  # percent of finishing the Core
        self.ins = int(0)  # size of the nascent soul
        self.exd = int(0)  #domain size
        self.dac = int(0)  #percent of connection with dao
        self.uip = None
        self.pr = 0
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        self.bt4 = 0
        self.sr = 0  #sect rank
        self.rp = int(0)  #reputation in sects
        self.starting_map_token = 1
        self.day = int(1)
        self.month = int(1)
        self.year = int(103)
        self.btc = int(5)  #base travel cost time
        self.dct = int(0)  #daily cultivation time
        self.place = None  #player location
        self.frt = int(24)  # daily free time

    def del_butn(self):
        try:
            self.butt1.destroy()
            self.butt2.destroy()
            self.butt3.destroy()
            self.butt4.destroy()
            print("Del_Button just works")
        except:
            print("OK del-button seems to do nothing")

    def create_butn(self):
        pass

    def uin(self):
        self.uip = self.inp.get()
        self.inp.delete(0, tk.END)
        if self.pr == 0:
            self.pr += 1
            game.start()

    def combat(self):
        lwp = self.cp - 50
        hwp = self.cp + 50
        self.output.insert(tk.END, "Who do you want to fight with?\n")
        self.output.insert(tk.END, "\n")
        nl = ["Mo Tianxie", "Xie Wuhen", "Bai Mingsheng", "Guo Zhenhai",
              "Hei Wulian", "Zhao Tiansha", "Feng Luoxian", "Yan Wujian", "Du Chengkong", "Luo Hengzhi"]  #list bad guys
        e1 = random.randrange(lwp, hwp)
        e2 = random.randrange(lwp, hwp)
        e3 = random.randrange(lwp, hwp)
        e4 = random.randrange(lwp, hwp)

        self.output.insert(tk.END, f"1 {random.choice(nl)} Combat Power: {e1}\n")
        self.output.insert(tk.END, f"2 {random.choice(nl)} Combat Power: {e2}\n")
        self.output.insert(tk.END, f"3 {random.choice(nl)} Combat Power: {e3}\n")
        self.output.insert(tk.END, f"4 {random.choice(nl)} Combat Power: {e4}\n")

        self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=lambda: game.fdt1(e1))
        self.butt1.place(x=559, y=340)

        self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=lambda: game.fdt2(e2))
        self.butt2.place(x=629, y=340)

        self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=lambda: game.fdt3(e3))
        self.butt3.place(x=559, y=380)

        self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=lambda: game.fdt4(e4))
        self.butt4.place(x=629, y=380)

        self.output.insert(tk.END, "\n")
        self.output.yview(tk.END)

    def fdt1(self, e1):
        if e1 < self.cp:
            self.output.insert(tk.END, "You won against your enemy\n")
        else:
            self.output.insert(tk.END, "You lost but you were able to survive\n")
        self.bt1 += 1

        for bt in [self.butt1, self.butt2, self.butt3, self.butt4]:
            try:
                bt.destroy()
            except:
                pass

        self.output.yview(tk.END)

    def fdt2(self, e2):
        if e2 < self.cp:
            self.output.insert(tk.END, "You won against your enemy\n")
        else:
            self.output.insert(tk.END, "You lost but you were able to survive\n")
        self.bt2 += 1
        for bt in [self.butt1, self.butt2, self.butt3, self.butt4]:
            try:
                bt.destroy()
            except:
                pass
        self.output.yview(tk.END)

    def fdt3(self, e3):
        if e3 < self.cp:
            self.output.insert(tk.END, "You won against your enemy\n")
        else:
            self.output.insert(tk.END, "You lost but you were able to survive\n")
        self.bt3 += 1

        for bt in [self.butt1, self.butt2, self.butt3, self.butt4]:
            try:
                bt.destroy()
            except:
                pass
        self.output.yview(tk.END)

    def fdt4(self, e4):
        if e4 < self.cp:
            self.output.insert(tk.END, "You won against your enemy\n")
        else:
            self.output.insert(tk.END, "You lost but you were able to survive\n")
        self.bt4 += 1
        for bt in [self.butt1, self.butt2, self.butt3, self.butt4]:
            try:
                bt.destroy()
            except:
                pass
        self.output.yview(tk.END)

    def window(self):
        game.del_butn()
        self.root = tk.Tk()
        self.root.geometry("700x600")
        self.root.title("Python-Cultivation")
        self.cp = self.rea * 100

        self.output = tk.Text(self.root, height=14, width=79)
        self.output.place(x=0, y=0)

        self.map = tk.Text(self.root, height=18, width=79)
        self.map.place(x=0, y=200)

        self.inp = tk.Entry(self.root, width=61)
        self.inp.place(x=0, y=460)

        self.but1 = tk.Button(self.root, height=2, width=4, text="Travel", command=lambda: game.travel(1, None))
        self.but1.place(x=559, y=0)

        self.but2 = tk.Button(self.root, height=2, width=4, text="Sect", command=lambda: game.sects(0))
        self.but2.place(x=629, y=0)

        self.but3 = tk.Button(self.root, height=2, width=4, text="Fight", command=game.combat)
        self.but3.place(x=559, y=40)

        self.but4 = tk.Button(self.root, height=2, width=4, text="Time", command=lambda: game.time_manager())
        self.but4.place(x=629, y=40)

        self.but5 = tk.Button(self.root, height=2, width=4, text="Cultivate",
                              command=lambda: game.cultivate(0, 0, None))
        self.but5.place(x=559, y=80)

        self.but6 = tk.Button(self.root, height=2, width=4, text="Ascension", command=game.realms)
        self.but6.place(x=629, y=80)

        #self.but7 = tk.Button(self.root,height=2,width=4,text="Yes",command=game.yes)
        #self.but7.place(x=559,y=340)

        #self.but8 = tk.Button(self.root,height=2,width=4,text="No",command=game.no)
        #self.but8.place(x=629,y=340)

        self.but9 = tk.Button(self.root, height=2, width=8, text="Enter", command=game.uin)
        self.but9.place(x=559, y=450)

        self.buttime1 = tk.Button(self.root, height=2, width=5, text="1 Second", command="")
        self.buttime1.place(x=30, y=490)

        self.buttime2 = tk.Button(self.root, height=2, width=5, text="5 Seconds", command="")
        self.buttime2.place(x=110, y=490)

        self.buttime3 = tk.Button(self.root, height=2, width=5, text="30 Seconds", command="")
        self.buttime3.place(x=190, y=490)

        self.buttime4 = tk.Button(self.root, height=2, width=5, text="1 Minute", command="")
        self.buttime4.place(x=270, y=490)

        self.buttime5 = tk.Button(self.root, height=2, width=5, text="5 Minutes", command="")
        self.buttime5.place(x=350, y=490)

        self.buttime6 = tk.Button(self.root, height=2, width=5, text="30 Minutes", command="")
        self.buttime6.place(x=430, y=490)

        self.buttime7 = tk.Button(self.root, height=2, width=5, text="1 Hour", command="")
        self.buttime7.place(x=510, y=490)

        self.buttime8 = tk.Button(self.root, height=2, width=5, text="5 Hours", command="")
        self.buttime8.place(x=590, y=490)

        self.buttime9 = tk.Button(self.root, height=2, width=5, text="1 day", command=lambda: game.time(1))
        self.buttime9.place(x=70, y=540)

        self.buttime10 = tk.Button(self.root, height=2, width=5, text="5 days", command=lambda: game.time(5))
        self.buttime10.place(x=150, y=540)

        self.buttime11 = tk.Button(self.root, height=2, width=5, text="1 Month", command=lambda: game.time(30))
        self.buttime11.place(x=230, y=540)

        self.buttime12 = tk.Button(self.root, height=2, width=5, text="6 Months", command=lambda: game.time(30 * 6))
        self.buttime12.place(x=310, y=540)

        self.buttime13 = tk.Button(self.root, height=2, width=5, text="1 Year", command=lambda: game.time(30 * 12))
        self.buttime13.place(x=390, y=540)

        self.buttime14 = tk.Button(self.root, height=2, width=5, text="10 Years",
                                   command=lambda: game.time(30 * 12 * 10))
        self.buttime14.place(x=470, y=540)

        self.buttime15 = tk.Button(self.root, height=2, width=5, text="50 Years",
                                   command=lambda: game.time(30 * 12 * 50))
        self.buttime15.place(x=550, y=540)

        self.cpl = tk.Label(self.root, height=2, width=15, text=f"Combat Power:\n {self.cp}")
        self.cpl.place(x=559, y=120)

        self.drc = tk.Label(self.root, height=2, width=15, text=f"{self.rsn} level of \n{self.step} realm")
        self.drc.place(x=559, y=160)

        self.kph = tk.Label(self.root, height=2, width=15, text=f"Cultivation Xp: \n{self.cue}")
        self.kph.place(x=559, y=205)

        self.xpn = tk.Label(self.root, height=2, width=15, text=f"XP for next level:\n {self.acr}")
        self.xpn.place(x=559, y=250)

        self.date = tk.Label(self.root, height=2, width=15, text=f"{self.day}.{self.month}.{self.year} ")
        self.date.place(x=559, y=290)

        #travel code
        self.root.bind_all("<w>", lambda e: self.travel(1, "up"))
        self.root.bind_all("<a>", lambda e: self.travel(1, "left"))
        self.root.bind_all("<s>", lambda e: self.travel(1, "down"))
        self.root.bind_all("<d>", lambda e: self.travel(1, "right"))

        if self.starting_map_token == 1:
            game.travel(start_call=self.starting_map_token)

        self.output.insert(tk.END, "Welcome to Python-Cultivation!\n")
        self.output.insert(tk.END, "\n")
        self.output.insert(tk.END, "You open your eyes to a world with vast towering mountains,"
                                   " their peaks covered in mist, stretch endlessly into the heavens."
                                   " The air is filled with Qi, an unseen force that allows you to cultivate.\n")
        self.output.insert(tk.END, "\n")
        self.output.insert(tk.END, "What is your name in this vast world\n")

        self.root.mainloop()

    def end(self):
        pass

    def yes(self):
        self.output.insert(tk.END, "Yes\n")

    def no(self):
        self.output.insert(tk.END, "No\n")

    def start(self):

        self.nm = self.uip
        self.uip = None

        self.output.insert(tk.END, "What is your gender?\n")
        self.man = tk.Button(self.root, height=2, width=4, text="Man", command=game.gedm)
        self.man.place(x=559, y=380)

        self.women = tk.Button(self.root, height=2, width=4, text="Women", command=game.gedw)
        self.women.place(x=629, y=380)

    def gedm(self):
        self.gs = "Man"
        self.output.insert(tk.END, f"You are {self.nm} and you are a {self.gs}\n")
        self.man.destroy()
        self.women.destroy()
        self.output.insert(tk.END, "From now on you can do whatever you want\n")

    def gedw(self):
        self.gs = "Women"
        self.output.insert(tk.END, f"You are {self.nm} and you are a {self.gs}\n")
        self.women.destroy()
        self.man.destroy()
        self.output.insert(tk.END, "From now on you can do whatever you want\n")

    def sects(self, c):
        game.del_butn()

        if self.psc == None:

            nsc = ["1 Heavenly Sword Sect\n", "2 Demonic Blood Sect\n", "3 Mystic Lotus Sect\n",
                   "4 Azure Cloud Sect\n"]  #names of the sects
            self.output.insert(tk.END, "")
            for sect in nsc:
                self.output.insert(tk.END, sect)
            self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=game.sdt1)
            self.butt1.place(x=559, y=340)
            self.bt1 = 1

            self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=game.sdt2)
            self.butt2.place(x=629, y=340)
            self.bt2 = 1

            self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=game.sdt3)
            self.butt3.place(x=559, y=380)
            self.bt3 = 1

            self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=game.sdt4)
            self.butt4.place(x=629, y=380)
            self.bt4 = 1

        else:
            self.output.insert(tk.END, "Do you want to (1) improve relations with your sect or "
                                       "(2) do you want to increase your rank in the sect? \n")
            self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=lambda: game.sects(1))
            self.butt1.place(x=559, y=340)
            self.bt1 = 1

            self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=lambda: game.sects(2))
            self.butt2.place(x=629, y=340)
            self.bt2 = 1
            self.output.yview(tk.END)

            if c == 2:
                game.del_butn()
                if self.sr == 0:
                    pass
                elif self.sr == 1:
                    self.output.insert(tk.END, "You are currently a outer disciple"
                                               " but you can improve your rank in the sect, by doing:\n")
                    self.output.insert(tk.END, "\n")
                    self.output.insert(tk.END, "1 Help with some regular tasks\n")
                    self.output.insert(tk.END, "2 do easy sect missions\n")
                    self.output.insert(tk.END, "3 Gather firewood and water for the sect’s communal areas\n")
                    self.output.insert(tk.END, "4 Gather herbs or resources for the sect\n")

                    self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=lambda: game.sri(1))
                    self.butt1.place(x=559, y=340)
                    self.bt1 = 1

                    self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=lambda: game.sri(1))
                    self.butt2.place(x=629, y=340)
                    self.bt2 = 1

                    self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=lambda: game.sri(1))
                    self.butt3.place(x=559, y=380)
                    self.bt3 = 1

                    self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=lambda: game.sri(1))
                    self.butt4.place(x=629, y=380)
                    self.bt4 = 1

                elif self.sr == 2:
                    self.output.insert(tk.END, "You are currently a inner disciple"
                                               " but you can improve your rank in the sect, by doing:\n")
                    self.output.insert(tk.END, "\n")
                    self.output.insert(tk.END, "1 Scout potential outer disciples for the sect\n")
                    self.output.insert(tk.END, "2 Assist in managing and training outer disciples\n")
                    self.output.insert(tk.END, "3 Guard the sect entrance or patrol the outer grounds\n")
                    self.output.insert(tk.END, "4 Assist in setting up and maintaining training grounds\n")

                    self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=lambda: game.sri(2))
                    self.butt1.place(x=559, y=340)
                    self.bt1 = 1

                    self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=lambda: game.sri(2))
                    self.butt2.place(x=629, y=340)
                    self.bt2 = 1

                    self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=lambda: game.sri(2))
                    self.butt3.place(x=559, y=380)
                    self.bt3 = 1

                    self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=lambda: game.sri(2))
                    self.butt4.place(x=629, y=380)
                    self.bt4 = 1

                elif self.sr == 3:
                    self.output.insert(tk.END, "You are currently a core disciple"
                                               " but you can improve your rank in the sect, by doing:\n")
                    self.output.insert(tk.END, "\n")
                    self.output.insert(tk.END, "1 Train and mentor inner disciples\n")
                    self.output.insert(tk.END, "2 Guard the sect treasury \n")
                    self.output.insert(tk.END, "3 help the elders\n")
                    self.output.insert(tk.END, "4 help supervising training fights\n")

                    self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=lambda: game.sri(3))
                    self.butt1.place(x=559, y=340)
                    self.bt1 = 1

                    self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=lambda: game.sri(3))
                    self.butt2.place(x=629, y=340)
                    self.bt2 = 1

                    self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=lambda: game.sri(3))
                    self.butt3.place(x=559, y=380)
                    self.bt3 = 1

                    self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=lambda: game.sri(3))
                    self.butt4.place(x=629, y=380)
                    self.bt4 = 1

                #elif self.sr == 4:
                #   self.output.insert(tk.END,"You are currently a elder"
                #                            " but you can improve your rank in the sect, by doing:\n")
                #elif self.sr == 5:
                #   self.output.insert(tk.END,"You are currently the sect leader\n")
            elif c == 1:
                game.del_butn()
                if self.psc != None:
                    if self.otu == 1:
                        self.output.insert(tk.END, "You already reached max relations with your sect\n")
                    ri = random.randrange(5, 20)
                    self.rwsi += ri
                    self.output.insert(tk.END,
                                       f"You were able to improve your relation with {self.psc} to {self.rwsi}\n")
                    if 1 <= self.rwsi < 25:
                        self.output.insert(tk.END,
                                           f"If you reach 25 relations with {self.psc} you will be able to reach a new cultivation level\n")
                    elif 25 <= self.rwsi < 50:
                        if self.rw25 == 1:
                            self.output.insert(tk.END,
                                               "If you are able to reach 50 relations a wise elder will teach you\n")
                        else:
                            self.output.insert(tk.END, "Congratulation you reached relations up to 25.\n"
                                                       " You are getting toughed by a new elder and you try to reach a new cultivation level\n")
                            self.rw25 = 1

                            if self.rsn == 9:
                                self.output.insert(tk.END, f"As you are currently in the peek of {self.step}\n"
                                                           f" the elder was not able to help you break through but you got 1000 cultivation xp\n")
                                self.cue += 1000
                                self.kph.config(text=f"Cultivation Xp: \n{self.cue}")
                            else:
                                self.rea += 1
                                self.rsn += 1
                                self.output.insert(tk.END, "You were able to reach a new cultivation level\n")
                                self.drc.config(text=f"{self.rsn} level of \n{self.step} realm")
                    elif 50 <= self.rwsi < 100:
                        if self.rw50 == 1:
                            self.output.insert(tk.END,
                                               "If you reach 100 relations the sect master will teach you personally\n")
                        else:
                            self.output.insert(tk.END, "Fabulous you reached 50 relations.\n"
                                                       " A wise elder guided you on your way and you broke through 2 cultivation levels.\n")
                            self.rw50 = 1
                            if self.rsn >= 8:
                                self.output.insert(tk.END, f"As you are currently in the {self.rsn} of {self.step}\n"
                                                           f" the elder was not able to help you break through but you got 2500 cultivation xp")
                                self.cue += 2500
                                self.kph.config(text=f"Cultivation Xp: \n{self.cue}")
                            else:
                                self.rea += 2
                                self.rsn += 2
                                self.drc.config(text=f"{self.rsn} level of \n{self.step} realm")
                    elif self.rwsi >= 100:
                        if self.rw100 == 1:
                            self.output.insert(tk.END, "The sect master already guided you\n")
                        else:
                            self.output.insert(tk.END, f"Magnificent you reached 100 relations with the {self.psc}.\n"
                                                       f"The sect master taught you and you were able to reach the peak in the {self.step} realm.")
                            nfm = 9 - self.rsn
                            self.rsn += nfm
                            self.rea += nfm
                            self.drc.config(text=f"{self.rsn} level of \n{self.step} realm")
                            self.rw100 = 1
                            if nfm == 0:
                                self.output.insert(tk.END, "You are already at the peak "
                                                           "but the sect master was able to teach you so much that now you can break through on your own\n")
                                self.cue += self.acr

                            self.otu = 1

        self.cp = self.rea * 100
        self.cpl.config(text=f"Combat Power:\n {self.cp}")
        self.kph.config(text=f"Cultivation Xp: \n{self.cue}")
        self.output.yview(tk.END)

    def sri(self, cr):
        game.del_butn()
        self.rp += 10
        if cr == 1:
            nr = "Inner disciple"
        elif cr == 2:
            nr = "Core disciple"
        elif cr == 3:
            nr = "Sect Elder"
        elif cr == 4:
            nr = "Sect Leader"
        if self.rp == 100:
            self.output.insert(tk.END, f"You reached the rank of {nr}\n")
            self.sr = 2
        elif self.rp == 200:
            self.output.insert(tk.END, f"You reached the rank of {nr}\n")
            self.sr = 3
        elif self.rp == 300:
            self.output.insert(tk.END, f"You reached the rank of {nr}\n")
        self.output.insert(tk.END, f"You completed your task and are now closer to reach the rank of {nr}\n")

    def sdt1(self):
        self.psc = "Heavenly Sword Sect"
        rws = self.sfr_HSS
        self.output.insert(tk.END, f"You joined {self.psc} as a outer disciple\n")
        self.sr = 1
        self.bt1 = 1
        game.del_butn()
        self.output.yview(tk.END)

    def sdt2(self):
        self.psc = "Demonic Blood Sect"
        rws = self.sfr_DBS
        self.output.insert(tk.END, f"You joined {self.psc} as a outer disciple\n")
        self.sr = 1
        self.bt2 = 1
        game.del_butn()
        self.output.yview(tk.END)

    def sdt3(self):
        self.psc = "Mystic Lotus Sect"
        rws = self.sfr_MLS

        self.output.insert(tk.END, f"You joined {self.psc} as a outer disciple\n")
        self.sr = 1
        self.bt3 = 1
        game.del_butn()
        self.output.yview(tk.END)

    def sdt4(self):
        self.psc = "Azure Cloud Sect"
        rws = self.sfr_ALS
        self.output.insert(tk.END, f"You joined {self.psc} as a outer disciple\n")
        self.sr = 1
        self.bt4 = 1
        game.del_butn()
        self.output.yview(tk.END)

    def realms(self):
        game.del_butn()
        if self.cue >= self.acr:
            self.cue -= self.acr
            self.rsn += 1
            self.rea += 1
            self.acr = self.acr * self.rea  # required
            self.xpn.config(text=f"XP for next level:\n {self.acr}")
            self.kph.config(text=f"Cultivation Xp: {self.cue}")
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
                self.output.insert(tk.END, "You advance to the next realm\n")
                self.rsn = 1
            self.output.insert(tk.END, f"Your cultivation increased and reached the {self.rsn} of {self.step}\n")
        else:
            self.output.insert(tk.END, f"You need {self.acr} Xp but you only have {self.cue}\n")
        self.xpn.config(text=f"XP for next level:\n {self.acr}")
        self.cp = self.rea * 100
        self.kph.config(text=f"Cultivation Xp: \n{self.cue}")
        self.drc.config(text=f"{self.rsn} level of \n{self.step} realm")
        self.cpl.config(text=f"Combat Power:\n {self.cp}")
        self.output.yview(tk.END)

    def location(self, pl_loc=None):
        self.output.insert(tk.END, f"As you are in a {self.place} you are able to do:\n")

    def travel(self, t=None, wmove=None, start_call=None):  #this def part was mostly written by ai
        game.del_butn()

        self.map.tag_configure("zero", foreground="green")
        self.map.tag_configure("one", foreground="dark green")
        self.map.tag_configure("two", foreground="gold")
        self.map.tag_configure("three", foreground="white")

        """
        Show map and either:
          - display movement buttons (when wmove is None), or
          - perform the move (when wmove is 'up'/'down'/'left'/'right' or a visit option).
        t is used to control special visit-menu behaviour (original code used t==0).
        """

        # --- Ensure button flag attributes exist (safe checks) ---
        for i in range(1, 5):
            if not hasattr(self, f"bt{i}"):
                setattr(self, f"bt{i}", 0)
            if not hasattr(self, f"butt{i}"):
                setattr(self, f"butt{i}", None)

        # --- Ensure we have a persistent map for the player ---
        if not hasattr(self, "current_map") or getattr(self, "current_map") is None:
            self.current_map = Map()
            self.current_map.load_map()
            print(self.current_map.get_player_terrain())

        # --- Clean up any old buttons to avoid duplicates (safe getattr) ---
        for i in range(1, 5):
            if getattr(self, f"bt{i}", 0) == 1:
                btn = getattr(self, f"butt{i}", None)
                if btn is not None:
                    try:
                        btn.destroy()
                    except Exception:
                        pass
                setattr(self, f"bt{i}", 0)
                setattr(self, f"butt{i}", None)

        if start_call == 1:

            for line in self.current_map.display_map():
                for ch in line:
                    if ch == "0":
                        self.map.insert(tk.END, ch, "zero")
                    elif ch == "1":
                        self.map.insert(tk.END, ch, "one")
                    elif ch == "2":
                        self.map.insert(tk.END, ch, "two")
                    elif ch == "3":
                        self.map.insert(tk.END, ch, "three")
                    else:
                        self.map.insert(tk.END, ch)
                self.map.insert(tk.END, "\n")

            self.starting_map_token = 0
        else:

            # If original caller asked t==0, show visit menu instead of directional buttons.
            if t == 0:
                # destroy directional buttons (we just created them) to show visit options instead
                for i in range(1, 5):
                    if getattr(self, f"bt{i}", 0) == 1:
                        btn = getattr(self, f"butt{i}", None)
                        if btn is not None:
                            try:
                                btn.destroy()
                            except Exception:
                                pass
                        setattr(self, f"bt{i}", 0)
                        setattr(self, f"butt{i}", None)

                self.output.insert(tk.END, "\nYou can visit:\n\n")
                self.output.insert(tk.END, "1 - random Place\n")
                self.output.insert(tk.END, "2 - the village\n")

                # Option 1 and 2 buttons
                self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=self.rdt1)
                self.butt1.place(x=559, y=340)
                self.bt1 = 1

                self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=self.rdt2)
                self.butt2.place(x=629, y=340)
                self.bt2 = 1

                # Option 3 (requires rwsi > 25)
                if getattr(self, "rwsi", 0) > 25:
                    self.output.insert(tk.END, "3 - sect middle\n")
                    self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=self.rdt3)
                    self.butt3.place(x=559, y=380)
                    self.bt3 = 1

                # Option 4 (requires rwsi >= 100)
                if getattr(self, "rwsi", 0) >= 100:
                    self.output.insert(tk.END, "4 - a goldy artifact\n")
                    self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=self.rdt4)
                    self.butt4.place(x=629, y=380)
                    self.bt4 = 1

            # <<-- PLACE THE RETURN HERE so we only exit when we created buttons (no wmove provided) -->
            if wmove is None:
                self.output.yview(tk.END)
                return
        # nothing to do until the player clicks a button

        # If we get here, wmove is not None so perform the move

        # --- If a movement (wmove) was provided, perform it ---
        if wmove is not None:
            move_result = self.current_map.move_player(wmove)

            self.map.delete("1.0", tk.END)
            for line in self.current_map.display_map():
                for ch in line:
                    if ch == "0":
                        self.map.insert(tk.END, ch, "zero")
                    elif ch == "1":
                        self.map.insert(tk.END, ch, "one")
                    elif ch == "2":
                        self.map.insert(tk.END, ch, "two")
                    elif ch == "3":
                        self.map.insert(tk.END, ch, "three")
                    else:
                        self.map.insert(tk.END, ch)
            game.time(5)
            if int(self.current_map.get_player_terrain()) == 0:
                self.output.insert(tk.END, "You traveled for 5 days and arrived in Plains.\n")
                self.place = "Plains"
            elif int(self.current_map.get_player_terrain()) == 1:
                self.output.insert(tk.END, "You traveled for 5 days and arrived in a Forrest.\n")
                self.place = "Forest"
            elif int(self.current_map.get_player_terrain()) == 2:
                self.output.insert(tk.END, "You traveled for 5 days and arrived in a City.\n")
                self.place = "City"
            elif int(self.current_map.get_player_terrain()) == 3:
                self.output.insert(tk.END, "You traveled for 5 days and should not be able to be here.\n")
                self.place = "???"
            try:
                self.current_map.save_map("Main_Map.txt")
            except Exception:
                self.output.insert(tk.END, "Warning: failed to save map.\n")

        self.output.yview(tk.END)

    def rdt1(self):
        self.location = "random Place"
        self.bls += 50
        self.output.insert(tk.END, "You are now at a random place\n")
        self.bt1 = 0
        game.del_butn()
        self.output.yview(tk.END)

    def rdt2(self):
        event = random.random()
        self.location = "Village"
        self.output.insert(tk.END, f"You went to the {self.location}\n")
        self.bt2 = 1
        game.del_butn()
        self.bls += 100
        self.output.yview(tk.END)
        #if event > 0.75:
        #   k = random.random()
        #  if k <= 0.5:
        #     self.output.insert(tk.END,"The village is getting attacked currently do you want to help?\n")
        #   self.output.insert(tk.END,"\n")
        #    print("Yes or No?")
        #  l = input("Choice:")
        # if l == "Yes":
        #    r = random.random()
        #   if r <= 0.5:
        #      "You helped kill the bands and the villager thanked you"
        # else:
        #    print("You were unable to do anything against the bandits, but they let you be")
        #        elif l == "No":
        #           print("You leave the village alone,"
        #                " when you came back 1 hour later the village was in ruin and on fire")
        #     else:
        #        print("Not a valid option,"
        #             " please be careful while writing and also look if you write in caps"), game.control()

        #    elif k > 0.5:
        #       print("The village is currently holding a celebration do you wish to join?")
        #      print("")
        #     print("Yes or No?")
        #    o = input("Choice:")
        #   if o == "Yes":
        #      print("You had much fun with the villagers and celebrated deep into the night")
        # elif o == "No":
        #    print("You ignored the celebration and continue with your work alone")
        #        else:
        #           print("Not a valid option,"
        #                " please be careful while writing and also look if you write in caps"), game.control()
        #else:
        #   print("Nothing is currently happening in the village.")

    def rdt3(self):
        self.location = "sect middle"
        self.output.insert(tk.END, f"You are at the {self.location}\n")
        self.bls += 200
        game.del_butn()
        self.output.yview(tk.END)

    def rdt4(self):
        self.location = "godly artifact"
        self.output.insert(tk.END, f"You are at the {self.location}\n")
        self.bls += 1000
        game.del_butn()
        self.output.yview(tk.END)

    def control(self):
        self.cp = self.rea * 100
        while True:
            acr = self.cr * self.rea  # required
            self.acr = acr
            print("")
            print("What do you want to do?")
            print("")
            print("1 Go to a place")
            print("2 Cultivate")
            print("3 try to break through")
            if self.psc == None:
                print("4 join a sect")
            elif self.otu < 1:
                print(f"4 Improve relations with {self.psc}")
            print("5 fight")
            if self.step == "Qi Gathering":
                print("6 improve Spirit Sea")
                self.cp += self.sps
                ch6 = 1  # just means that the realm is this and is used for the choice thing
            elif self.step == "Foundation Establishment":
                print("6 improve quality of Qi")
                self.cp *= self.qq / 100
                ch6 = 2
            elif self.step == "Core Formation":
                print("6 Condense Core")
                self.cp *= self.pc
                ch6 = 3
            elif self.step == "Nascent Soul":
                print("6 Improve Nascent Soul")
                self.cp += self.ins * 1000
                ch6 = 4
            elif self.step == "Soul Formation":
                print("6 expand your domain")
                self.cp *= self.exd
                ch6 = 5
            elif self.step == "Void Refinement":
                print("6 improve Dao Connection")
                self.cp *= self.dac
                ch6 = 6
            print("")
            print(f"Your cultivation is {self.rsn} in the {self.step} realm")
            print(f"Cultivation Xp: {self.cue}")
            print(f"required for next level: {self.acr}")
            print(f"Your Combat Power is {self.cp}")
            d = int(input("Choice:"))

            if d == 1:
                game.travel()

            elif d == 2:
                print("How long do you want to cultivate?")
                print("")
                print("1 10 days")
                print("2 50 days")
                print("3 100 days")
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
            elif d == 5:
                game.combat()
            elif d == 6:
                sc = random.randrange(10, 50)
                qi = sc / 10
                if ch6 == 1:
                    self.sps += sc
                    print(f"improved your spirit sea by {sc} your spirit sea now has a size of {self.sps}")
                elif ch6 == 2:
                    if self.qq == 100:
                        print("You already have the purest Qi")
                    elif self.qq < 100:
                        self.qq += qi
                        print(f"Your Qi quality improved by {qi} and now has a purity of {self.qq}%")
                        if self.qq >= 100:
                            print("You reached the maximum purity of your Qi")
                            self.qq = 100
                elif ch6 == 3:
                    if self.pc >= 100:
                        print("You already completed your core")
                    elif self.pc < 100:
                        self.pc += qi
                        print(f"Your Core has improved by {qi} and now is to {self.pc} completed")
                        if self.pc >= 100:
                            print("You completed your core")
                            self.pc = 100
                elif ch6 == 4:
                    self.ins += sc
                    print(f"The size of your Nascent Soul increased by {sc} meter"
                          f" and has now reached a height of {self.ins} meter")
                elif ch6 == 5:
                    self.exd += sc
                    print(f"The size of your domain increased by {sc} meter"
                          f"and has now reached a size of {self.exd} meter")
                elif ch6 == 6:
                    self.dac += qi
                    print(f"Your connection with the dao increased by {qi} "
                          f"and has now reached a connection of {self.dac}%")
                    if self.dac >= 100:
                        print("You reached the dao and are now an immortal")
                        print("")
                        print("I hope you liked my game")
                        break

    def cultivate(self, t, c, days):

        if c == 0:
            game.del_butn()
            self.output.insert(tk.END, "How long do you want to cultivate each day?\n")
            self.output.insert(tk.END, "\n")
            self.output.insert(tk.END, "(1) 1 Hour\n")
            self.output.insert(tk.END, "(2) 5 Hours \n")
            self.output.insert(tk.END, "(3) 10 Hours\n")
            self.output.insert(tk.END, "(4) 18 Hours\n")

            self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=lambda: game.cultivate(1, 1, None))
            self.butt1.place(x=559, y=340)

            self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=lambda: game.cultivate(5, 1, None))
            self.butt2.place(x=629, y=340)

            self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=lambda: game.cultivate(10, 1, None))
            self.butt3.place(x=559, y=380)

            self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=lambda: game.cultivate(18, 1, None))
            self.butt4.place(x=629, y=380)
        elif c == 1:
            game.del_butn()
            game.del_butn()
            self.output.insert(tk.END, f"You decided to cultivate {t} hours a day\n")
            self.dct = t
            self.frt = 24 - self.dct

        elif c == 2:
            try:

                ctpd = self.dct
                dc = self.bls * ctpd * days / 100
                self.cue += dc
                self.kph.config(text=f"Cultivation Xp: \n{self.cue}")
            except self.dct == 0:
                self.output.insert(tk.END, f"You first need to decide how long you want to cultivate\n")

        self.output.yview(tk.END)

    def time(self, days=None):

        new_days = days
        game.cultivate(None, 2, days)
        while new_days > 0:
            new_days -= 1
            self.day += 1
            if self.day == 31:
                self.month += 1
                self.day = 1
                if self.month == 13:
                    self.month = 1
                    self.year += 1
        else:
            self.date.config(text=f"{self.day}.{self.month}.{self.year} ")
            self.output.yview(tk.END)

    def dtime(self):  # for the 24-hour cycles
        pass

    def time_manager(self):  # for time managment system #no idea how i will get this to work
        pass
        time_manager_overlay = tk.Toplevel(self.root)
        time_manager_overlay.transient(self.root)  # associate with root
        time_manager_overlay.grab_set()  # make it modal (blocks background)
        time_manager_overlay.overrideredirect(True)  # remove window decorations

        # match geometry to root (works if root isn't moved between calls)
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty() + 450
        w = self.root.winfo_width()
        h = self.root.winfo_height() - 450
        time_manager_overlay.geometry(f"{w}x{h}+{x}+{y}")
        self.root.bind("<Escape>", lambda e: close_time_manager())
        exit_btn = tk.Button(time_manager_overlay, text="X", command=lambda: close_time_manager())
        exit_btn.pack(side="top", anchor="ne")

        Activities = [
            {"name": "Cultivation", "color": "#bfbfbf"},
            {"name": "Work", "color": "#6b8e23"},
            {"name": "Needs", "color": "#9370db"},
            {"name": "Sleep", "color": "#5b7bd5"},
        ]

        HOUR_DEFAULT = "#4a4a4a"  # default hour box color
        self.hours = [-1] * 24  # -1 means unset
        self.rect_ids = [None] * 24

        self.group_buttons = []
        for i, g in enumerate(Activities):

            btn = tk.Button(
                time_manager_overlay, text=g['name'], relief=tk.RAISED,
                command=lambda i=i: self.select_group(i),
                pady=6, width=8

            )
            btn.place(x=100 + i * 110, y=10, )
            self.group_buttons.append(btn)

            #i give up from here on onwards is danger expect for the close def thats great.

            #canvas_frame = tk.Frame()
            #canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

            #self.canvas = tk.Canvas(canvas_frame, highlightthickness=0)
            #self.canvas.pack(fill=tk.BOTH, expand=True)

            # Bindings for mouse events
            #self.canvas.bind("<Button-1>", self._on_left_click)
            #self.canvas.bind("<B1-Motion>", self._on_left_drag)
            #self.canvas.bind("<ButtonRelease-1>", self._on_left_release)

            def close_time_manager():
                time_manager_overlay.grab_release(),
                time_manager_overlay.destroy()
                self.root.focus_set()

            def select_group(self, index):
                self.select_group = index
                # Visual feedback
                for i, btn in enumerate(self.group_buttons):
                    if i == index:
                        btn.config(relief=tk.SUNKEN, bd=3)
                    else:
                        btn.config(relief=tk.RAISED, bd=1)

            def _draw_hours(self):
                self.canvas.delete("all")
                w = self.canvas.winfo_width() or 800
                h = self.canvas.winfo_height() or 160

                left_col_w = 220
                top_padding = 12
                hour_strip_h = 80

                # Left column (name + icon)
                self.canvas.create_rectangle(0, 0, left_col_w, h, fill="#111", outline="")
                # small icon box
                icon_x = 18
                icon_y = top_padding
                self.canvas.create_rectangle(icon_x, icon_y, icon_x + 48, icon_y + 48, fill="#222", outline="#333")
                # name text
                self.canvas.create_text(icon_x + 64, icon_y + 8, anchor='nw', fill="#fff",
                                        text="Dave, Taxonomist", font=("Segoe UI", 12, "bold"))

                # Hour numbers header (0..23)
                usable_w = max(600, w - left_col_w - 20)
                hour_w = usable_w / 24.0
                start_x = left_col_w + 10
                y0 = top_padding + 20

                for i in range(24):
                    x1 = start_x + i * hour_w
                    x2 = x1 + hour_w - 2
                    # hour background rect
                    rect = self.canvas.create_rectangle(x1, y0 + 24, x2, y0 + 24 + hour_strip_h,
                                                        fill=HOUR_DEFAULT, outline="#222", width=1)
                    self.rect_ids[i] = rect
                    # store tag for lookup
                    self.canvas.tag_bind(rect, '<Enter>', lambda e, idx=i: None)

                    # draw hour number above
                    self.canvas.create_text((x1 + x2) / 2, y0, text=str(i), fill="#ddd", font=("Helvetica", 9))

                    # colored overlay if assigned
                    if self.hours[i] != -1:
                        col = GROUPS[self.hours[i]]['color']
                        # put a smaller rect on top so outline remains
                        self.canvas.create_rectangle(x1 + 1, y0 + 25, x2 - 1, y0 + 24 + hour_strip_h - 1, fill=col,
                                                     outline="")

                # thin dividing line
                self.canvas.create_line(left_col_w, 0, left_col_w, h, fill="#2a2a2a")

            def _redraw(self):
                # redraw on resize
                self._draw_hours()

            def _hour_index_from_xy(self, x, y):
                # compute which hour box the x,y falls into
                left_col_w = 220
                start_x = left_col_w + 10
                w = self.canvas.winfo_width()
                usable_w = max(600, w - left_col_w - 20)
                hour_w = usable_w / 24.0
                if x < start_x:
                    return None
                rel = (x - start_x) / hour_w
                idx = int(rel)
                if 0 <= idx < 24:
                    return idx
                return None

            def _paint_hour(self, idx, group_idx):
                if idx is None:
                    return
                # update model
                self.hours[idx] = group_idx
                # update canvas: redraw the small overlay rect on top of the hour rectangle
                # To keep things simple, just call _draw_hours which re-renders everything
                self._draw_hours()

            def _clear_hour(self, idx):
                if idx is None:
                    return
                self.hours[idx] = -1
                self._draw_hours()

            # Mouse handlers
            def _on_left_click(self, event):
                idx = self._hour_index_from_xy(event.x, event.y)
                if idx is None:
                    return
                self._dragging = True
                self._last_painted = idx
                self._paint_hour(idx, self.selected_group)

            def _on_left_drag(self, event):
                if not self._dragging:
                    return
                idx = self._hour_index_from_xy(event.x, event.y)
                if idx is None or idx == self._last_painted:
                    return
                self._last_painted = idx
                self._paint_hour(idx, self.selected_group)

            def _on_left_release(self, event):
                self._dragging = False
                self._last_painted = None

        #self.frt


game = Game()
game.window()
