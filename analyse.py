import pandas as pd # required for csv file 
import matplotlib.pyplot as plt #for plotting
from wordcloud import WordCloud

#importing data
df = pd.read_csv('ILUG-D.csv')

#pie charrt
all = df['from'].value_counts() 
all.head(21).plot(kind='pie',y ='',autopct='%1.1f%%',fontsize=12) #setting the pie chart
plt.axis('equal')
#plt.title('Number of meassages',bbox={'facecolor':'0.8', 'pad':3})
fig = plt.gcf() 
fig.set_size_inches(10,10) #setting the size of figure
plt.savefig('PieOfNumberOfMessages.png') #saving the plot

#bar graph
all = df['from'].value_counts()
all.head(21).plot(kind='barh')
plt.title('Number of messages in ILUG-D group|')
plt.xlabel('Number of messages')
fig = plt.gcf()
fig.set_size_inches(10,10)
plt.savefig('BarhOfNumberOfMessages.png') #saving the plot


list = df.text.values.tolist()
list2 = []
for i in list:
    list2.extend(i.split(' '))
list2

#wordcloud
str1 = ''.join(list2)
wordcloud = WordCloud(max_words=1000).generate(str1)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
fig = plt.gcf()
fig.set_size_inches(10,10)
plt.savefig('WordcloudOfMessages.png') #saving the plot

#counting editors
vim_count = 0
nano_count = 0
micro_count = 0
atom_count = 0
sublime_count = 0
gedit_count = 0

for i in list2:
    if 'vim' in i:
        vim_count = vim_count + 1
    elif 'nano' in i:
        nano_count = nano_count + 1
    elif 'micro' in i:
        micro_count = micro_count + 1
    elif 'atom' in i:
        atom_count = atom_count + 1
    elif 'sublime' in i:
        sublime_count = sublime_count + 1
    elif 'gedit' in i:
        gedit_count = gedit_count + 1
print('\nno of editors')#try plotting them
print('vim ' + str(vim_count))
print('nano ' + str(nano_count))
print('micro ' + str(micro_count))
print('atom ' + str(atom_count))
print('sublime ' + str(sublime_count))
print('gedit ' + str(gedit_count))

#counting distros
ubuntu_count = 0
arch_count = 0
debian_count = 0
gentoo_count = 0
mint_count = 0
for i in list2:
    if 'ubuntu' in i:
        ubuntu_count = ubuntu_count + 1
    elif 'arch' in i:
        arch_count = arch_count + 1
    elif 'debian' in i:
        debian_count = debian_count + 1
    elif 'gentoo' in i:
        gentoo_count = gentoo_count + 1
    elif 'mint' in i:
        mint_count = mint_count + 1
print('\nno of distro')#try plotting them 
print('ubuntu ' + str(ubuntu_count))
print('arch ' + str(arch_count))
print('debian ' + str(debian_count))
print('gentoo ' + str(gentoo_count))
print('mint ' + str(gentoo_count))

