import csv
import matplotlib.pyplot as plt

# Initialize lists to store data
# img_size(KB)：原始图片大小
# end_edge_time ：端到边传输时间
# edge_cloud_time ：边到云传输时间
# plate_size ：分割后图片大小
# seg_edge_cloud_time：分割后边到云传输时间
# cloud_all_processing_time ：云上分割+识别时间
# cloud_gpu_rec_time ：云上识别时间
# cloud_gpu_utilization ：云上GPU利用率
# edge_cpu_det_time ：边上CPU检测时间
# edge_cpu_percent ：边上CPU利用率
# no_seg_time ：不在边上做语义分割的总处理时间
# after_seg_time：在边上做语义分割的总处理时间

original_size = []
after_segmentation_size = []

# Read data from CSV file
with open('/Users/beibei/PycharmProjects/semantic-draw/data/data_mtcnn_lprnet.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row

    for row in csv_reader:
        original_size.append(float(row[1]))  # Ninth column (index 8) contains the original time
        after_segmentation_size.append(float(row[4]))  # Tenth column (index 9) contains the after segmentation time

cloud_size = [2*x for x in original_size]
after_segmentation_size = [sum(x) for x in zip(original_size, after_segmentation_size)]
# Plot the boxplot
data_to_plot = [cloud_size, after_segmentation_size]
labels = ['w/o \n segmantation', 'after \n segmentation']

plt.figure(figsize=(5, 10))
plt.boxplot(data_to_plot)
plt.xticks([1, 2], labels, fontsize=18)
plt.yticks(fontsize=14)

# plt.xlabel('Time')
plt.ylabel('Total Data Transmission Size (KB)', fontsize=18)
# plt.title('Transmission Time Comparison')
plt.grid(True)
plt.savefig("transmission_mtcnn.pdf", format="pdf", bbox_inches="tight")

plt.show()
