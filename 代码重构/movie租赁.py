# https://www.jianshu.com/p/b0b0fa7cabdc


class Movie:
    """ 影片类，一个单纯的数据类

    :param title: string, 影片标题
    :param price_code: int, 影片的计价类型
    """

    CHILDRENS = 2  # 儿童片
    REGULAR = 0  # 普通片
    NEW_REALEASE = 1  # 新片

    def __init__(self, title, price_code):
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        return self.price_code

    def set_price_code(self, arg):
        self.price_code = arg

    def get_title(self):
        return self.title


class Rental:
    """ 租赁类，表示某个顾客租了一部影片

    :param movie: object, Movie类
    :days_rented: int, 租期
    """

    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def get_days_rented(self):
        return self.days_rented

    def get_movie(self):
        return self.movie


class Customer:
    """ 顾客类，存放每个顾客租赁信息的列表

    :param name: 顾客姓名
    """

    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        """ 增加一条租赁信息

        :param rental: object, Rental类
        """
        self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        """ 生成详单的函数 """
        total_amount = 0.0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"
        for retal in self.rentals:
            this_amount = 0

            # 计算每部影片的价格
            if retal.get_movie().get_price_code() == Movie.REGULAR:
                this_amount += 2
                if retal.get_days_rented() > 2:
                    this_amount += (retal.get_days_rented() - 2) * 1.5
            elif retal.get_movie().get_price_code() == Movie.NEW_REALEASE:
                this_amount += retal.get_days_rented() * 3
            elif retal.get_movie().get_price_code() == Movie.CHILDRENS:
                this_amount += 1.5
                if retal.get_days_rented() > 3:
                    this_amount += (retal.get_days_rented() - 3) * 1.5

            # 计算常客积分
            frequent_renter_points += 1
            # 新片租赁两天以上会有额外的积分奖励
            if retal.get_movie().get_price_code() == Movie.NEW_REALEASE and \
                    retal.get_days_rented() > 1:
                frequent_renter_points +=  1

            # 展示一条影片租赁的详情
            result += "\t" + retal.get_movie().get_title() + "\t" \
                + str(this_amount) + "\n"

            total_amount += this_amount

        # 汇总信息
        result += "Amount owned is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) \
            + " frequent renter points"
        return result

def test():
    c_movie = Movie("CHILDRENS", Movie.CHILDRENS)
    r_movie = Movie("REGULAR", Movie.REGULAR)
    n_movie = Movie("NEW_REALEASE", Movie.NEW_REALEASE)

    c_rental = Rental(c_movie, 20)
    r_rental = Rental(r_movie, 20)
    n_rental = Rental(n_movie, 20)

    customer = Customer("CUSTOMER")
    customer.add_rental(c_rental)
    customer.add_rental(r_rental)
    customer.add_rental(n_rental)

    result = customer.statement()

    print(result)


if __name__ == "__main__":
    test()


# final version

class Movie:
    """ 影片类，一个单纯的数据类

    :param title: string, 影片标题
    :param price_code: int, 影片的计价类型
    """

    CHILDRENS = 2  # 儿童片
    REGULAR = 0  # 普通片
    NEW_REALEASE = 1  # 新片

    def __init__(self, title, price_code):
        self.title = title
        self.set_price_code(price_code)

    def get_price_code(self):
        return self.price.get_price_code()

    def set_price_code(self, arg):
        if arg == self.REGULAR:
            self.price = RegularPrice()
        elif arg == self.NEW_REALEASE:
            self.price = NewReleasePrice()
        elif arg == self.CHILDRENS:
            self.price = ChildrensPrice()
        else:
            raise AttributeError("Incorrect Price Code")

    def get_title(self):
        return self.title

    def get_charge(self, days_rented):
        """ 计算租赁一部影片多少天的价格

        :param days_rented: int, 租赁天数
        :rtype: float
        """
        return self.price.get_charge(days_rented)

    def get_frequent_renter_point(self, days_rented):
        """ 计算租赁一部影片多少天的常客积分

        :param days_rented: int, 租赁天数
        :rtype: int
        """
        return self.price.get_frequent_renter_point(days_rented)


