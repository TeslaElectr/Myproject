from products import RoadBase265

dict_of_products = {
    "RoadBase265": RoadBase265,

}


class Company:

    #  Здесь вводятся реквизиты компании из карточки партнёра
    #  От этого класса, по замыслу, будет наследоваться класс Horda (название компании)
    #
    #

    def __int__(self):
        pass


class Horda(Company):

    def __int__(self):
        pass

    def buy_product(self, name: str, value: float = 10.1, price: float = 100000, unit: str = 'rub'):
        # в этом методе я покупаю продукт. Припокупки создаётся экземпляр класса и
        # все аргументы функции покупки передаются в __init__ в класс покупаемого продукта
        #
        # Сейчас тут представлен принцип работы этого замысла.

        # Также нужно продукмать как сделать так что бы при вызове функции, он уже знал какие обекты уже сидят в учёте (учёт может
        # быть любой: списки, словари, бд (БД я еще не умею))
        product_object = dict_of_products[name]
        exit = product_object.produce(product_object)
        return exit

    def get_paid(self):
        pass


def main():
    horda = Horda
    return print(horda.buy_product(horda, 'RoadBase265'))


if __name__ == '__main__':
    main()
