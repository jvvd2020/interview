import re

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

# 将长文本转化为列表
lines = long_text.strip().split('\n')
# 标题
name = lines[0].strip()
lei = lines[1].strip()

# 使用正则表达式对sub_fund进行处理
sub_fund = []
i = 2
while i < len(lines):
    title = lines[i].strip()
    i += 1
    isin = []
    while i < len(lines) and not re.match("^\d.",lines[i]) :
        isin.append(lines[i].strip())
        i += 1
    sub_fund.append({'title': title, 'isin': isin})

# 最终的字典
result = {'name': name, 'lei': lei, 'sub_fund': sub_fund}

print(result)