class Price:
    """ 抽象类，由于鸭子类型的关系，完全可以让子类不继承这个类 """
    def get_price_code(self):
        """ 抽象函数，获取价格码

        :rtype: int
        """
        raise NotImplementedError

    def get_charge(self, days_rented):
        """ 计算租赁一部影片多少天的价格

        :param days_rented: int, 租赁天数
        :rtype: float
        """
        raise NotImplementedError

    def get_frequent_renter_point(self, days_rented):
        """ 默认租一次加一分 """
        return 1


class ChildrensPrice(Price):
    def get_price_code(self):
        return Movie.CHILDRENS

    def get_charge(self, days_rented):
        """ 计算租赁一部影片多少天的价格

        :param days_rented: int, 租赁天数
        :rtype: float
        """
        result = 1.5
        if days_rented > 3:
            result += (days_rented - 3) * 1.5
        return result


class NewReleasePrice(Price):
    def get_price_code(self):
        return Movie.NEW_REALEASE

    def get_charge(self, days_rented):
        """ 计算租赁一部影片多少天的价格

        :param days_rented: int, 租赁天数
        :rtype: float
        """
        return days_rented * 3

    def get_frequent_renter_point(self, days_rented):
        """ 新片超过一天加两分，覆盖了父类的方法 """
        if days_rented > 1:
            return 2
        return 1


class RegularPrice(Price):
    def get_price_code(self):
        return Movie.REGULAR

    def get_charge(self, days_rented):
        """ 计算租赁一部影片多少天的价格

        :param days_rented: int, 租赁天数
        :rtype: float
        """
        result = 2
        if days_rented > 2:
            result += (days_rented - 2) * 1.5
        return result


class Rental:
    """ 租赁类，表示某个顾客租了一部影片

    :param movie: object, Movie类
    :days_rented: int, 租期
    """

    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def get_days_rented(self):
        return self.days_rented

    def get_movie(self):
        return self.movie

    def get_charge(self):
        return self.get_movie().get_charge(self.get_days_rented())

    def get_frequent_renter_point(self):
        """ 计算常客积分 """
        return self.get_movie().get_frequent_renter_point(self.get_days_rented())


class Customer:
    """ 顾客类，存放每个顾客租赁信息的列表

    :param name: 顾客姓名
    """

    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        """ 增加一条租赁信息

        :param rental: object, Rental类
        """
        self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        """ 生成详单的函数

        rtype: string
        """
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"
        for retal in self.rentals:
            # 展示一条影片租赁的详情
            result += "\t" + retal.get_movie().get_title() + "\t" \
                + str(retal.get_charge()) + "\n"

        # 汇总信息
        result += "Amount owned is " + str(self.get_total_charge()) + "\n"
        result += "You earned " + str(self.get_total_frequent_renter_point()) \
            + " frequent renter points"
        return result

    def get_total_charge(self):
        """ 计算顾客消费总金额

        :rtype: float
        """
        result = 0.0
        for rental in self.rentals:
            result += rental.get_charge()
        return result

    def get_total_frequent_renter_point(self):
        """ 计算常客积分的总量

        :rtype: int
        """
        result = 0
        for rental in self.rentals:
            result += rental.get_frequent_renter_point()
        return result


def test():
    c_movie = Movie("CHILDRENS", Movie.CHILDRENS)
    r_movie = Movie("REGULAR", Movie.REGULAR)
    n_movie = Movie("NEW_REALEASE", Movie.NEW_REALEASE)

    c_rental = Rental(c_movie, 20)
    r_rental = Rental(r_movie, 20)
    n_rental = Rental(n_movie, 20)

    customer = Customer("CUSTOMER")
    customer.add_rental(c_rental)
    customer.add_rental(r_rental)
    customer.add_rental(n_rental)

    result = customer.statement()

    print(result)


if __name__ == "__main__":
    test()