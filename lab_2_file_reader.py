file = open('numbers.txt', 'w')
file.write('''1
2
3
4
5
''')
file = open('numbers.txt', 'r')
list_nums = file.read().split('\n')
print(sum(int(x) for x  in list_nums if x != ''))