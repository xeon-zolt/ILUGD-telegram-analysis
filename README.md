# ILUGD-telegram-analysis

# How to make Backup of telegram group chat
use [LINK](https://github.com/tvdstaaij/telegram-history-dump#usage) to dump it I have include the latest chat of ILUGD telegram group in the repo
after that you will get a jsonl file in the dump of your group chat to convert it into csv i have used [link](https://github.com/xeon-zolt/ILUGD-telegram-analysis/blob/master/jsonl2csv.py)
like 
```
python2 jsonl2csv.py json/ILUG-D.jsonl ILUG-D.csv
```
after getting csv file i have used varios operations for analysis of chat data
for eg 
## pie chart
![](https://github.com/xeon-zolt/ILUGD-telegram-analysis/blob/master/PieOfNumberOfMessages.png?raw=true)

you can help in creating functions to do more analysis on this data 
