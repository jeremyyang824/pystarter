import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 绘制图形
    fig = plt.figure(dpi=128, figsize=(8, 5))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形格式
    plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()  # 绘制斜向日期标签
    plt.ylabel('Temperature (F)', fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()
