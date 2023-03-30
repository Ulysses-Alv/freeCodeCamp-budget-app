class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        new_amount = amount * -1
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": new_amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total_amount = 0
        for item in self.ledger:
            total_amount += item["amount"]
        return total_amount

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(other_category.name))
            other_category.deposit(
                amount, "Transfer from {}".format(self.name))
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        my_string = self.name
        title_line = my_string.center(30, "*")
        console_print = title_line + "\n"
        for transaction in self.ledger:
            amount_str = "{:.2f}".format(transaction["amount"])
            amount_str = amount_str[:7]
            description_str = transaction["description"][:23]
            console_print += description_str.ljust(23) + \
                amount_str.rjust(7) + "\n"
        console_print += "Total: " + str(self.get_balance())
        return console_print


def create_spend_chart(categories=[]):
    header = "Percentage spent by category\n"
    bar_chart = create_bars_chart(percentage_of_usage(categories))
    separation_line = "----------".rjust(14)
    write_names = write_Names(obtain_names(categories))
    return (header + bar_chart + separation_line + write_names)


def create_bars_chart(categories):
    bar_char = ""
    position = 100
    for bar in create_bars():
        new_bar_one = ""
        new_bar_two = ""
        new_bar_three = ""
        new_bar_fourth = ""

        new_bar = ""
        for index, category in enumerate(categories):
            category_name = list(category.keys())[0]
            category_usage = category[category_name]
            if category_usage >= position:
                if index == 0:
                    new_bar_one += " o"
                elif index == 1:
                    new_bar_two += "  o"
                elif index == 2:
                    new_bar_three += "  o"
                elif index == 3:
                    new_bar_fourth += "  o"
            else:
                if index == 0:
                    new_bar_one += "  "
                elif index == 1:
                    new_bar_two += "   "
                elif index == 2:
                    new_bar_three += "   "
                elif index == 3:
                    new_bar_fourth += "   "
        new_bar = new_bar_one + new_bar_two + new_bar_three + new_bar_fourth
        bar_char += bar + new_bar + "\n"
        position -= 10

    return bar_char


def white_spaces(index, new_bar):
    white_spaces = " "
    if index == 1 and not "o" in new_bar:

        white_spaces = " "
        return white_spaces


def obtain_names(categories):
    return [objeto.name for objeto in categories]


def percentage_of_usage(categories):
    total_usage = 0
    list_categories_usage = []
    for category in categories:
        usage = amount_of_usage(category)
        list_categories_usage.append({f"{category.name}": usage})
        total_usage += usage

    list_categories_percentage = []
    for category in list_categories_usage:
        category_name = list(category.keys())[0]
        category_usage = list(category.values())[0]
        percentage = round_down((category_usage / total_usage) * 100)
        list_categories_percentage.append({category_name: percentage})
    return list_categories_percentage


def amount_of_usage(category):
    usage = 0
    for transaction in category.ledger:
        if transaction["amount"] < 0:
            usage += abs(transaction["amount"])
    return usage


def create_bars():
    percentage = 100
    list_percentage = []
    while percentage >= 0:
        list_percentage.append(str(percentage).rjust(3) + "|")
        percentage -= 10
    return list_percentage


def round_down(num):
    return num // 10 * 10


def write_Names(categories):
    lista = categories
    resultado = "\n"

    longitud_maxima = max([len(elemento) for elemento in lista])

    for i in range(longitud_maxima):
        resultado += "     "
        for elemento in lista:
            if i < len(elemento):
                resultado += elemento[i]
            else:
                resultado += " "
            resultado += "  "
        resultado += "\n"
    resultado = resultado.rstrip("\n")
    return resultado
