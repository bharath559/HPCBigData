import sys
from operator import add
from pyspark import SparkContext
from string import punctuation


if len(sys.argv) != 3:
    print >> sys.stderr, "Usage: wordcount <input_file> <output_file>"
    exit(-1)
sc = SparkContext(appName="PythonWordCount")
lines = sc.textFile(sys.argv[1])
counts = lines.flatMap(lambda line: line.strip(punctuation).lower().strip().strip(' ').split(' ')).map(lambda word: (word, 1)).reduceByKey(add)
output_counts = counts.filter(lambda x: len(x)>0)
output_counts.saveAsTextFile(sys.argv[2])
output_counts.cache()
print "Highest Frequency Word:%s",output_counts.count()
sc.stop()
