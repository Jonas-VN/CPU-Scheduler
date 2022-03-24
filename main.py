from matplotlib import pyplot as plt
from src.functions import parse_data, visualize_data
from FCFS import FCFS
from SJF import SJF
from HRRN import HRRN

#data = parse_data('processen10000.xml')
#hrrn = HRRN(data, True)
data = parse_data('processen10000.xml')
fcfs = FCFS(data)
data = parse_data('processen10000.xml')
sjf = SJF(data)

visualize_data(fcfs, "red", "FCFS")
visualize_data(sjf, "blue", "SJF")
#visualize_data(hrrn, "orange", "HRRN")
plt.legend(loc = "upper right")
plt.xlabel("Service time")
plt.ylabel("Response ratio")
plt.show()