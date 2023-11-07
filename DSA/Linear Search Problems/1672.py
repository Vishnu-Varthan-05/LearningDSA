# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
# accounts = [[1,2,3],[3,2,1]]
# max = sum(accounts[0])
# for amounts in accounts:
#     if sum(amounts) > max:
#         max = sum(amounts)

# print(max)

# or 
accounts = [[1,2,3],[3,2,1]]
max = 0 
for banks in accounts:
    total = 0
    for amounts in banks:
        total += amounts
    if total > max:
        max = total
print(max)