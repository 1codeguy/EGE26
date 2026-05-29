with open(r'/Users/admin/Desktop/N26/26_24897.txt') as file:
    N = int(file.readline())
    requests = [list(map(int, i.split())) for i in file]

requests = sorted(requests, key=lambda x: (x[1], x[2], x[0]))
house_num = 0
padic_num = 0
max_padics = 0
min_request = 10 ** 10

cnt_padics = 1
num_start_padic = requests[0][2]
min_num_req_start_padic = requests[0][1]

for req_1, req_2 in zip(requests, requests[1:]):
    if req_1[1] != req_2[1] or req_1[2] + 1 != req_2[2]:
        cnt_padics = 1
        num_start_padic = req_2[2]
        min_num_req_start_padic = req_2[0]
        continue
    if req_1[2] == req_2[2]:
        if req_2[2] == num_start_padic:
            min_num_req_start_padic = min(min_num_req_start_padic, req_2[0])
        continue
    if req_1[2] + 1 == req_2[2]:
        cnt_padics += 1

    if cnt_padics > max_padics or \
            cnt_padics == max_padics and min_request > min_num_req_start_padic:
        house_num = req_1[1]
        padic_num = num_start_padic
        min_request = min_num_req_start_padic
        max_padics = cnt_padics

print(house_num, padic_num)