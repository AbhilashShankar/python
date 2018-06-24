# what year were you born
# what month were you born
# what day were you born
# 2003,8,22
january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31
m=0

def get_days():
    if month == 8:
        m = 365 * (2018-(years+1)) + (august-days) + 30 + 31 + 30 + 31 + 174 + 4
        print(m)

if __name__  == "__main__":
    years = input("What year were you born")
    month = input("What month were you born")
    days = input("What day were you born")
    get_days()
