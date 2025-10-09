from abc import ABC


class Phone:
    def __init__(self):
        self.__data = ""

    def params_info(self, data: str):
        self.__data += data

    def about_info(self):
        print(self.__data)


class IBuilder(ABC):
    def create_box(self):
        pass

    def create_chip(self):
        pass

    def create_os(self):
        pass

    def phone_info(self):
        pass


class IphoneBuilder(IBuilder):
    def __init__(self):
        self.__phone = Phone()

    def create_box(self):
        self.__phone.params_info("Create Iphone Box\n")

    def create_chip(self):
        self.__phone.params_info("Create Iphone Chip\n")

    def create_os(self):
        self.__phone.params_info("Create Iphone OS\n")

    def phone_info(self):
        self.__phone.about_info()


class SamsungBuilder(IBuilder):
    def __init__(self):
        self.__phone = Phone()

    def create_box(self):
        self.__phone.params_info("Create Samsung Box\n")

    def create_chip(self):
        self.__phone.params_info("Create Samsung Chip\n")

    def create_os(self):
        self.__phone.params_info("Create Samsung OS\n")

    def phone_info(self):
        self.__phone.about_info()




class DirectorBuilder(IBuilder):
    def __init__(self, builder: IBuilder):
        self.builder = builder

    def set_builder(self, builder: IBuilder):
        self.builder = builder

    def build_all_phone(self):
        self.builder.create_box()
        self.builder.create_chip()
        self.builder.create_os()

    def build_phone_without_os(self):
        self.builder.create_box()
        self.builder.create_chip()


if __name__ == 'main':
    iphone_builder = IphoneBuilder()
    director = DirectorBuilder(builder=iphone_builder)
    director.build_phone_without_os()
    iphone_builder.phone_info()
    samsung_builder = SamsungBuilder()
    director.set_builder(builder=samsung_builder)
    director.build_all_phone()
    samsung_builder.phone_info()