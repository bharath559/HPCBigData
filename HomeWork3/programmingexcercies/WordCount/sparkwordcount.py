import sys
from operator import add
from pyspark import SparkContext
from string import punctuation


if len(sys.argv) != 3:
    print >> sys.stderr, "Usage: wordcount <input_file> <output_file>"
    exit(-1)
sc = SparkContext(appName="PythonWordCount")
lines = sc.textFile(sys.argv[1])
counts = lines.flatMap(lambda line: line.strip(punctuation).lower().strip().strip('').split(' ')).map(lambda word: (word, 1)).reduceByKey(add)
counts_nonempty = counts.filter(lambda(k,v):len(k)>0)
counts_nonempty.saveAsTextFile(sys.argv[2])
counts_max = counts_nonempty.map(lambda(k,v):(v,k))
highest_count = counts_max.max()
print "Highest Frequency Word:%s",highest_count
sc.stop()
