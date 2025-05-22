# account_list = {'2024312157': {'name': 'xzq', 'phone_number': '17613945236',
#                                'card': {'00000': {'password': '123456', 'money': 200.0}}}}
#
# for k, v in account_list.items():
#     print(v['card'])
#
# for k, v in account_list.items():
#     if '00000' in v['card'].keys():
#         print(v['card']['00000']['money'])
from itertools import count

# class Test:
#     count = 21
#
#     def print_num(self):
#         count = 20
#         self.count += 20
#         print(count)
#
#
# test = Test()
# test.print_num()
# print(Test.count)
# print(test.count)


file = open('abc.txt', 'r')
data = file.readline()
data_list = list(data)
print(data_list)
