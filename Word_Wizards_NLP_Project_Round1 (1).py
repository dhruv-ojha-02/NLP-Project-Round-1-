#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk

from nltk.corpus import stopwords
import string
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
from nltk.tokenize import word_tokenize
import re
from tabulate import tabulate
import random


# In[2]:


nltk.download('stopwords')


# In[3]:


# In[39]:


import nltk

from nltk.corpus import stopwords
import string
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
from nltk.tokenize import word_tokenize
import re
from tabulate import tabulate
import random


# In[2]:


nltk.download('stopwords')


# In[4]:


import nltk

from nltk.corpus import stopwords
import string
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
from nltk.tokenize import word_tokenize
import re
from tabulate import tabulate
import random


# In[5]:


nltk.download('stopwords')


# In[6]:


nltk.download('punkt')


# In[7]:


nltk.download('averaged_perceptron_tagger')


# In[8]:


file = open("the-kite-runner.txt",encoding='utf-8')
wordslists = file.read().splitlines()
wordslists = [i for i in wordslists if i != ' ']
text = " "
text = text.join(wordslists)


# In[9]:


text[:2000]


# In[10]:


len(text)


# In[11]:


#removing unwanted links from the text
text = re.sub(r'http\S+', '',text, flags=re.MULTILINE)
#removing unwanted email-ids from the text
text=re.sub(r'[A-Za-z0-9]*@[A-Za-z]*\.?[A-Za-z0-9]*', "", text)
#remove unwanted spaces
res = re.sub(' +', ' ', text)
text = str(res)


# In[12]:


text[:2000]


# In[13]:


#removing all punctuationns from our text file
punctuations = '''!()-[]{};:'"\,<>./‘’?“”@#$%^&*_~'''
newtext = ""
for char in text:
    if char not in punctuations:
        newtext = newtext + char


# In[14]:


#Converting the text into lower case         
newtext = newtext.lower()


# In[15]:


newtext[:2000]


# In[16]:


# Tokenizing 
tokens = word_tokenize(newtext)
tokens[:50] #first 50 tokens


# In[17]:


type(tokens)


# In[18]:


len(tokens)


# In[19]:


# Removing stopwords and storing it into finaltext
stop_words = set(stopwords.words('english'))
# tokens = word_tokenize(cleantext)
tokens_final = [i for i in tokens if not i in stop_words] # tokenising with removing stopwords
text_new = "  "
text_new = text_new.join(tokens_final)


# In[20]:


text_new[:2000]


# In[21]:


#STEP 4 : Analyse the frequency distribution of tokens in T
#With stopwords
freq = nltk.FreqDist(tokens)
freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse=True)}
x = list(freq.keys())[:40]
y = list(freq.values())[:40]
plt.figure(figsize=(12,5))
plt.plot(x,y,c='b',lw=3,ls='-.')
plt.grid()
plt.xticks(rotation=90)
plt.title('Frequency Distribution of Tokens (with stopwords)',size=17)
plt.xlabel('Tokens',size=13)
plt.ylabel('Frequency',size=13)
plt.show()


# In[42]:


#STEP 4 : Analyse the frequency distribution of tokens in T
#Without stopwords
freq = nltk.FreqDist(text_new)
freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse=True)}
x = list(freq.keys())[:40]
y = list(freq.values())[:40]
plt.figure(figsize=(12,5))
plt.plot(x,y,c='b',lw=3,ls='-.')
plt.grid()
plt.xticks(rotation=90)
plt.title('Frequency Distribution of Tokens (without stopwords)',size=17)
plt.xlabel('Tokens',size=13)
plt.ylabel('Frequency',size=13)
plt.show()


# In[23]:


# Create a word cloud on the Tokens in T 
#With stopwords
cloud = WordCloud(width = 800, height = 500, 
                background_color ='black', 
                min_font_size = 10,stopwords = {},colormap='summer').generate(newtext) 

