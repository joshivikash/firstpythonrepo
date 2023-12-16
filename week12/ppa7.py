nums = [int(x) for x in input().split(',')]
nos_of_rotations = int(input())
rotated_list = nums[0:len(nums)]
for i in range(nos_of_rotations):
    rotated_list = [rotated_list[-1]] + rotated_list[0:len(rotated_list)-1]
for x in rotated_list:
    if rotated_list.index(x) < (len(rotated_list)-1):
        print(x,end=',')
    else:
        print(x)