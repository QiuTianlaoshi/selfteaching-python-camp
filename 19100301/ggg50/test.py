import requests
import getpass
import yagmail
from pyquery import PyQuery
from mymodule import stats_word_day10
import matplotlib.pyplot as plt

plt.rcdefaults()
fig, ax = plt.subplots()

response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
r_content = document('#js_content').text()

# input text and define output word numbers
send_content = stats_word_day10.stats_text_cn(r_content, 10)

words = [x for (x, y) in send_content]
count = [y for (x, y) in send_content]

ax.barh(words, count, align = "center", color = "blue")
ax.set_yticks(words)
ax.set_yticklabels(words)
ax.invert_yaxis()
ax.set_xlabel('count')
ax.set_title('Top 10 words sorted by frequency')
plt.show()