plt.figure(figsize = (12,8), facecolor = None) 
plt.imshow(cloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 


# In[24]:


# Create a word cloud on the Tokens in T 
#Without stopwords
cloud = WordCloud(width = 800, height = 500, 
                background_color ='black', 
                min_font_size = 10,stopwords = {},colormap='summer').generate(text_new) 

plt.figure(figsize = (12,8), facecolor = None) 
plt.imshow(cloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 


# In[25]:


# using Penn Treebank Tag Set
tagged_text = nltk.pos_tag(tokens)
tagged_text[:20]


# In[26]:


from collections import Counter
counts = Counter( tag for word,  tag in tagged_text)
print(counts)


# In[27]:


freq_tags = nltk.FreqDist(counts)
freq_tags = {k: v for k, v in sorted(freq_tags.items(), key=lambda item: item[1],reverse=True)}
x = list(freq_tags.keys())[:40]
y = list(freq_tags.values())[:40]
plt.figure(figsize=(12,5))
plt.plot(x,y,c='b',lw=3,ls='-.')
plt.grid()
plt.xticks(rotation=90)
plt.title('Frequency Distribution of TAGs',size=17)
plt.xlabel('Tags',size=13)
plt.ylabel('Frequency',size=13)
plt.show()


# In[28]:


# Get the largest chapter C from the book
# replace chapter with a intentional delimiter
formatted_text = newtext.replace('the kite runner by khaled hosseini','#jaskaran#chapter')
formatted_text[:2000]


# In[29]:


splitted_text = formatted_text.split("#jaskaran#")
biggest_chapter = ""
biggest_chapter_len = 0
for i in splitted_text:
    chapter = i.split("\n\n")
    if len(i) > biggest_chapter_len:
        biggest_chapter = str(i)
        biggest_chapter_len = len(i)
print(biggest_chapter_len)
print(biggest_chapter)


# In[30]:


chapter_words = biggest_chapter.split()
print(chapter_words)


# In[31]:


bigrams = [(w1, w2) for w1, w2 in zip(chapter_words,chapter_words[1:])]
print(bigrams)


# In[32]:


listOfBigrams = []
bigramCounts = {}
unigramCounts = {}
nbyn = {}

for i in range(len(chapter_words)):
    if i < len(chapter_words) - 1:

        listOfBigrams.append((chapter_words[i], chapter_words[i + 1]))

        if (chapter_words[i], chapter_words[i+1]) in bigramCounts:
            bigramCounts[(chapter_words[i], chapter_words[i + 1])] += 1
        else:
            bigramCounts[(chapter_words[i], chapter_words[i + 1])] = 1

    if chapter_words[i] in unigramCounts:
        unigramCounts[chapter_words[i]] += 1
    else:
        unigramCounts[chapter_words[i]] = 1 

listOfProb = {}

bigram_of_every_word = {}

for bigram in listOfBigrams:
    word1 = bigram[0]
    word2 = bigram[1]
    listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))
    if word1 in bigram_of_every_word:
        bigram_of_every_word[word1].append([word2,str((bigramCounts.get(bigram))/(unigramCounts.get(word1)))])
    else:
        bigram_of_every_word[word1] = [word2,str((bigramCounts.get(bigram))/(unigramCounts.get(word1)))]

bigram_prob_table = []

# print(bigram_of_every_word['and'])

for bigrams in listOfBigrams:
    temp_list = [(str(bigrams)),str(bigramCounts[bigrams]),str(listOfProb[bigrams])]
    bigram_prob_table.append(temp_list)
	# print(str(bigrams) + ' : ' + str(bigramCounts[bigrams]) + ' : ' + str(listOfProb[bigrams]) + '\n')
print (tabulate(bigram_prob_table, headers=["Bigram", "Count", "Probability"]))


# In[39]:


shannon_game_text = random.choice(splitted_text)


# In[40]:


shannon_game_words = shannon_game_text.split()
statement = shannon_game_words[169:177]
print(statement)


# In[41]:


prev_word = statement[-1]
print(prev_word)
predicted_next_word = prev_word
if prev_word not in bigram_of_every_word:
    
    print('Word not found')
else:
    next_words = bigram_of_every_word[prev_word]
    # print(type(next_words))
    # print(next_words)
    next_letters_sorted = sorted(next_words, key=lambda x: x[1],reverse=True)
    predicted_next_word = next_letters_sorted[0]
    print('The predicted next word is : ' + predicted_next_word)
    print('Actual word is : ' + shannon_game_words[177])

