import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "Analisis de datos/csv/data/sitka_weather_2018_simple.csv"

with open(filename) as file:
    reader =csv.reader(file)
    next(reader)

    #print(header)
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        dates.append(current_date)
        high = int(row[-2])
        highs.append(high)
    
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(dates, highs, c='red')

    ax.set_title("Yearly_high temperatures, 2018", fontsize=24)
    ax.set_xlabel("")
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=15)

    plt.show()
