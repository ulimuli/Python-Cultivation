import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


#maybe use a notebook tkk widget for better looks?


class Inv_system:
    def __init__(self):
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
        self.Items = None
        self.coins = None

    def create_ui(self, parent, item, coins):
        self.parent = parent
        self.Items = item
        self.coins = coins

        self.canvas = tk.Canvas(self.parent)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.inv_canvas = tk.Canvas(
            self.canvas,
            height=500,
            width=700,
        )
        self.inv_canvas.place(x=0, y=100)
        self.parent.bind("<Escape>", lambda e: self.close_inv())
        exit_btn = tk.Button(self.canvas, text="X", command=lambda: self.close_inv())
        exit_btn.pack(side=tk.TOP, anchor="ne")
        self.cat()

    def cat(self):
        x = 50
        y = 25
        spa = 50

        buttons = []

        for i in self.Inv_Groups:
            img = Image.open(f"Images/{i['name']}.png")
            img = img.resize((48, 48), Image.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            btn = tk.Button(
                self.canvas,
                image=tk_img,
                command=lambda cat=i["name"]: self.inv_cat(cat)

            )
            btn.image = tk_img
            buttons.append(btn)
            btn.place(x=x, y=y)
            x += spa
            self.canvas.create_line(
                0, y + 65, 700, y + 65, fill="white"
            )
        self.inv_cat()

    def inv_cat(self, category="Everything"):
        list_start_x = 180
        list_start_y = 150
        list_gab_y = 35
        self.selected_category = category
        self.inv_canvas.delete("all")
        self.inv_canvas.create_text(

            100,
            10,
            text=category,
            font=("", 17,)
        )
        self.inv_canvas.create_text(

            80,
            80,
            text="Amount",
        )
        self.inv_canvas.create_text(

            list_start_x,
            80,
            text="Item",
        )
        self.inv_canvas.create_text(

            list_start_x + 200,
            80,
            text="Value",
        )
        self.inv_canvas.create_line(
            0, 90, 700, 90, fill="white"
        )
        self.inv_canvas.create_text(

            50,
            450,
            text=f"Coins: {self.coins}"
        )
        for i in self.Items:
            if category == "Everything" or i["category"] == category:
                if i["amount"] == 0:
                    pass
                else:
                    self.inv_canvas.create_text(

                        80,
                        list_start_y,
                        text=i["amount"],
                    )

                    self.inv_canvas.create_text(
                        list_start_x,
                        list_start_y,
                        text=i["item"]

                    )
                    self.inv_canvas.create_text(
                        list_start_x + 200,
                        list_start_y,
                        text=i["value"]

                    )
                    self.inv_canvas.create_line(
                        0, list_start_y + 15, 700, list_start_y + 15, fill="white"
                    )
                    list_start_y += list_gab_y

    def count_item(self,seller,buyer, name, amount=0, seller_coins=0, buyer_coins=0 ):
        message = ""
        for item in seller:
            if item["item"] == name:
                if amount is None:
                    amount = item["amount"]
                if item["value"]*amount <= buyer_coins:
                    item["amount"] -= amount
                    buyer_coins -= item["value"]*amount
                    seller_coins += item["value"]*amount
                    for d in buyer:
                        if d["item"] == name:
                            d["amount"] += amount
                            break
                    else:
                        new_item_add = item.copy()
                        new_item_add["amount"] = amount
                        buyer.append(new_item_add)
                    message = "Transaction complete\n"
                else:
                    message = "The Buyer does not have enough coins to buy this Item\n"

        return seller,buyer,seller_coins,buyer_coins,message

    def close_inv(self):
        self.canvas.grab_release()
        self.canvas.destroy()
        self.parent.focus_set()
