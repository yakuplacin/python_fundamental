accountYakup = {
    "name": "Yakup LAÇIN",
    "accountNo": "1232341",
    "cash": 3000,
    "additionalAccount": 2000
}

# Here, for example, instead of sending normal paramter like name="Yakup" would be problem!!
# Because, in python, you cannot change global values inside a function if you do not mention it as global.
# Instead, use objects like this. Python will give them an address and you will change their values that is referenced by that address!

accountGözde = {
    "name": "Gözde AĞAR",
    "accountNo": "12323432",
    "cash": 2000,
    "additionalAccount": 1000
}


def takeMoney(account, money):
    print(f"Hello {account['name']}")

    if (account["cash"] >= money):
        account['cash'] -= money
        print("You can take the money!")
        askMoney(account)

    else:
        total = account["cash"] + account["additionalAccount"]

        if (total >= money):
            wantedAdditionalAccount = input(
                "Allow to use additional account: (y / n) ")

            if (wantedAdditionalAccount == "y"):
                additionalAccountUsed = money - account["cash"]
                account["cash"] = 0
                account["additionalAccount"] -= additionalAccountUsed
                print("You can take your money")
                askMoney(account)

            else:
                print(
                    f"{account['accountNo']} in this account you have {account['cash']} money.")

        else:
            print("Not enough money!")
            askMoney(account)


def askMoney(account):
    print(f'{account["accountNo"]} in this account, you have {account["cash"]} money and Additional limit is: {account["additionalAccount"]}')


takeMoney(accountYakup, 3000)
takeMoney(accountYakup, 2000)
askMoney(accountYakup)
