from csv import writer
from misc import lists

# Params
tickername = input("Ticker i.e 'SPY': ")
timeframe = input("Time Interval i.e '30/minute': ")
timeinterval = input("Timeframe i.e '2000-01-21/2021-11-26': ") # max 5000 iterations

#funktion from lists.py
lists.list_stocks(tickername, timeframe, timeinterval)

# names for created csv
csvname = tickername + '_' + timeframe.replace('/','') + '_' + timeinterval.replace('/','_') + '.csv'

list_data = ['Date','Open','High','Low','Close','Volume']

# Create csv coloumns
with open('tickers\\' + csvname, 'w', newline='') as f_object:
    # Pass the CSV  file object to the writer() function
    writer_object = writer(f_object)
    writer_object.writerow(list_data)

    for x in range(len(lists.date)):
        f_object.write(lists.date[x])
        f_object.write(',')
        f_object.write(str(lists.open[x]))
        f_object.write(',')
        f_object.write(str(lists.high[x]))
        f_object.write(',')
        f_object.write(str(lists.low[x]))
        f_object.write(',')
        f_object.write(str(lists.close[x]))
        f_object.write(',')
        f_object.write(str(lists.volume[x]))
        f_object.write("\n")

lines_seen = set() # holds lines already seen

with open('tickers\\' + csvname, "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:()
    if i not in lines_seen:
        f.write(i)
        lines_seen.add(i)
        f.truncate()

with open('tickers\\' + csvname, "r") as txt_file:
  new_data = list(set(txt_file))

f_object.close()