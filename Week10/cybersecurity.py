# cybersecurity.py
# This program reads from a log file available from course material at the below repo
# https://github.com/andrewbeattycourseware/pands-course-material/blob/main/code/topic10-Extra%20pandas/data/access.log.demo

# Author Ellen McGrory
import pandas as pd
import re
import matplotlib.pyplot as plt

path = './data/'
log_filename = 'access.log.demo'

col_names= ('ip', 'dash1', 'userId', 'time', 'url', 'status code', 'size of response', 'referer', 'user agent', 'dunno')

df = pd.read_csv(log_filename, sep=' ', header=None, names=col_names)

# Dropping columns that contains dashes
df.drop(columns=['dash1','userId'],inplace=True)

# Lambda function to remove [] from the 'time' variable 
df['time'] =df['time'].apply(lambda x: re.search('[\w:/]+',x).group())

print(df.dtypes)

# 'time' column is an object so can be converted to datetime and is now a datetime64
# data type 
df['time'] = pd.to_datetime(df['time'],format='%d/%b/%Y:%H:%M:%S')
print(df.dtypes)

# Given 'time' is now datetime, the number of events that occured between two times
# such as an hour interval every day
df = df.set_index(['time'])
print(df.head())
new_df = df.between_time('23:00', '23:59')

# As the 'time' column is in the index, this can be resampled and can be plotted
# such as with mean of samples every 30 mins
download_samples_30min = df['size of response'].resample(rule='30min').mean()

download_samples_30min.plot()
plt.title('Mean Size of Responses',fontsize=20)
plt.xlabel('Date',fontsize=15)
plt.ylabel('Mean Size of Responses',fontsize=15)
plt.show()