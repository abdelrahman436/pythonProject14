from string import Template


class MyTemplate(Template):
    delimiter = '#'


def Main():
    cart = []
    cart.append(dict(item="desk", price=12, qty=3))
    cart.append(dict(item="chair", price=96, qty=2))
    cart.append(dict(item="notebooks", price=45, qty=2))
    cart.append(dict(item="pencils", price=24, qty=1))
    cart.append(dict(item="stapler", price=7, qty=1))
    cart.append(dict(item="scissors", price=65, qty=1))
    cart.append(dict(item="compass", price=8, qty=1))
    cart.append(dict(item="ballpoints", price=65, qty=2))
    cart.append(dict(item="calculator", price=84, qty=1))
    cart.append(dict(item="palette", price=1944, qty=2))

    t = MyTemplate("#qty x #item = #price")
    total = 0
    print("Cart:")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("Total: " + str(total))


if __name__ == '__main__':
    Main()

