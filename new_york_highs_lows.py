import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename='New_York_2022-01-04.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    #从文件中获取最高温度和日期、最低温度
    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#根据最高温度绘制图形
plt.style.use('seaborn')
fig, ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#设置图形的格式
ax.set_title('2022/01-04 temperature for New York',fontsize=20)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("temperature(F)",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.show()