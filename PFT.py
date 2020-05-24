from tkinter import *
import requests
import json

pycrypto=Tk()
pycrypto.title("MY PORTFOLIO")
pycrypto.iconbitmap('favicon.ico')
def font_color(amount):
    if amount >=0:
        return "green"
    return "red"
def my_portfolio():
    api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=332c0fe8-fcfe-410a-a7bb-85c61fe285ff")
    api=json.loads(api_request.content)
    coins=[
        {
            "symbol":"BTC",
            "amount_owned":20000,
            "price_per_coin":32
        },
        {
            "symbol":"ETH",
            "amount_owned":10000,
            "price_per_coin":2
        },
        {
            "symbol":"USDT",
            "amount_owned":10,
            "price_per_coin":9
        },
        {
            "symbol":"XRP",
            "amount_owned":1,
            "price_per_coin":1
        }



    ]
    total_pl=0
    coin_row=1
    total_current_value=0
    for i in range (0,300):
        for coin in coins :
            if api["data"][i]["symbol"]==coin["symbol"]:
                total_paid=coin["amount_owned"]*coin["price_per_coin"]
                current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
                pl_percoin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
                total_pl_coin=pl_percoin*coin["amount_owned"]

                total_pl = total_pl + total_pl_coin
                total_current_value=total_current_value+current_value

                name = Label(pycrypto,text=api["data"][i]["symbol"],bg="#FFE5CC",fg="#000099",font="Helvetica 10 bold italic",padx="5" ,pady="5",borderwidth=2,relief="groove")
                name.grid(row=coin_row,column=0,sticky=N+S+E+W)

                price = Label(pycrypto,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),bg="#FFE5CC",fg="#000099",font="Helvetica 10 bold italic",padx="2" ,pady="2",borderwidth=2,relief="groove")
                price.grid(row=coin_row,column=1,sticky=N+S+E+W)

                no_coins = Label(pycrypto,text=coin["amount_owned"],bg="#FFE5CC",fg="#000099",font="Helvetica 10 bold italic",padx="2" ,pady="2",borderwidth=2,relief="groove")
                no_coins.grid(row=coin_row,column=2,sticky=N+S+E+W)

                amount_paid = Label(pycrypto,text="${0:0.2f}".format(total_paid),bg="#FFE5CC",fg="#000099",font="Helvetica 10 bold italic",padx="2" ,pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row,column=3,sticky=N+S+E+W)

                current_value = Label(pycrypto,text="${0:0.2f}".format(current_value),bg="#FFE5CC",fg="#000099",font="Helvetica 10 bold italic",padx="2" ,pady="2",borderwidth=2,relief="groove")
                current_value.grid(row=coin_row,column=4,sticky=N+S+E+W)

                pl_coin = Label(pycrypto,text="${0:0.2f}".format(pl_percoin),bg="#FFE5CC",fg="#000099",font="Helvetica 10 bold italic",padx="2" ,pady="2",borderwidth=2,relief="groove")
                pl_coin.grid(row=coin_row,column=5,sticky=N+S+E+W)

                totalpl = Label(pycrypto,text="${0:0.2f}".format(total_pl_coin),bg="#FFE5CC",fg=font_color(float("{0:0.2f}".format(total_pl_coin))),font="Helvetica 10 bold italic",padx="2" ,pady="2",borderwidth=2,relief="groove")
                totalpl.grid(row=coin_row,column=6,sticky=N+S+E+W)

                coin_row = coin_row + 1
    totalpl = Label(pycrypto,text="${0:0.2f}".format(total_pl),bg=font_color(float("{0:0.2f}".format(total_pl))),fg="#000099",font="Helvetica 10 bold italic",padx="2" ,pady="2",borderwidth=2,relief="groove")
    totalpl.grid(row=coin_row,column=6,sticky=N+S+E+W)

    totalcv = Label(pycrypto,text="${0:0.2f}".format(total_current_value),bg=font_color(float("{0:0.2f}".format(total_current_value))),fg="#000099",font="Helvetica 10 bold italic",padx="2" ,pady="2",borderwidth=2,relief="groove")
    totalcv.grid(row=coin_row,column=4,sticky=N+S+E+W)

    api = ""

    update = Button(pycrypto,text="Update",bg="#6666FF",fg="#000099",command=my_portfolio,font="Helvetica 10 bold italic",padx="2" ,pady="2",borderwidth=2,relief="groove")
    update.grid(row=coin_row,column=1,sticky=N+S+E+W)


name = Label(pycrypto,text="Coin Name",bg="#FFCC99",fg="#660033",font="Helvetica 10 bold italic",padx="5" ,pady="5",borderwidth=2,relief="groove")
name.grid(row=0,column=0,sticky=N+S+E+W)

price = Label(pycrypto,text="Price",bg="#FFCC99",fg="#660033",font="Helvetica 10 bold italic",padx="5" ,pady="5",borderwidth=2,relief="groove")
price.grid(row=0,column=1,sticky=N+S+E+W)

no_coins = Label(pycrypto,text="Coins Owned",bg="#FFCC99",fg="#660033",font="Helvetica 10 bold italic",padx="5" ,pady="5",borderwidth=2,relief="groove")
no_coins.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid = Label(pycrypto,text="Total Amount Paid",bg="#FFCC99",fg="#660033",font="Helvetica 10 bold italic",padx="5" ,pady="5",borderwidth=2,relief="groove")
name.grid(row=0,column=3,sticky=N+S+E+W)

current_value = Label(pycrypto,text="Current Value",bg="#FFCC99",fg="#660033",font="Helvetica 10 bold italic",padx="5" ,pady="5",borderwidth=2,relief="groove")
current_value.grid(row=0,column=4,sticky=N+S+E+W)

pl_coin = Label(pycrypto,text="P/L Per Coin",bg="#FFCC99",fg="#660033",font="Helvetica 10 bold italic",padx="5" ,pady="5",borderwidth=2,relief="groove")
pl_coin.grid(row=0,column=5,sticky=N+S+E+W)

total_pl = Label(pycrypto,text="Total P/L With Coin",bg="#FFCC99",fg="#660033",font="Helvetica 10 bold italic",padx="5" ,pady="5",borderwidth=2,relief="groove")
total_pl.grid(row=0,column=6,sticky=N+S+E+W)

my_portfolio()
pycrypto.mainloop()
print("Program Completed")
