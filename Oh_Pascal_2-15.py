def get_total(purchase_price):
    markup_tax = (purchase_price * 0.40)
    markup_price = markup_tax + purchase_price
    sales_tax = markup_price * 0.055
    total_price = markup_price + sales_tax
    print(total_price)



if __name__ == '__main__':
    purchase_price = input("What is your purchase price: ")
    get_total(purchase_price)