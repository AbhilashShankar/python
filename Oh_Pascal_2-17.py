def get_cashdifference(second_price, first_price):
    cash_difference = (second_price - first_price)
    return cash_difference


def get_percentageincrease(cash_difference,first_price):
    return (float(cash_difference) / float(first_price)) * 100


# def get_yearlyinterestgain():
#     years = input("What is the year difference:")
#     print((((float(second_price) - float(first_price)) / float(first_price)) * 100 / years))


if __name__ == '__main__':
    first_price = input("What is the price of your first item:")
    second_price = input("What is the price of your second item:")
    cash_difference = get_cashdifference(second_price, first_price)
    print("The item gained ${}".format(cash_difference))
    percentage_increase = get_percentageincrease(cash_difference, first_price)
    print("The item's price inceased by {}%".format(percentage_increase))
