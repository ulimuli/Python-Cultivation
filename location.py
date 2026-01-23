#alr so trade with local tribes clans and such, gathering of local resources, work system, maybe a clan sect system thingy
import random
import tkinter as tk
from tkinter import ttk
from Time import Timming


class Loc_sys:
    def __init__(self, parent, place="Forrest", place_nr=1, dct=1, bls=1, cue=10, second=1,
                 minute=1, hour=1, day=1, month=1, year=1,items=None,user_items=None,coins=None,dwt=0):
        self.upds = True
        self.fmw = None
        self.ttt = 0
        self.ch_plc = None
        self.cur_plc = "out of this world"
        self.selected_var = None
        self.label_var = tk.StringVar()
        self.parent = parent
        self.place = place
        self.place_nr = place_nr
        self.place_coord = None
        self.tiles_col = {}
        self.ch_col = ""
        self.cur_col = "out of this world"
        self.dct = dct  #all for the time stuff import from main
        self.bls = bls
        self.cue = cue
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day = day
        self.month = month
        self.year = year  # till here main import stuff
        self.seconds = 0
        self.trv_r_time = 0
        self.local_tribes = [
            {"name": "Ashfang Totem Tribe"},
            {"name": "Bloodsun Hunter Clan", },
            {"name": "Stoneheart Ancestral Tribe", },
            {"name": "Frostbone Wolf Tribe", },
            {"name": "Sky-Eater Hawk Tribe", },
            {"name": "Obsidian Vein Tribe", },
            {"name": "Thousand Scar Berserker Tribe", },
            {"name": "Spirit Drum Earth Tribe", },
            {"name": "Red Marsh Crocodile Tribe", },
            {"name": "Thunder Totem Bear Tribe", },
            {"name": "Moon-Howl Night Tribe", },
            {"name": "Iron Blood War Tribe", },
            {"name": "Sun-Devouring Serpent Tribe", },
            {"name": "Black Ridge Bone Tribe", },
            {"name": "Ancestral Flame Totem Tribe", },
            {"name": "Void Step Shadow Tribe", },
            {"name": "Stormcaller Horn Tribe", },
            {"name": "Heaven-Sunder Giant Tribe", },
            {"name": "Gravewind Spirit Tribe", },
            {"name": "Primordial Fang Savage Tribe"},
        ]

        self.locations = [
            {"name": "Market Place","call": self.marketplace},
            {"name": "Local Inn","call": self.local_inn},
            {"name": "Workplace","call": self.workplace}
        ]

        self.Inv_Groups = [
            {"name": "Everything"},
            {"name": "Equipment"},
            {"name": "Consumables"},
            {"name": "Talisman"},
            {"name": "Food"},
            {"name": "Refinement Resources"},
            {"name": "Artifacts"},
            {"name": "others"}
        ]

        self.Items = items
        self.user_items = user_items
        self.coins = coins
        self.dwt = dwt
    def create_ui(self):
        self.loc_location()
        self.parent.after_idle(self.collections_list)
        self.canvas = tk.Canvas(self.parent, height=480, width=700, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.parent.bind("<Escape>", lambda e: self.close_inv())
        exit_btn = tk.Button(self.canvas, text="X", command=lambda: self.close_inv())
        exit_btn.place(x=650, y=2)

        self.canvas.create_text(
            70,
            50,
            text=f"Location: {self.place}"
        )
        self.collection = "None"
        if self.place_nr <= 1:
            self.collection = "Local Tribes"
        elif self.place_nr == 2:
            self.collection = " Local Clans"
        elif self.place_nr == 4:
            pass  #later for Sects

        ttk.Label(self.canvas, text=f"{self.collection}:", font=("Inter", 10, "bold")).place(x=10, y=100)

        self.logger = tk.Text(self.canvas, height=10, width=60, highlightthickness=0)
        self.logger.place(x=250, y=330)

        self.collection_list = tk.Listbox(self.canvas, height=8)
        self.collection_list.place(y=120, x=10)

        ttk.Label(self.canvas, text=f"Travel to:", font=("Inter", 10, "bold")).place(x=10, y=280)

        self.dis_loc_loc = ttk.Combobox(self.canvas, values=self.loc_locations, state="readonly")
        self.dis_loc_loc.place(x=0, y=300)

        dis_tn = ttk.Label(self.canvas, textvariable=self.label_var, font=("Inter", 10, "bold")).place(x=5, y=330)

        ttk.Button(self.canvas, text="Travel", command=self.travel).place(x=5, y=350)

        self.pb = ttk.Progressbar(self.canvas, orient="horizontal", length=100, mode="determinate")
        self.pb.place(x=5, y=390)

        ttk.Label(self.canvas, text=f"Travel Progress:", font=("Inter", 10, "bold")).place(x=10, y=405)

        self.date = tk.Label(self.canvas, width=20, height=1, text=f"{self.day}.{self.month}.{self.year}")
        self.date.place(x=300, y=10)

        self.ddate = tk.Label(self.canvas, width=20, height=1,
                              text=f"{self.hour}:{self.minute} and {self.second} seconds")
        self.ddate.place(x=300, y=30)

        self.coin = tk.Label(self.canvas, text=f"Coins: {self.coins}")
        self.coin.place(x=600, y=50)


    def time_update(self, nsec=0, nmin=0, nhour=0, nday=0, nmonth=0, nyear=0, pt=0):
        self.second = nsec
        self.minute = nmin
        self.hour = nhour
        self.day = nday
        self.month = nmonth
        self.year = nyear

        try:
            wpt = pt
            while wpt > 0:
                self.ttm -= 1
                wpt -= 1
                if self.ttm <= 0:
                    self.coins += self.pm
                    self.work()
        except: pass

        try:
            self.date.config(text=f"{self.day}.{self.month}.{self.year}")
            self.ddate.config(text=f"{self.hour}:{self.minute} and {self.second} seconds")

            self.trv_r_time -= pt
            nvfb = 100 - self.trv_r_time * 100 / self.ttt
            self.pb["value"] = nvfb

            if self.trv_r_time <= 0:
                if self.fmw == 1:
                    self.cur_plc = self.ch_plc
                    for v in self.locations:
                        if v["name"] == self.cur_plc:
                            v["call"]()
                elif self.fmw == 2:
                    self.cur_col = self.ch_col
                self.logger.insert(tk.END, f"You arrived\n")
                self.ttt = 0
                self.trv_r_time = 0
                self.pb["value"] = 0



        except:
            pass


        #Timming.dtime(Timming(self.dct,self.bls,self.cue,self.second,self.minute,self.hour,self.day,self.month,self.year),self.seconds)

    def col_list_update(self,place_coord):
        self.place_coord = place_coord

    def travel(self):
        for f in self.collection_list.curselection():
            self.ch_col = self.collection_list.get(f)
        self.ch_plc = self.dis_loc_loc.get()

        if self.ch_col == "":
            self.logger.insert(tk.END, f"Please first select a {self.collection}\n")
        else:
            if self.ch_col == self.cur_col:
                if self.ch_plc == self.cur_plc:
                    pass
                else:
                    if self.ch_plc == "":
                        self.logger.insert(tk.END, f"Please first select a local Location\n")
                    else:
                        self.logger.insert(tk.END, f"You decided to travel to {self.ch_plc}. The travel time is 1 hour\n")
                        self.trv_r_time = 60 * 60
                        self.ttt = 60 * 60
                        self.fmw = 1
            else:

                self.logger.insert(tk.END, f"You decided to travel to {self.ch_col}. The travel time is 5 hours\n")
                self.trv_r_time = 60 * 60 * 5
                self.ttt = 60 * 60 * 5
                self.fmw = 2

        self.logger.yview(tk.END)

    def update_label(self):
        pass
        #self.ch_plc = self.selected_var.get()
        #self.label_var.set(
        #    f"You will need 1 hour to get to {self.selected_var.get()}:"
        #)

    def collections_list(self):
        print(f"qssdf {self.place_coord}")
        self.collection_list.delete(0, tk.END)

        if self.place_coord not in self.tiles_col:
            local_collections = random.randint(2, 4)
            col_chos = random.sample(self.local_tribes, local_collections)

            self.tiles_col[self.place_coord] = [col.copy() for col in col_chos]
        for col in self.tiles_col[self.place_coord]:
            self.collection_list.insert(tk.END, col["name"])
        print(self.tiles_col)
        self.logger.yview(tk.END)
    def loc_location(self):
        self.loc_locations = list()
        for loc in self.locations:
            self.loc_locations.append(loc["name"])

    def marketplace(self):
        self.close_inv()
        self.create_ui()
        x=300
        y=110

        self.trade_tree = ttk.Treeview(self.canvas,columns=("Value","Quantity"))
        self.trade_tree.place(x=x,y=y)

        trade_scroll = ttk.Scrollbar(self.canvas, orient="vertical", command=self.trade_tree.yview)
        self.trade_tree.config(yscrollcommand=trade_scroll.set)
        trade_scroll.place(x=x + 365,y=y + 25,height=184)
        self.trade_tree.heading("#0", text="Item")
        self.trade_tree.heading("Value", text="Value")
        self.trade_tree.column("Value",width=90)
        self.trade_tree.heading("Quantity", text="Quantity")
        self.trade_tree.column("Quantity",width=90)


        buy = ttk.Button(self.canvas,text="Buy",command=lambda: self.count_item(amount=1,g=True))
        buyall = ttk.Button(self.canvas, text="Buy all", command=lambda: self.count_item(amount=-1,g=True))
        sell = ttk.Button(self.canvas, text="Sell", command=lambda: self.count_item(amount=1,g=False))
        sellall = ttk.Button(self.canvas, text="Sell all", command=lambda: self.count_item(amount=-1,g=False))

        buy.place(x=x,y=80)
        buyall.place(x=x+100, y=80)
        sell.place(x=x+200, y=80)
        sellall.place(x=x+300, y=80)



        seller = self.trade_tree.insert("",tk.END, text="Seller Inventory")
        user = self.trade_tree.insert("", tk.END, text="Your Inventory")
        self.seller(update=self.upds)

        for cat in self.Inv_Groups:
            carts = self.trade_tree.insert(seller, tk.END, text=cat["name"])
            for d in self.seller_inf:
                if cat["name"] == "Everything" or d["category"] == cat["name"]:
                    if d["amount"] == 0:
                        pass
                    else:
                        self.trade_tree.insert(carts,tk.END,text=d["item"],values=(d["value"],d["amount"]))

        for cat in self.Inv_Groups:
            cats = self.trade_tree.insert(user, tk.END, text=cat["name"])
            for i in self.user_items:
                if cat["name"] == "Everything" or i["category"] == cat["name"]:
                    if i["amount"] == 0:
                        pass
                    else:
                        self.trade_tree.insert(cats,tk.END,text=i["item"],values=(i["value"],i["amount"]))
        self.coin.config(text=f"Coins: {self.coins}")
    def seller(self,update):
        if update is True:
            isa = self.place_nr #multipliyer
            voagfs = 10000#*isa  # value of all goods from seller
            self.seller_inf = []

            while voagfs >=0:
                t1 = random.choice(self.Items)
                sfidk = t1.copy() #save for idk what ?? i guess?
                for i in self.seller_inf:
                    if i["item"] == sfidk["item"]:
                        i["amount"] += 1
                        break
                else:
                    self.seller_inf.append(sfidk)
                voagfs -= sfidk["value"]
        else:pass
        self.upds = False


    def local_inn(self):
        pass
    def workplace(self,dwt=None):
        print(self.cur_plc)
        if self.cur_plc == "Workplace":

            self.close_inv()
            self.create_ui()
            ttk.Label(self.canvas,text="You can start working. You will be paid 2 Coins per hour.").place(x=300,y=100)
            ttk.Button(self.canvas,text="Start Work",command=self.work).place(x=350,y=200)

        else:pass

        if dwt is None:
            pass
        else:
            self.dwt = dwt


    def work(self):
        self.pm = self.dwt * 2
        self.ttm =60*60*24 #time till money
        self.coin.config(text=f"Coins: {self.coins}")


    def count_item(self,amount=0,g=False): #g = get/buy
        curItem = self.trade_tree.focus()
        name = self.trade_tree.item(curItem)["text"]
        gtc = self.trade_tree.parent(curItem)
        wit = self.trade_tree.parent(gtc)
        wit_name = self.trade_tree.item(wit)["text"]
        found = False

        if wit_name == "Seller Inventory":
            wiyt = self.seller_inf
        else: wiyt = self.user_items
        if g is True:
            for item in wiyt:
                if item["item"] == name:
                    if amount == -1:
                        amount = item["amount"]
                    if item["value"]*amount > self.coins:
                        self.logger.insert(tk.END,f"You do not have enough Coins\n")
                        return
                    item["amount"] -= amount
                    self.coins -= item["value"]*amount
            for d in self.user_items:
                if d["item"] == name:
                    d["amount"] += amount
                    found = True
            if not found:
                for s in self.Items:
                    if s["item"] == name:
                        ani = s.copy()
                        ani["amount"] += amount
                        self.user_items.append(ani)
        else:
            for item in wiyt:
                if item["item"] == name:
                    if amount == -1:
                        amount = item["amount"]
                    item["amount"] -= amount
                    self.coins += item["value"] * amount
            for d in self.seller_inf:
                if d["item"] == name:
                    d["amount"] += amount
                    found = True
            if not found:
                for s in self.Items:
                    if s["item"] == name:
                        ani = s.copy()
                        ani["amount"] += amount
                        self.user_items.append(ani)
        print(f"Coins:{self.coins}")
        self.marketplace()


    def close_inv(self):
        self.canvas.grab_release()
        self.canvas.destroy()
        self.parent.focus_set()
