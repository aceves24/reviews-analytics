data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取結束, 總共有', len(data), '筆資料' )


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	print(sum_len)
print("留言平均長度為: ", sum_len / len(data))

new_list = []
for d in data:
	if len(d) < 100:
		new_list.append(d)
print('總共有', len(new_list), '筆留言小於100個字')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

good = [d  for d in data if 'good' in d]
print(good)
bad = ['bad' in d for d in data]
print(bad)


# 文字計數

wc = {}             # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
	
print(len(wc))

print(wc['Allen'])

while True:
	word = input('請輸入想查找的字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過', wc[word], '次')
	else:
		print('這個字沒有出現過!')

print('感謝使用本查詢功能')