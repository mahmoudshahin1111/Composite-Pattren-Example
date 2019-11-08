import random


class Product(object):
    def __init__(self):
        self.code = random.randint(1000, 2000)
        self.price = random.randint(100, 200)

    def getPrice(self):
        return self.price

    def getCode(self):
        return self.code

    def __str__(self):
        return "Product => Price : "+str(self.price)+"|"+"Code : "+str(self.code)

    def getType(self):
        return type(self).__name__


class Box(object):
    def __init__(self):
        self.code = random.randint(3000, 4000)
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def getCode(self):
        return self.code

    def getPrice(self):
        price = 0
        for item in self.items:
            price += item.getPrice()
        return price
    def __str__(self):
        price = self.getPrice();
        return "Box => Code :"+str(self.code)+"|"+"Price :"+str(price);

main_box = Box();
b1 = Box();
p1 = Product();
p2 = Product();
b1.add(p1);
b1.add(p2);
main_box.add(b1);
print(b1);

b2 = Box();
p3 = Product();
p4 = Product();
b2.add(p3);
b2.add(p4);
main_box.add(b2);
print(b2);
print("====== Total =======");
print(main_box);
