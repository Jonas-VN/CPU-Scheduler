from src.functions import parse_data, visualize_data

if __name__ == '__main__':
    data = parse_data("processen10000.xml")
    #index = 0
    total_p_no = len(data)  #aantal processen
    total_time = 0  #totale tijd te doen
    total_time_counted = 0  #totale tijd van proces dat al gescheduled is
    # proc is process list
    proc = []
    wait_time = 0
    turnaround_time = 0
    response_ratio = 0
    pid = 0
    for index in range(total_p_no):
        # Getting the input for process
        service_time = data[index][2]
        arrival = data[index][1]
        remaining_time = service_time
        pid = data[index][0]
        # processes are appended to the proc list in following format
        proc.append([arrival, service_time, remaining_time, 0, pid, wait_time, turnaround_time, response_ratio])
        # total_time gets incremented with burst time of each process
        total_time += service_time


    print("Enter time quantum")
    time_quantum = int(input())
    scheduled = []
    total_time_counted = proc[0][0] # no need to start at 0, start at the first arrival time
    q_finished_procs = 0
    # Keep traversing in round robin manner until the total_time == 0
    while total_time != 0:
        # traverse all the processes
        for i in range(len(proc)):
            arrivalTime = proc[i][0]
            remainingTime = proc[i][2]
            # if pid is already finished, go to next pid
            if proc[i][3] == 1:
                continue

            if arrivalTime > total_time_counted:
                # total_time_counted = arrivalTime #only valid if all previous processes are finished
                # total_time_counted += 1
                if q_finished_procs > 0 and q_finished_procs == i:
                    total_time_counted = arrivalTime  # only valid if all previous processes are finished
                break

            # proc[i][2] here refers to remaining_time for each process i.e "i"
            if time_quantum >= remainingTime >= 0:
                total_time_counted += remainingTime
                total_time -= remainingTime
                # the process has completely ended here thus setting it's remaining time to 0.
                proc[i][2] = 0

            elif proc[i][2] > 0:
                # if process has not finished, decrementing it's remaining time by time_quantum
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum

            # if remaining time of process is 0 and
            # individual waiting time of process has not been calculated i.e flag
            if proc[i][2] == 0 and proc[i][3] != 1:
                q_finished_procs += 1
                wait_time += total_time_counted - proc[i][1] - proc[i][0]
                turnaround_time += total_time_counted- proc[i][0]
                response_ratio = turnaround_time / proc[i][1]
                # flag is set to 1 once wait time is calculated
                proc[i][3] = 1
                wait_time_pid = total_time_counted - proc[i][1] - proc[i][0]
                turnaround_time_pid = total_time_counted - proc[i][0]
                response_ratio_pid = turnaround_time_pid / proc[i][1]
                print(f"PID: {proc[i][4]}\t Arrival time: {proc[i][0]}\t Service time: {proc[i][1]}\t Waiting time: {wait_time_pid}\t Turnaround time: {turnaround_time_pid}\t Response ratio: {round(response_ratio_pid, 2)}")
                scheduled.append([proc[i][4], proc[i][0], proc[i][1], wait_time_pid, turnaround_time_pid, response_ratio_pid])



    print("\nAvg Waiting Time is ", (wait_time * 1) / total_p_no)
    print("Avg Turnaround Time is ", (turnaround_time * 1) / total_p_no)

    visualize_data(scheduled)
