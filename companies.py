from products import RoadBase265

dict_of_products = {
    "RoadBase265": RoadBase265,

}


class Company:

    #  Здесь вводятся реквизиты компании из карточки партнёра
    #  От этого класса, по замыслу, будет наследоваться класс Horda (название компании)

    def __int__(
            self,
            legal_address: str = None,
            mailing_address: str = None,
            contact_numbers: str = None,
            INN: str = None,
            KPP: str = None,
            bank: str = None,
            checking_account: str = None,
            corr_account: str = None,
            bik: str = None,
            post_code: str = None
    ):
        self.legal_address = legal_address
        self.mailing_address = mailing_address
        self.contact_numbers = contact_numbers
        self.INN = INN
        self.KPP = KPP
        self.bank = bank
        self.checking_account = checking_account
        self.corr_account = corr_account
        self.bik = bik
        self.post_code = post_code

    @property
    def get_legal_address(self):
        return self.legal_address

    @property
    def get_mailing_address(self):
        return self.mailing_address

    @property
    def get_contact_numbers(self):
        return self.get_contact_numbers

    @property
    def get_contact_numbers(self):
        return self.contact_numbers


class Horda(Company):

    def buy_product(self, name: str, value: float = 10.1, price: float = 100000, unit: str = 'rub'):
        # в этом методе я покупаю продукт. Припокупки создаётся экземпляр класса и
        # все аргументы функции покупки передаются в __init__ в класс покупаемого продукта
        #
        # Сейчас тут представлен принцип работы этого замысла.

        # Также нужно продумать как сделать так что бы при вызове функции, он уже знал какие обекты уже сидят в учёте (учёт может
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
