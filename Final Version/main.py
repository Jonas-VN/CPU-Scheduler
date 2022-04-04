from matplotlib import pyplot as plt
from src.functions import parse_data, calc_percentile
from src.FCFS import FCFS
from src.SJF import SJF
from src.SRT import SRT
from src.HRRN import HRRN
from src.RR import RR
from src.FB import FB


def main():
    choice = int(input("0: All graphs individually (large)\n1: All graphs in one plot (small)\n"))

    # veranderen naar range(1, 11) om beter de tendenzen te kunnen zien
    x = range(1, 101)

    # FCFS
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    FCFS1 = calc_percentile(FCFS(data1), x)
    FCFS2 = calc_percentile(FCFS(data2), x)
    
    # SJF
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    SJF1 = calc_percentile(SJF(data1), x)
    SJF2 = calc_percentile(SJF(data2), x)

    # SRT
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    SRT1 = calc_percentile(SRT(data1), x)
    SRT2 = calc_percentile(SRT(data2), x)

    # HRRN
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    HRRN1 = calc_percentile(HRRN(data1), x)
    HRRN2 = calc_percentile(HRRN(data2), x)

    # RR
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    RR1_2 = calc_percentile(RR(data1, 2), x)
    RR2_2 = calc_percentile(RR(data2, 2), x)

    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    RR1_4 = calc_percentile(RR(data1, 4), x)
    RR2_4 = calc_percentile(RR(data2, 4), x)

    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    RR1_8 = calc_percentile(RR(data1, 8), x)
    RR2_8 = calc_percentile(RR(data2, 8), x)

    # FB
    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    quanta1 = [2, 4, 8, 16, 32]
    FB1_1 = calc_percentile(FB(data1, quanta1), x)
    FB2_1 = calc_percentile(FB(data2, quanta1), x)

    data1 = parse_data("processen10000.xml")
    data2 = parse_data("processen20000.xml")
    quanta2 = [4, 8, 16, 32, 64]
    FB1_2 = calc_percentile(FB(data1, quanta2), x)
    FB2_2 = calc_percentile(FB(data2, quanta2), x)

    waiting_times1 = [FCFS1[0], SJF1[0], SRT1[0], HRRN1[0], RR1_2[0], RR1_4[0], RR1_8[0], FB1_1[0], FB1_2[0]]
    waiting_times2 = [FCFS2[0], SJF2[0], SRT2[0], HRRN2[0], RR2_2[0], RR2_4[0], RR2_8[0], FB2_1[0], FB2_2[0]]
    response_ratios1 = [FCFS1[1], SJF1[1], SRT1[1], HRRN1[1], RR1_2[1], RR1_4[1], RR1_8[1], FB1_1[1], FB1_2[1]]
    response_ratios2 = [FCFS2[1], SJF2[1], SRT2[1], HRRN2[1], RR2_2[1], RR2_4[1], RR2_8[1], FB2_1[1], FB2_2[1]]

    legend = ["FCFS", "SJF", "SRT", "HRRN", "RR (q=2)", "RR (q=4)", "RR (q=8)", f"FB {quanta1}", f"FB {quanta2}"]

    if choice:
        figure, axis = plt.subplots(2, 2)
    
        # Waiting times 10.000 processen
        [axis[0, 0].plot(x, i) for i in waiting_times1]
        axis[0, 0].set_xlabel("Service time in percentiles")
        axis[0, 0].set_ylabel("Waiting time")
        axis[0, 0].set_ylim([0, 2000])
        axis[0, 0].legend(legend, prop={'size': 8})
        axis[0, 0].set_title("10.000 processes")

        # Waiting times 20.000 processen
        [axis[0, 1].plot(x, i) for i in waiting_times2]
        axis[0, 1].set_xlabel("Service time in percentiles")
        axis[0, 1].set_ylabel("Waiting time")
        axis[0, 1].set_ylim([0, 2000])
        axis[0, 1].legend(legend, prop={'size': 8})
        axis[0, 1].set_title("20.000 processes")

        # Response ratios 10.000 processen
        [axis[1, 0].plot(x, i) for i in response_ratios1]
        axis[1, 0].set_xlabel("Service time in percentiles")
        axis[1, 0].set_ylabel("Response ratio")
        axis[1, 0].set_ylim([0, 30])
        axis[1, 0].legend(legend, loc="upper right", prop={'size': 8})

        # Response ratios 20.000 processen
        [axis[1, 1].plot(x, i) for i in response_ratios2]
        axis[1, 1].set_xlabel("Service time in percentiles")
        axis[1, 1].set_ylabel("Response ratio")
        axis[1, 1].set_ylim([0, 30])
        axis[1, 1].legend(legend, loc="upper right", prop={'size': 8})

        figure.suptitle("CPU Scheduling exercise (full screen this window)")
        plt.show()

    else:
        # Waiting times 10.000 processen
        [plt.plot(x, i) for i in waiting_times1]
        plt.xlabel("Service time in percentiles")
        plt.ylabel("Waiting time")
        plt.ylim([0, 2000])
        plt.legend(legend)
        plt.title("10.000 processes waiting time")
        plt.show()

        # Waiting times 20.000 processen
        [plt.plot(x, i) for i in waiting_times2]
        plt.xlabel("Service time in percentiles")
        plt.ylabel("Waiting time")
        plt.ylim([0, 2000])
        plt.legend(legend)
        plt.title("20.000 processes waiting time")
        plt.show()

        # Response ratios 10.000 processen
        [plt.plot(x, i) for i in response_ratios1]
        plt.xlabel("Service time in percentiles")
        plt.ylabel("Response ratio")
        plt.ylim([0, 30])
        plt.legend(legend)
        plt.title("10.000 processes response ratio")
        plt.show()

        # Response ratios 20.000 processen
        [plt.plot(x, i) for i in response_ratios2]
        plt.xlabel("Service time in percentiles")
        plt.ylabel("Response ratio")
        plt.ylim([0, 30])
        plt.legend(legend)
        plt.title("20.000 processes response ratio")
        plt.show()


if __name__ == "__main__":
    main()
