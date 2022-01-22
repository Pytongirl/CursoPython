import csv
import matplotlib.pyplot as plt

filename = "Analisis de datos/csv/data/sitka_wheather.csv"

with open(filename) as file:
    reader =csv.reader(file)
    header =next(reader)

    #print(header)
    highs = []
    for row in reader:
        high = int(row[-2])
        highs.append(high)
    
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(highs, c='red')

    ax.set_title("Daily_high temperatures, July 2018, fontsize=24")
    ax.set_xlabel("")
    ax.set_ylabel("Temperature (F)", fontsize=15)
    plt.show()
     
