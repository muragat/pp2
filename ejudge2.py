#ejudge2.1
'''
year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("YES")
else:
    print("NO")
    '''

#ejudge2.2
'''
um=int(input())
print(sum*(sum+1)//2)
'''

#ejudge2.3
'''
n=int(input())
total=0
sums=input().split()
for i in range(n):
    total+=int(sums[i])
print(total)
'''

#ejudge2.4
'''
a=int(input())
sum=input().split()
count=0

for i in range(a):
 if int(sum[i])>=1:
    count+=1
print(count)
'''

#ejudge2.5
'''
n=int(input())
if n<1:
    print('NO')
else:
    x=1
    while x<n:
        x*=2
    if x==n:
        print('YES')
    else:
        print('NO')
'''

#ejudge2.6
'''
n=int(input())
sums=input().split()
 
print(max(int(sums[i]) for i in range(n)))
'''

#ejudge2.7
'''
n = int(input())             # 输入数字个数
nums = input().split()       # 输入一行数字，得到字符串列表

max_value = int(nums[0])     # 假设第一个数是最大
position = 1                 # 最大值的位置（从 1 开始）

for i in range(1, n):        # 从第二个数开始遍历
    if int(nums[i]) > max_value:
        max_value = int(nums[i])
        position = i + 1     # i 从 0 开始，所以位置要加 1

print(position)
'''

#ejudge2.8
'''
n = int(input())

x = 1
while x <= n:
    print(x, end=' ')  # 打印在同一行，用空格分隔
    x *= 2
'''

#ejudge2.9
'''
n = int(input())
nums = input().split()

# 先把所有元素转成整数
for i in range(n):
    nums[i] = int(nums[i])

# 找最小值和最大值
max_value = nums[0]
min_value = nums[0]
for i in range(1, n):
    if nums[i] > max_value:
        max_value = nums[i]
    if nums[i] < min_value:
        min_value = nums[i]

# 把最大值改成最小值
for i in range(n):
    if nums[i] == max_value:
        nums[i] = min_value

# 输出修改后的数组
for i in range(n):
    print(nums[i], end=' ')
'''

#ejudge2.10
'''
# 读入
n = int(input())
nums = input().split()

# 转换成整数
for i in range(n):
    nums[i] = int(nums[i])

# 排序（升序）
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # 交换

# 反转数组
for i in range(n // 2):
    nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]

# 输出结果
for i in range(n):
    print(nums[i], end=' ')
'''

#ejudge2.11
'''
# 输入
n, l, r = map(int, input().split())
nums = input().split()

# 转整数
for i in range(n):
    nums[i] = int(nums[i])

# 调整索引
l_index = l - 1
r_index = r - 1

# 区间反转
while l_index < r_index:
    nums[l_index], nums[r_index] = nums[r_index], nums[l_index]
    l_index += 1
    r_index -= 1

# 输出结果
for i in range(n):
    print(nums[i], end=' ')
'''

#ejudge2.12
'''
# 输入
n = int(input())
nums = input().split()

# 转整数
for i in range(n):
    nums[i] = int(nums[i])

# 平方每个元素
for i in range(n):
    nums[i] = nums[i] ** 2

# 输出结果
for i in range(n):
    print(nums[i], end=' ')
'''

#ejudge2.13
'''n = int(input())

if n <= 1:
    print("No")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Yes")
    else:
        print("No")
'''

#ejudge2.14
'''n = int(input())
nums = list(map(int, input().split()))

# 统计每个数字出现次数
freq = {}
for x in nums:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

# 找出现次数最多的数字
max_count = 0
most_frequent = None

for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        most_frequent = key
    elif freq[key] == max_count:
        if key < most_frequent:
            most_frequent = key

print(most_frequent)
'''

#ejudge2.15
'''# 读入学生数量
n = int(input())

# 用集合存储唯一姓氏
unique_surnames = set()

# 读入每个姓氏并加入集合（自动去重）
for _ in range(n):
    surname = input().strip()  # 去掉首尾空格
    unique_surnames.add(surname)

# 输出不同姓氏数量
print(len(unique_surnames))
'''

#ejudge2.16
'''n = int(input())
nums = list(map(int, input().split()))

seen = set()  # 用集合存放已经出现过的数字

for x in nums:
    if x in seen:
        print("NO")
    else:
        print("YES")
        seen.add(x)
'''

#ejudge2.17
'''n = int(input())

# 用字典统计每个电话号码出现的次数
freq = {}

for _ in range(n):
    number = input().strip()
    if number in freq:
        freq[number] += 1
    else:
        freq[number] = 1

# 统计出现次数正好为 3 的电话号码个数
count = 0
for number in freq:
    if freq[number] == 3:
        count += 1

print(count)
'''

#ejudge2.18
'''n = int(input())

strings = []
first_occurrence = {}  # 用字典记录每个字符串第一次出现的位置

# 读入字符串并记录第一次出现位置
for i in range(n):
    s = input().strip()
    strings.append(s)
    if s not in first_occurrence:
        first_occurrence[s] = i + 1  # 下标从 1 开始

# 对字符串去重并排序
unique_sorted_strings = sorted(first_occurrence.keys())

# 输出每个字符串及其第一次出现的位置
for s in unique_sorted_strings:
    print(s, first_occurrence[s])
'''

#ejudge2.19
'''n = int(input())

episodes = {}  # 用字典记录每部剧总集数

for _ in range(n):
    line = input().split()
    name = line[0]
    k = int(line[1])
    
    if name in episodes:
        episodes[name] += k
    else:
        episodes[name] = k

# 按字典序排序输出
for name in sorted(episodes.keys()):
    print(name, episodes[name])
'''

#ejudge2.20
'''
n = int(input())  # 命令数量

document = {}  # 空文档

for _ in range(n):
    command = input().split()
    if command[0] == "set":
        key = command[1]
        value = command[2]
        document[key] = value  # 插入或更新
    elif command[0] == "get":
        key = command[1]
        if key in document:
            print(document[key])
        else:
            print(f"KE: no key {key} found in the document")
'''