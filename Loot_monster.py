class Loot_monster:
    def __init__(self, info_loot):
        self.name = info_loot["name"]
        self.quantity = info_loot["quantity"]
        self.rate = info_loot["rate"]

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    def get_rate(self):
        return self.rate