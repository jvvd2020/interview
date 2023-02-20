from bs4 import BeautifulSoup
import csv

#反爬虫无法使用request读取，因此使用curl读成文件
response = open('response.txt','r')
html = response.read()
response.close()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find("table")

# 遍历<tr>
rows = []
for tr in table.find_all('tr')[1:]:
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    rows.append(row)

# 保存CSV文件
csvfile=open('data.csv', 'w', newline='')
writer = csv.writer(csvfile)
writer.writerows(rows)
print("数据保存成功！")