from matplotlib import pyplot as plt
from src.functions import  parse_data, calc_percentile
from FCFS import FCFS
from SJF import SJF
from SRT import SRT
from HRRN import HRRN
from RR import RR
#from FB import FB


def main():
    choice = int(input("0: All graphs individually (large)\n1: All graphs in one plot (small)\n"))
    legend = ["FCFS", "SJF", "SRT", "HRRN", "RR (q=2)", "RR (q=4)", "RR (q=8)"]

    # FCFS
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    FCFS1 = calc_percentile(FCFS(data1))
    FCFS2 = calc_percentile(FCFS(data2))
    
    # SJF
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    SJF1 = calc_percentile(SJF(data1))
    SJF2 = calc_percentile(SJF(data2))

    # SRT
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    SRT1 = calc_percentile(SRT(data1))
    SRT2 = calc_percentile(SRT(data2))

    # HRRN
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    HRRN1 = calc_percentile(HRRN(data1))
    HRRN2 = calc_percentile(HRRN(data2))

    # RR
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    RR1_2 = calc_percentile(RR(data1, 2))
    RR2_2 = calc_percentile(RR(data2, 2))

    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    RR1_4 = calc_percentile(RR(data1, 4))
    RR2_4 = calc_percentile(RR(data2, 4))

    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    RR1_8 = calc_percentile(RR(data1, 8))
    RR2_8 = calc_percentile(RR(data2, 8))

    # TODO FB

    waiting_times1 = [FCFS1[0], SJF1[0], SRT1[0], HRRN1[0], RR1_2[0], RR1_4[0], RR1_8[0]]
    waiting_times2 = [FCFS2[0], SJF2[0], SRT2[0], HRRN2[0], RR2_2[0], RR2_4[0], RR2_8[0]]
    response_ratios1 = [FCFS1[1], SJF1[1], SRT1[1], HRRN1[1], RR1_2[1], RR1_4[1], RR1_8[1]]
    response_ratios2 = [FCFS2[1], SJF2[1], SRT2[1], HRRN2[1], RR2_2[1], RR2_4[1], RR2_8[1]]


    x = range(1, 101)

    if choice:
        figure, axis = plt.subplots(2, 2)
    
        # Waiting times 10.000 processen
        for i in waiting_times1:
            axis[0, 0].plot(x, i)
        axis[0, 0].set_xlabel("Service time in percentiles")
        axis[0, 0].set_ylabel("Waiting time")
        axis[0, 0].set_ylim([0, 20])
        axis[0, 0].legend(legend)
        axis[0, 0].set_title("10.000 processes")

        # Waiting times 20.000 processen
        for i in waiting_times2:
            axis[0, 1].plot(x, i)
        axis[0, 1].set_xlabel("Service time in percentiles")
        axis[0, 1].set_ylabel("Waiting time")
        axis[0, 1].set_ylim([0, 20])
        axis[0, 1].legend(legend)
        axis[0, 1].set_title("20.000 processes")

        # Response ratios 10.000 processen
        for i in response_ratios1:
            axis[1, 0].plot(x, i)
        axis[1, 0].set_xlabel("Service time in percentiles")
        axis[1, 0].set_ylabel("Response ratio")
        axis[1, 0].set_ylim([0, 1000])
        axis[1, 0].legend(legend)

        # Response ratios 20.000 processen
        for i in response_ratios2:
            axis[1, 1].plot(x, i)
        axis[1, 1].set_xlabel("Service time in percentiles")
        axis[1, 1].set_ylabel("Response ratio")
        axis[1, 1].set_ylim([0, 1000])
        axis[1, 1].legend(legend)

        # Combine all the operations and display
        figure.suptitle("CPU Scheduling exercise (full screen this window)")
        plt.show()

    else:
        # Waiting times 10.000 processen
        for i in waiting_times1:
            plt.plot(x, i)
        plt.xlabel("Service time in percentiles")
        plt.ylabel("Waiting time")
        plt.ylim([0, 20])
        plt.legend(legend)
        plt.title("10.000 processes waiting time")
        plt.show()

        # Waiting times 20.000 processen
        for i in waiting_times2:
            plt.plot(x, i)
        plt.xlabel("Service time in percentiles")
        plt.ylabel("Waiting time")
        plt.ylim([0, 20])
        plt.legend(legend)
        plt.title("20.000 processes waiting time")
        plt.show()

        # Response ratios 10.000 processen
        for i in response_ratios1:
            plt.plot(x, i)
        plt.xlabel("Service time in percentiles")
        plt.ylabel("Response ratio")
        plt.ylim([0, 1000])
        plt.legend(legend)
        plt.title("10.000 processes response ratio")
        plt.show()

        # Response ratios 20.000 processen
        for i in response_ratios2:
            plt.plot(x, i)
        plt.xlabel("Service time in percentiles")
        plt.ylabel("Response ratio")
        plt.ylim([0, 1000])
        plt.legend(legend)
        plt.title("10.000 processes response ratio")
        plt.show()


if __name__ == "__main__":
    main()
