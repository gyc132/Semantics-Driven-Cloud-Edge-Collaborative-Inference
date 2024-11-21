import csv
import numpy as np
import matplotlib.pyplot as plt

file_names = ['/Users/beibei/PycharmProjects/semantic-draw/data/data_hyperlpr.csv',
              '/Users/beibei/PycharmProjects/semantic-draw/data/data_yolo5_crnn.csv',
              '/Users/beibei/PycharmProjects/semantic-draw/data/data_mtcnn_lprnet.csv']

all_time_intervals = []
all_utilizations = []

for file_name in file_names:
    time_intervals = []
    utilizations = []

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        for row in csv_reader:
            time_intervals.append(row[0])
            utilizations.append(float(row[8]))

    all_time_intervals.append(time_intervals[0:1001])
    all_utilizations.append(utilizations[0:1001])

plt.figure(figsize=(10,5))

for time_intervals, utilizations in zip(all_time_intervals, all_utilizations):
    plt.plot(time_intervals, utilizations, linewidth=0.5)

tick_positions = np.arange(0, 1001, 200)
tick_labels = [f'{t}' for t in tick_positions]

plt.xticks(tick_positions, tick_labels)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.xlabel('Time Interval (ms)', fontsize=18)
plt.ylabel('Cloud GPU Utilization', fontsize=18)

legend_labels = ["hyperlpr", "yolov5", "mtcnn"]
plt.legend(legend_labels, fontsize=10)

plt.grid(True)
plt.savefig("utilization_cloud.pdf", format="pdf", bbox_inches="tight")

plt.show()
