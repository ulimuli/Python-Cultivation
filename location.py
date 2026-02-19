#alr so trade with local tribes clans and such, gathering of local resources, work system, maybe a clan sect system thingy
import copy
import random
import tkinter as tk
from tkinter import ttk
from Inventory_System import Inv_system


class Loc_sys:
    def __init__(self, parent, place="Forrest", place_nr=1, dct=1, bls=1, cue=10, second=1,
                 minute=1, hour=1, day=1, month=1, year=1,items=None,user_items=None,coins=None,dwt=None):
        self.renting = None
        self.ctr = 0
        self.working = None
        self.dtp = None
        self.ct = 0
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
        self.ttrf = 60*60*24*7
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

        self.collection_traits = [ #traits currently copeid from ai will change that once i give each attributes

            # 🌍 Attitude toward outsiders
            "welcomes_outsiders",
            "distrusts_outsiders",
            "hostile_to_outsiders",
            "isolationist_sect",
            "allows_outsiders_on_trial",

            # 🤝 Trade & interaction
            "likes_trading",
            "trade_neutral",
            "refuses_trade",
            "controls_trade_strictly",
            "black_market_tolerant",

            # 🏯 Culture & values
            "honors_ancestors",
            "values_strength",
            "values_enlightenment",
            "values_wealth",
            "values_merit",
            "values_bloodline",
            "values_seniority",

            # ⚔️ Conflict & violence
            "quick_to_take_offense",
            "vengeance_oriented",
            "honor_bound",
            "avoids_open_conflict",
            "prefers_duels",
            "collective_punishment",

            # 🧘 Cultivation philosophy
            "orthodox_cultivation",
            "demonic_cultivation",
            "balanced_yin_yang",
            "body_refinement_focused",
            "soul_cultivation_focused",
            "artifact_reliant",
            "pill_dependent",

            # 🧠 Knowledge & secrecy
            "guards_techniques",
            "shares_knowledge_selectively",
            "open_teachings",
            "hoards_manuals",
            "tests_disciples_harshly",

            # 👥 Social structure
            "sect_over_family",
            "family_over_sect",
            "elder_rule",
            "patriarch_rule",
            "council_rule",

            # 🌱 Growth & recruitment
            "recruits_mortals",
            "recruits_only_clan",
            "steals_disciples",
            "adopts_orphans",
            "talent_obsessed",

            # 🌑 Morality & reputation
            "ruthless_methods",
            "benevolent_reputation",
            "neutral_alignment",
            "feared_by_neighbors",
            "respected_by_neighbors",

            # 🏔️ Environment & lifestyle
            "mountain_secluded",
            "urban_sect",
            "nomadic_cultivators",
            "hidden_realm_dwelling",
            "spirit_beast_friendly",

            # ⚖️ Law & discipline
            "strict_rules",
            "lenient_rules",
            "harsh_punishments",
            "rehabilitative_justice",
            "trial_by_strength"
        ]

        self.locations = [
            {"name": "Market Place","call": self.create_marketplace},
            {"name": "Local Inn","call": self.local_inn},
            {"name": "Workplace","call": self.workplace},
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
        self.user_coins = coins
        self.dwt = dwt
        self.inv = Inv_system()
    def create_ui(self):
        self.loc_location()
        self.parent.after_idle(self.collections_list)
        self.canvas = tk.Canvas(self.parent, height=490, width=700, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.parent.bind("<Escape>", lambda e: self.close_inv())
        exit_btn = tk.Button(self.canvas, text="X", command=lambda: self.close_inv())
        exit_btn.place(x=650, y=2)

        self.location = ttk.Label(self.canvas,text=f"Location: {self.place}")
        self.location.place(x=10,y=40,)

        self.collection = "None"
        if self.place_nr <= 1:
            self.collection = "Local Tribes"
        elif self.place_nr == 2:
            self.collection = " Local Clans"
        elif self.place_nr == 4:
            pass  #later for Sects

        ttk.Label(self.canvas, text=f"{self.collection}:", font=("Inter", 10, "bold")).place(x=10, y=100)

        self.logger = tk.Text(self.canvas, height=10, width=60, highlightthickness=0)
        self.logger.place(x=250, y=340)

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

        self.coin = tk.Label(self.canvas, text=f"Coins: {self.user_coins}")
        self.coin.place(x=550, y=30)

        self.acf = ttk.LabelFrame(self.canvas, width=420, height=270, )  # activity frame
        self.acf.place(x=250, y=48)

        for v in self.locations:
            if v["name"] == self.cur_plc:
                v["call"]()

    def time_update(self, nsec=0, nmin=0, nhour=0, nday=0, nmonth=0, nyear=0, pt=0):

        self.work(pt,self.hour)
        self.rent(pt, self.hour)

        self.second = nsec
        self.minute = nmin
        self.hour = nhour
        self.day = nday
        self.month = nmonth
        self.year = nyear

        try:
            if pt >= self.ttrf:
                self.seller()
            else: self.ttrf -= pt
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
                    self.place = self.cur_plc
                    self.location.config(text=f"Location: {self.place}")
                    for v in self.locations:
                        if v["name"] == self.cur_plc:
                            v["call"]()
                elif self.fmw == 2:
                    self.cur_col = self.ch_col
                    self.cur_plc = None

                    self.acf.destroy()
                    self.acf = ttk.LabelFrame(self.canvas, width=420, height=270, )  # activity frame
                    self.acf.place(x=250, y=48)

                    self.place = self.cur_col
                    self.location.config(text=f"Location: {self.place}")
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

    def update_place(self,place):
        self.cur_plc = None
        self.cur_col = None
        self.place = place
        self.seller()

    def create_collections(self,c):
        traits = random.randint(2,4)
        col = {
                "name": c["name"],
                "Population": random.randint(50000,200000),
                "Traits": random.sample(self.collection_traits, traits)
        }
        return col


    def collections_list(self):
        print(f"qssdf {self.place_coord}")
        self.collection_list.delete(0, tk.END)

        if self.place_coord not in self.tiles_col:
            local_collections = random.randint(2, 4)
            col_chos = random.sample(self.local_tribes, local_collections)

            preset = [self.create_collections(c) for c in col_chos]
            self.tiles_col[self.place_coord] = preset

        for col in self.tiles_col[self.place_coord]:
            self.collection_list.insert(tk.END,f"{col['name']}")
        print(self.tiles_col)
        self.logger.yview(tk.END)
    def loc_location(self):
        self.loc_locations = list()
        for loc in self.locations:
            self.loc_locations.append(loc["name"])

    def create_marketplace(self):

        self.acf.destroy()
        self.acf = ttk.LabelFrame(self.canvas, width=420, height=270, )  # activity frame
        self.acf.place(x=250, y=48)
        x = 15
        y = 30

        self.trade_tree = ttk.Treeview(self.acf, columns=("Value", "Quantity"))
        self.trade_tree.place(x=x, y=y)

        trade_scroll = ttk.Scrollbar(self.acf, orient="vertical", command=self.trade_tree.yview)
        self.trade_tree.config(yscrollcommand=trade_scroll.set)
        trade_scroll.place(x=x + 365, y=y + 25, height=184)
        self.trade_tree.heading("#0", text="Item")
        self.trade_tree.heading("Value", text="Value")
        self.trade_tree.column("Value", width=90)
        self.trade_tree.heading("Quantity", text="Quantity")
        self.trade_tree.column("Quantity", width=90)

        buy = ttk.Button(self.acf, text="Buy", command=lambda: self.count_item(amount=1, g=True))
        buyall = ttk.Button(self.acf, text="Buy all", command=lambda: self.count_item(amount=None, g=True))
        sell = ttk.Button(self.acf, text="Sell", command=lambda: self.count_item(amount=1, g=False))
        sellall = ttk.Button(self.acf, text="Sell all", command=lambda: self.count_item(amount=None, g=False))

        buy.place(x=x, y=5)
        buyall.place(x=x + 100, y=5)
        sell.place(x=x + 200, y=5)
        sellall.place(x=x + 300, y=5)

        self.marketplace()



    def marketplace(self):
        try:
            self.trade_tree.delete(*self.trade_tree.get_children())
            print("worked deleted trade tree")
        except: print("did not delete the trade info")
        seller = self.trade_tree.insert("",tk.END, text="Seller Inventory")
        user = self.trade_tree.insert("", tk.END, text="Your Inventory")


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
        self.coin.config(text=f"Coins: {self.user_coins}")
    def seller(self,):
            self.ttrf = 60*60*24*7 #time till refresh
            isa = self.place_nr #multipliyer
            voagfs = 10000#*isa  # value of all goods from seller
            self.seller_coins = random.randint(2500,5000)
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


    def local_inn(self):
        if self.cur_plc == "Local Inn":
            self.acf.destroy()
            self.acf = ttk.LabelFrame(self.canvas, width=420, height=270, )  # activity frame
            self.acf.place(x=250, y=48)
            ttk.Label(self.acf, text="You can rent a room. \nYou will be deducted 10 Coins per day.").place(x=50, y=100)

            ttk.Button(self.acf, text="Start Renting", command=lambda: self.rent(ntime=None, renting=True)).place(x=100,
                                                                                                               y=200)
            ttk.Button(self.acf, text="Stop Renting", command=lambda: self.rent(ntime=None, renting=False)).place(x=210,
                                                                                                              y=200)

    def rent(self,ntime=0,hour=None,renting=None):
        if renting is True:
            self.renting = True
        else:
            if renting is False:
                self.renting = False
        print(f"Currently it is {hour} hour late and {ntime} seconds passed.")
        if self.renting is True:
            try:
                if ntime is None:
                    self.logger.insert(tk.END, f"You started renting\n")

                self.ctr = self.ctr + ntime

                while self.ctr >= 60*60*24:
                    self.user_coins -= 10
                    self.ctr -= 60 * 60*24
            except: pass

        else:
            if ntime is None:
                self.logger.insert(tk.END, f"You stopped renting\n")

        try:
            self.coin.config(text=f"Coins: {self.user_coins}")
        except:
            pass
    def workplace(self,dtp=None): #Plan: Make like a board where jobs can be given out based on skill level or so. Bad thing is i do not have a skill system yet ... Also i will need to integrate the work hours from the Time Planner
        print(self.cur_plc)
        if self.cur_plc == "Workplace":

            self.acf.destroy()
            self.acf = ttk.LabelFrame(self.canvas, width=420, height=270, )  # activity frame
            self.acf.place(x=250, y=48)
            ttk.Label(self.acf,text="You can start working. \nYou will be paid 2 Coins per hour.").place(x=50,y=100)

            ttk.Button(self.acf,text="Get a Job",command=lambda: self.work(ntime=None,working=True)).place(x=100,y=200)
            ttk.Button(self.acf,text="Quit your Job",command=lambda: self.work(ntime=None,working=False)).place(x=210,y=200)

        else:pass

        if dtp is None:
            pass
        else: self.dtp = dtp


    def work(self,ntime=0,hour=None,working=None):
        if working is True:
            self.working = True
        else:
            if working is False:
                self.working = False
        print(f"Currently it is {hour} hour late and {ntime} seconds passed also here is the array {self.dtp}")
        if self.working is True:
            try:
                if ntime is None:
                    self.logger.insert(tk.END, f"You started working\n")

                self.ct = self.ct + ntime

                while self.ct >= 60 * 60:
                    if self.dtp[hour] == 1:
                        self.user_coins += 2
                    self.ct -= 60 * 60
                    hour = (hour + 1) % 24
            except: pass

        else:
            if ntime is None:
                self.logger.insert(tk.END, f"You stopped working\n")

        try:
            self.coin.config(text=f"Coins: {self.user_coins}")
        except:
            pass


    def count_item(self, amount=0, g=False,): #g = get/buy
        curItem = self.trade_tree.focus()
        name = self.trade_tree.item(curItem)["text"]
        gtc = self.trade_tree.parent(curItem)
        wit = self.trade_tree.parent(gtc)
        wit_name = self.trade_tree.item(wit)["text"]

        if wit_name == "Seller Inventory":
            seller = self.seller_inf
            sel_coins = self.seller_coins
            buyer = self.user_items
            buy_coins = self.user_coins
        else:
            seller = self.user_items
            sel_coins = self.user_coins
            buyer = self.seller_inf
            buy_coins = self.seller_coins

        seller,buyer,sel_coins,buy_coins,message = self.inv.count_item(seller,buyer,name,amount,sel_coins,buy_coins)
        print(message,sel_coins,buy_coins)
        if wit_name == "Seller Inventory":

            self.seller_coins = sel_coins
            self.user_coins = buy_coins
        else:
            self.user_coins = sel_coins
            self.seller_coins = buy_coins

        self.logger.insert(tk.END, f"{message}")
        self.marketplace()


    def close_inv(self):
        self.canvas.grab_release()
        self.canvas.destroy()
        self.parent.focus_set()
