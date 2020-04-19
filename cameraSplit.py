def get_dates(file):
    fileSplit = file.split("_")
    dateList = list()
    year = fileSplit[1][:4]
    dateList.append(year)
    month = fileSplit[1][4:6]
    dateList.append(month)
    day = fileSplit[1][6:9]
    dateList.append(day)
    return dateList


def get_date_II(file):
    date = file.split('_')[1]
    year, month, day = date[:4], date[4:6], date[6:]
    return year, month, day


if __name__ == '__main__':
    file = "IMG_20180825_122319.jpg"
    print(get_dates(file))
    print(get_date_II(file))
