from utills import get_gas_price, get_watt_price


class Car:
    def __init__(self, name: str, price: int, fluel_economy: float, service_cost: int):
        self.name = name
        self.price = price
        self.fluel_economy = fluel_economy
        self.service_cost = service_cost

    def year_cost(self, milleage: int):
        return self.service_cost + self.fluel_cost(milleage)

    def fluel_cost(self, milleage: int):
        return milleage * self.fluel_economy / 100 * get_gas_price()

    def total_cost(self, milleage: int, years: int):
        return self.price + years * self.fluel_cost(milleage)


class ElectroCar(Car):
    def __init__(self, name: str, price: int, power_consumption: int, service_cost: int = 0):
        super().__init__(name, price, 0, service_cost)
        self.power_consumption = power_consumption  # wt/1km

    def fluel_cost(self, milleage: int):
        return milleage * self.power_consumption * get_watt_price()


if __name__ == "__main__":
    toyote = Car("Toyota Corolla", price=7800, fluel_economy=11, service_cost=2000)

    prius = Car("prius", price=10000, fluel_economy=7, service_cost=2400)

    tesla = ElectroCar("Tesla", price=300000, power_consumption=150)

    print(toyote.total_cost(10000, years=3))
    print(prius.total_cost(10000, years=3))
    print(tesla.total_cost(10000, years=3))
