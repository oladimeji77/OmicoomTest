def email(old, current):
    if "@" + "gmail.com" in old:
        new = old.index("@")
        latest = old[:new] + current
        print(latest)
    else:
        print(current)

for i in ["afolawe@gmail.com", "okiki@gmail.com", "keji@gmail.com", "oladimeji@gmail.com"]:
    email( i, "@yahoo.com")


