import random
import sys
import time
import tkinter as tk


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
        self.sfr_ALS = int(0) # Azure Cloud Sect
        self.rwsi = int(0) #the relation with the sect you are currently in
        self.otu = int(0) #if you reach 100 relations goes to 1 to stop infinite gain
        self.rw25 = int(0)
        self.rw50 = int(0)
        self.rw100 = int(0)
        self.gs = None #gender
        self.nm = None #name
        self.cp = int(0) #combat power
        self.sps = int(10) #size of the spirit sea
        self.qq = int(1) #quality of Qi
        self.pc = int(0) # percent of finishing the Core
        self.ins = int(0) # size of the nascent soul
        self.exd = int(0) #domain size
        self.dac = int(0) #percent of connection with dao
        self.uip = None
        self.pr = 0
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        self.bt4 = 0
        self.sr = 0 #sect rank
        self.rp = int(0) #reputation in sect


    def bdel(self):
        if self.bt1 == 1:
            self.butt1.destroy()
            self.bt1 = 0
        if self.bt2 == 1:
            self.butt2.destroy()
            self.bt2 = 0
        if self.bt3 == 1:
            self.butt3.destroy()
            self.bt3 = 0
            self.bt3 = 0
        if self.bt4 == 1:
            self.butt4.destroy()
            self.bt4 = 0

    
    def uin(self,c):
        self.uip = self.inp.get()
        self.inp.delete(0, tk.END)
        if c == 0:
            self.pr = 1
            game.start()
        else:
            if self.uip == 1:
                game.travel(0)
            elif self.uip == 2:
                game.sects(0)
            elif self.uip == 3:
                game.combat()
            elif self.uip == 4:
                pass
            elif self.uip == 5:
                game.time(0,0)
            elif self.uip == 6:
                game.realms()

    
    def combat(self):
        game.bdel()
        lwp = self.cp - 50
        hwp = self.cp + 50
        self.output.insert(tk.END,"\n")
        self.output.insert(tk.END,"Who do you want to fight with?\n")
        self.output.insert(tk.END,"\n")
        nl = ["Mo Tianxie","Xie Wuhen","Bai Mingsheng","Guo Zhenhai",
              "Hei Wulian","Zhao Tiansha","Feng Luoxian","Yan Wujian","Du Chengkong","Luo Hengzhi"] #list bad guys
        e1 = random.randrange(lwp,hwp)
        e2 = random.randrange(lwp,hwp)
        e3 = random.randrange(lwp,hwp)
        e4 = random.randrange(lwp,hwp)

        self.output.insert(tk.END,f"1 {random.choice(nl)} Combat Power: {e1}\n")
        self.output.insert(tk.END,f"2 {random.choice(nl)} Combat Power: {e2}\n")
        self.output.insert(tk.END,f"3 {random.choice(nl)} Combat Power: {e3}\n")
        self.output.insert(tk.END,f"4 {random.choice(nl)} Combat Power: {e4}\n")

        self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=lambda: game.fdt1(e1))
        self.butt1.place(x=559, y=340)
        self.bt1 = 1

        self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=lambda: game.fdt2(e2))
        self.butt2.place(x=629, y=340)
        self.bt2 = 1

        self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=lambda: game.fdt3(e3))
        self.butt3.place(x=559, y=380)
        self.bt3 = 1

        self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=lambda: game.fdt4(e4))
        self.butt4.place(x=629, y=380)
        self.bt4 = 1

        self.output.insert(tk.END,"\n")
        self.output.yview(tk.END)
        

    def fdt1(self,e1):
            if e1 < self.cp:
                 self.output.insert(tk.END,"You won against your enemy\n")
            else: self.output.insert(tk.END,"You lost but you were able to survive\n")
            game.bdel()
            self.output.yview(tk.END)
    def fdt2(self,e2):
            if e2 < self.cp:
                self.output.insert(tk.END,"You won against your enemy\n")
            else: self.output.insert(tk.END,"You lost but you were able to survive\n")
            game.bdel()
            self.output.yview(tk.END)
    def fdt3(self,e3):
            if e3 < self.cp:
                self.output.insert(tk.END,"You won against your enemy\n")
            else: self.output.insert(tk.END,"You lost but you were able to survive\n")
            game.bdel()
            self.output.yview(tk.END)
    def fdt4(self,e4):
            if e4 < self.cp:
                self.output.insert(tk.END,"You won against your enemy\n")
            else: self.output.insert(tk.END,"You lost but you were able to survive\n")
            game.bdel()
            self.output.yview(tk.END)
        

    def window(self):
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Python-Cultivation")
        self.cp = self.rea * 100

        self.output = tk.Text(self.root, height=34, width=79)
        self.output.place(x=0,y=0)

        self.inp = tk.Entry(self.root,width=61)
        self.inp.place(x=0,y=460)

        self.but1 = tk.Button(self.root, height=2, width=4,text="Travel",command=lambda: game.travel(0))
        self.but1.place(x=559,y=0)

        self.but2 = tk.Button(self.root,height=2,width=4,text="Sect",command=lambda: game.sects(0))
        self.but2.place(x=629,y=0)

        self.but3 = tk.Button(self.root,height=2,width=4,text="Fight",command=game.combat)
        self.but3.place(x=559,y=40)

        self.but4 = tk.Button(self.root,height=2,width=4,text="Stats")
        self.but4.place(x=629,y=40)

        self.but5 = tk.Button(self.root,height=2,width=4,text="Cultivate",command=lambda: game.time(0,0))
        self.but5.place(x=559,y=80)

        self.but6 = tk.Button(self.root,height=2,width=4,text="Ascension",command=game.realms)
        self.but6.place(x=629,y=80)

        self.but9 = tk.Button(self.root,height=2,width=8,text="Enter",command=lambda: game.uin(0))
        self.but9.place(x=559,y=450)

        self.cpl = tk.Label(self.root,height=2,width=15,text=f"Combat Power:\n {self.cp}")
        self.cpl.place(x=559,y=120)

        self.drc = tk.Label(self.root,height=2,width=15,text=f"{self.rsn} level of \n{self.step} realm")
        self.drc.place(x=559,y=160)

        self.kph = tk.Label(self.root,height=2,width=15,text=f"Cultivation Xp: {self.cue}",anchor="w")
        self.kph.place(x=559,y=210)

        self.xpn = tk.Label(self.root, height=2, width=15, text=f"XP for next level:\n {self.acr}")
        self.xpn.place(x=559, y=250)

        self.output.insert(tk.END,"Welcome to Python-Cultivation!\n")
        self.output.insert(tk.END,"\n")
        self.output.insert(tk.END,"You open your eyes to a world with vast towering mountains,"
              " their peaks covered in mist, stretch endlessly into the heavens."
              " The air is filled with Qi, an unseen force that allows you to cultivate.\n")
        self.output.insert(tk.END,"\n")
        self.output.insert(tk.END,"What is your name in this vast world\n")
        self.root.mainloop()


    def yes(self):
        self.output.insert(tk.END,"Yes\n")
    def no(self):
        self.output.insert(tk.END,"No\n")


    def start(self):
        self.nm = self.uip
        self.uip = None

        self.output.insert(tk.END,"What is your gender?\n")
        self.man = tk.Button(self.root,height=2,width=4,text="Man",command=game.gedm)
        self.man.place(x=559,y=380)

        self.women = tk.Button(self.root,height=2,width=4,text="Women",command=game.gedw)
        self.women.place(x=629,y=380)
        self.but9.config(command=lambda: game.uin(1))
    def gedm(self):
        self.gs = "Man"
        self.output.insert(tk.END, f"You are {self.nm} and you are a {self.gs}\n")
        self.man.destroy()
        self.women.destroy()
        self.output.insert(tk.END,"From now on you can do whatever you want\n")
    def gedw(self):
        self.gs = "Women"
        self.output.insert(tk.END, f"You are {self.nm} and you are a {self.gs}\n")
        self.women.destroy()
        self.man.destroy()
        self.output.insert(tk.END,"From now on you can do whatever you want\n")


    def sects(self,c):
        game.bdel()
        if self.psc == None:

                nsc = ["1 Heavenly Sword Sect\n","2 Demonic Blood Sect\n","3 Mystic Lotus Sect\n","4 Azure Cloud Sect\n"] #names of the sects
                self.output.insert(tk.END,"\n")
                self.output.insert(tk.END,"Which sect do you want to join?\n")
                self.output.insert(tk.END,"\n")
                for sect in nsc:
                    self.output.insert(tk.END,sect)
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
            self.butt1.destroy()
            self.butt2.destroy()
            self.output.insert(tk.END,"Do you want to (1) improve relations with your sect or "
                                      "(2) do you want to increase your rank in the sect? \n")
            self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=lambda: game.sects(1))
            self.butt1.place(x=559, y=340)
            self.bt1 = 1

            self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=lambda: game.sects(2))
            self.butt2.place(x=629, y=340)
            self.bt2 = 1
            self.output.yview(tk.END)

            if c == 2:
                game.bdel()
                if self.sr == 0:
                    pass
                elif self.sr == 1:
                    self.output.insert(tk.END,"You are currently a outer disciple"
                                              " but you can improve your rank in the sect, by doing:\n")
                    self.output.insert(tk.END,"\n")
                    self.output.insert(tk.END,"1 Help with some regular tasks\n")
                    self.output.insert(tk.END,"2 do easy sect missions\n")
                    self.output.insert(tk.END,"3 Gather firewood and water for the sect’s communal areas\n")
                    self.output.insert(tk.END,"4 Gather herbs or resources for the sect\n")

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
                    self.output.insert(tk.END,"You are currently a inner disciple"
                                              " but you can improve your rank in the sect, by doing:\n")
                    self.output.insert(tk.END,"\n")
                    self.output.insert(tk.END,"1 Scout potential outer disciples for the sect\n")
                    self.output.insert(tk.END,"2 Assist in managing and training outer disciples\n")
                    self.output.insert(tk.END,"3 Guard the sect entrance or patrol the outer grounds\n")
                    self.output.insert(tk.END,"4 Assist in setting up and maintaining training grounds\n")

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
                    self.output.insert(tk.END,"You are currently a core disciple"
                                              " but you can improve your rank in the sect, by doing:\n")
                    self.output.insert(tk.END,"\n")
                    self.output.insert(tk.END,"1 Train and mentor inner disciples\n")
                    self.output.insert(tk.END,"2 Guard the sect treasury \n")
                    self.output.insert(tk.END,"3 help the elders\n")
                    self.output.insert(tk.END,"4 help supervising training fights\n")

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
                    
            elif c == 1:
                game.bdel()
                if self.psc != None:
                    if self.otu == 1:
                        self.output.insert(tk.END,"You already reached max relations with your sect\n")
                    ri = random.randrange(5,20)
                    self.rwsi += ri
                    self.output.insert(tk.END,f"You were able to improve your relation with {self.psc} to {self.rwsi}\n")
                    if 1 <= self.rwsi < 25:
                        self.output.insert(tk.END,f"If you reach 25 relations with {self.psc} you will be able to reach a new cultivation level\n")
                    elif 25 <= self.rwsi < 50:
                        if self.rw25 == 1:
                            self.output.insert(tk.END,"If you are able to reach 50 relations a wise elder will teach you\n")
                        else:
                            self.output.insert(tk.END,"Congratulation you reached relations up to 25.\n"
                                  " You are getting toughed by a new elder and you try to reach a new cultivation level\n")
                            self.rw25 = 1

                            if self.rsn == 9:
                                self.output.insert(tk.END,f"As you are currently in the peek of {self.step}\n"
                                      f" the elder was not able to help you break through but you got 1000 cultivation xp\n")
                                self.cue += 1000
                                self.kph.config(text=f"Cultivation Xp: {self.cue}")
                            else:
                                self.rea += 1
                                self.rsn += 1
                                self.output.insert(tk.END,"You were able to reach a new cultivation level\n")
                                self.drc.config(text=f"{self.rsn} level of \n{self.step} realm")
                    elif 50 <= self.rwsi <100:
                        if self.rw50 == 1:
                            self.output.insert(tk.END,"If you reach 100 relations the sect master will teach you personally\n")
                        else:
                            self.output.insert(tk.END,"Fabulous you reached 50 relations.\n"
                                  " A wise elder guided you on your way and you broke through 2 cultivation levels.\n")
                            self.rw50 = 1
                            if self.rsn >= 8:
                                self.output.insert(tk.END,f"As you are currently in the {self.rsn} of {self.step}\n"
                                      f" the elder was not able to help you break through but you got 2500 cultivation xp")
                                self.cue += 2500
                                self.kph.config(text=f"Cultivation Xp: {self.cue}")
                            else:
                                self.rea += 2
                                self.rsn += 2
                                self.drc.config(text=f"{self.rsn} level of \n{self.step} realm")
                    elif self.rwsi >= 100:
                        if self.rw100 ==1:
                            self.output.insert(tk.END,"The sect master already guided you\n")
                        else:
                            self.output.insert(tk.END,f"Magnificent you reached 100 relations with the {self.psc}.\n"
                                  f"The sect master taught you and you were able to reach the peak in the {self.step} realm.")
                            nfm = 9 - self.rsn
                            self.rsn += nfm
                            self.rea += nfm
                            self.drc.config(text=f"{self.rsn} level of \n{self.step} realm")
                            self.rw100 = 1
                            if nfm == 0:
                                self.output.insert(tk.END,"You are already at the peak "
                                      "but the sect master was able to teach you so much that now you can break through on your own\n")
                                self.cue += self.acr
                            self.otu = 1

        self.cp = self.rea * 100
        self.cpl.config(text=f"Combat Power:\n {self.cp}")
        self.kph.config(text=f"Cultivation Xp: {self.cue}")
        self.xpn.config(text=f"XP for next level:\n {self.acr}")
        self.output.yview(tk.END)


    def sri(self,cr):
        game.bdel()
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
            self.output.insert(tk.END,f"You reached the rank of {nr}\n")
            self.sr = 2
        elif self.rp == 200:
            self.output.insert(tk.END,f"You reached the rank of {nr}\n")
            self.sr = 3
        elif self.rp == 300:
            self.output.insert(tk.END,f"You reached the rank of {nr}\n")
        self.output.insert(tk.END,f"You completed your task and are now closer to reach the rank of {nr}\n")



    def sdt1(self):
            self.psc = "Heavenly Sword Sect"
            rws = self.sfr_HSS
            self.output.insert(tk.END,f"You joined {self.psc} as an outer disciple\n")
            self.sr = 1
            self.bt1 = 1
            game.bdel()
            self.output.yview(tk.END)
    def sdt2(self):
            self.psc = "Demonic Blood Sect"
            rws = self.sfr_DBS
            self.output.insert(tk.END,f"You joined {self.psc} as an outer disciple\n")
            self.sr = 1
            game.bdel()
            self.output.yview(tk.END)
    def sdt3(self):
            self.psc = "Mystic Lotus Sect"
            rws = self.sfr_MLS
            self.output.insert(tk.END,f"You joined {self.psc} as an outer disciple\n")
            self.sr = 1
            game.bdel()
            self.output.yview(tk.END)
    def sdt4(self):
            self.psc = "Azure Cloud Sect"
            rws = self.sfr_ALS
            self.output.insert(tk.END,f"You joined {self.psc} as an outer disciple\n")
            self.sr = 1
            game.bdel()
            self.output.yview(tk.END)
        

    def realms(self):
        acr = self.cr*self.rea #required
        self.xpn.config(text=f"XP for next level:\n {self.acr}")
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
                c = random.randint(1,100)
                if c > 75:
                    self.output.insert(tk.END,"You experienced a backlash and you could not advance \n")
                    self.rsn -= 5
                    self.rea -= 5
                    self.xpn.config(text=f"XP for next level:\n {self.acr}")
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
                elif c <=74:
                    self.output.insert(tk.END,"You advance to the next realm\n")
                    self.rsn = 1
            self.output.insert(tk.END,f"Your cultivation is now the {self.rsn} of {self.step}\n")
        else: self.output.insert(tk.END,"You do not have enough Xp\n")
        self.cp = self.rea * 100
        self.xpn.config(text=f"XP for next level:\n {self.acr}")
        self.kph.config(text=f"Cultivation Xp: {self.cue}")
        self.drc.config(text=f"{self.rsn} level of \n{self.step} realm")
        self.cpl.config(text=f"Combat Power:\n {self.cp}")
        self.output.yview(tk.END)


    def travel(self,t):
        game.bdel()
        if t == 0:
            self.output.insert(tk.END,"\n")
            self.output.insert(tk.END,"You can visit:\n")
            self.output.insert(tk.END,"\n")
            self.output.insert(tk.END,"1 random Place\n")
            self.output.insert(tk.END,"2 the village\n")
            if self.rwsi > 25:
                self.output.insert(tk.END,"3 sect middle\n")
                self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=game.rdt3)
                self.butt3.place(x=559, y=380)
                self.bt3 = 1
            if self.rwsi >= 100:
                self.output.insert(tk.END,"4 a goldy artifact\n")
                self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=game.rdt4)
                self.butt4.place(x=629, y=380)
                self.bt4 = 1

            self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=game.rdt1)
            self.butt1.place(x=559,y=340)
            self.bt1 = 1

            self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=game.rdt2)
            self.butt2.place(x=629,y=340)
            self.bt2 = 1
            self.output.yview(tk.END)


    def rdt1(self):
                self.location = "random Place"
                self.bls += 50
                self.output.insert(tk.END,"You are now at a random place\n")
                game.bdel()
                self.output.yview(tk.END)
    def rdt2(self):
                self.location = "Village"
                self.output.insert(tk.END,f"You went to the {self.location}\n")
                game.bdel()
                self.bls += 100
                self.output.yview(tk.END)
    def rdt3(self):
                self.location = "sect middle"
                self.output.insert(tk.END,f"You are at the {self.location}\n")
                self.bls += 200
                game.bdel()
                self.output.yview(tk.END)
    def rdt4(self):
                self.location = "godly artifact"
                self.output.insert(tk.END,f"You are at the {self.location}\n")
                self.bls += 1000
                game.bdel()
                self.output.yview(tk.END)
        

    def time(self,t,c):
        game.bdel()
        if c == 0:
            self.output.insert(tk.END,"\n")
            self.output.insert(tk.END,"How long do you want to cultivate?\n")
            self.output.insert(tk.END,"\n")
            self.output.insert(tk.END,"1 10 days \n")
            self.output.insert(tk.END,"2 25 days \n")
            self.output.insert(tk.END,"3 50 days \n")
            self.output.insert(tk.END,"4 100 days \n")

            self.butt1 = tk.Button(self.root, height=2, width=4, text="1", command=lambda: game.time(10,1))
            self.butt1.place(x=559, y=340)
            self.bt1 = 1

            self.butt2 = tk.Button(self.root, height=2, width=4, text="2", command=lambda: game.time(25,1))
            self.butt2.place(x=629, y=340)
            self.bt2 = 1

            self.butt3 = tk.Button(self.root, height=2, width=4, text="3", command=lambda: game.time(50,1))
            self.butt3.place(x=559, y=380)
            self.bt3 = 1

            self.butt4 = tk.Button(self.root, height=2, width=4, text="4", command=lambda: game.time(100,1))
            self.butt4.place(x=629, y=380)
            self.bt4 = 1
        else:

            day = 1
            while t >0:
                l = self.bls * 10
                day += 1
                t -= 1
                b = random.randint(0,200)
                if b < 1:
                    self.output.insert(tk.END, f"You experienced backlash and lost {l}\n")
                    self.cue -= l
                self.cue += self.bls

                self.kph.config(text=f"Cultivation Xp: {self.cue}")
                c = 0
                for bt in [self.butt1, self.butt2, self.butt3, self.butt4]:
                    try:
                        bt.destroy()
                    except:
                        pass
            self.output.insert(tk.END, f"You completed your cultivation\n")
        self.output.yview(tk.END)


game = Game()
game.window()
