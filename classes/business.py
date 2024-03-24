class Business:
    def __init__(self, name, base_price, cookies_per_second, multiplier):
        self.name = name
        self.base_price = base_price
        self.cookies_per_second = cookies_per_second
        self.multiplier = multiplier
        self.count = 0

    def calculate_cps(self):
        return self.cookies_per_second * self.count


class Grandma(Business):
    def __init__(self):
        super().__init__("Babička", 100, 2, 2)

    def buy_button(self, cookies_count):
        if self.count == 0 and cookies_count >= self.base_price:
            cookies_count -= self.base_price
            self.count += 1
        elif self.count > 0 and cookies_count >= self.base_price * self.count * self.multiplier:
            cookies_count -= self.base_price * self.multiplier * self.count
            self.count += 1
class Owen(Business):
    def __init__(self):
        super().__init__("Trouba", 500, 5, 2)

    def buy_button(self, cookies_count):
        if self.count == 0 and cookies_count >= self.base_price:
            cookies_count -= self.base_price
            self.count += 1
        elif self.count > 0 and cookies_count >= self.base_price * self.count * self.multiplier:
            cookies_count -= self.base_price * self.multiplier * self.count
            self.count += 1


class Kiln(Business):
    def __init__(self):
        super().__init__("Pec", 2000, 15, 3)

    def buy_button(self, cookies_count):
        if self.count == 0 and cookies_count >= self.base_price:
            cookies_count -= self.base_price
            self.count += 1
        elif self.count > 0 and cookies_count >= self.base_price * self.count * self.multiplier:
            cookies_count -= self.base_price * self.multiplier * self.count
            self.count += 1


class Bakery(Business):
    def __init__(self):
        super().__init__("Pekárna", 10000, 40, 3)

    def buy_button(self, cookies_count):
        if self.count == 0 and cookies_count >= self.base_price:
            cookies_count -= self.base_price
            self.count += 1
        elif self.count > 0 and cookies_count >= self.base_price * self.count * self.multiplier:
            cookies_count -= self.base_price * self.multiplier * self.count
            self.count += 1


class Sweet_shop(Business):
    def __init__(self):
        super().__init__("Cukrárna", 50000, 100, 3)

    def buy_button(self, cookies_count):
        if self.count == 0 and cookies_count >= self.base_price:
            cookies_count -= self.base_price
            self.count += 1
        elif self.count > 0 and cookies_count >= self.base_price * self.count * self.multiplier:
            cookies_count -= self.base_price * self.multiplier * self.count
            self.count += 1


class Donut(Business):
    def __init__(self):
        super().__init__("Koblihárna", 300000, 250, 4)

    def buy_button(self, cookies_count):
        if self.count == 0 and cookies_count >= self.base_price:
            cookies_count -= self.base_price
            self.count += 1
        elif self.count > 0 and cookies_count >= self.base_price * self.count * self.multiplier:
            cookies_count -= self.base_price * self.multiplier * self.count
            self.count += 1


class Cake(Business):
    def __init__(self):
        super().__init__("Dortovna", 1000000, 600, 4)

    def buy_button(self, cookies_count):
        if self.count == 0 and cookies_count >= self.base_price:
            cookies_count -= self.base_price
            self.count += 1
        elif self.count > 0 and cookies_count >= self.base_price * self.count * self.multiplier:
            cookies_count -= self.base_price * self.multiplier * self.count
            self.count += 1


class Cracker(Business):
    def __init__(self):
        super().__init__("Sušenky", 5000000, 1500, 5)

    def buy_button(self, cookies_count):
        if self.count == 0 and cookies_count >= self.base_price:
            cookies_count -= self.base_price
            self.count += 1
        elif self.count > 0 and cookies_count >= self.base_price * self.count * self.multiplier:
            cookies_count -= self.base_price * self.multiplier * self.count
            self.count += 1