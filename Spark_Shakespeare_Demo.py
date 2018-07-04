from pyspark import SparkConf, SparkContext
from operator import add
import re
from English_Stop_Words import english_stop_words


# create Spark context with Spark configuration
conf = SparkConf()
conf.setMaster('local')
conf.setAppName('THB - Spark Basics Exercise')
sc = SparkContext(conf=conf)

# read the cleaned shakespeare file to RDD
rdd_text = sc.textFile("./t8.shakespeare_cleaned.txt")

# clean the initial text loaded into rdd and count all contained words
words_counts = rdd_text \
    .flatMap(lambda line: line.split(' ')) \
    .map(lambda word: word.lower()) \
    .map(lambda word: re.sub(r'\'+[a-z]', '', word)) \
    .map(lambda word: re.sub(r'[\n\b\f\r\t\v,.!?:;\"[\]{}()&\-\'\x00]', ' ', word)) \
    .map(lambda word: word.replace('\"', '')) \
    .map(lambda word: word.strip()) \
    .map(lambda word: re.sub(r'\s+[a-z]+$', '', word)) \
    .map(lambda word: re.sub(r'[s]$', '', word)) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(add)

print("Number of words (raw): " + str(words_counts.count()))

# filter out stop words which are irrelevant at all
filtered_word_counts = words_counts.filter(lambda x: len(x[0]) > 3 and not x[0] in english_stop_words)
print("Number of words (stop words stripped now): " + str(filtered_word_counts.count()))

# determine the 24 most frequent words
most_frequent_words = filtered_word_counts.takeOrdered(24, key=lambda x: -x[1])

# write the 24 most frequent words inlcuding it's total occurrence number to file
with open('most_frequent_words.txt', 'w') as filehandle:
    for count_item in most_frequent_words:
        filehandle.write('%s\t\t-\tOccurrences: %d\n' % (count_item[0], count_item[1]))
