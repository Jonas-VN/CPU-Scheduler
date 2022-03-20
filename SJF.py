n = int(input("enter number of processes"))
process_list = []
print("put process_id and burst_time respectively")
for _ in range(n):
    process_list.append(list(map(int,input().split())))
    #lijst sorteren op burst time
for i in range (n):
    for j in range (i+1,n):
        if process_list[i][1]>process_list[j][1]:
            process_list[i], process_list[j] = process_list[j], process_list[i]
ct = 0 #completion time
for i in range(n):
    ct+=process_list[i][1]
    process_list[i].append(ct)
print("pid BT CT/TAT WT")
tat,wt=0,0
for i in range(n):
    print(process_list[i][0],"",process_list[i][1],"", process_list[i][2]-process_list[i][1])
    tat+=process_list[i][2]
    wt+=process_list[i][2]-process_list[i][1]
avg_total_burst_time=tat/n
avg_waiting_time=wt/n
