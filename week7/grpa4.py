station_dict = {}
n = int(input())
for i in range(n):
    train_name = input()
    m = int(input())
    c_dict = {}
    for j in range(m):
        compartment_details = input()
        c_dict[compartment_details.split(',')[0]] = int(compartment_details.split(',')[1])
    station_dict[train_name] = c_dict
print(station_dict)