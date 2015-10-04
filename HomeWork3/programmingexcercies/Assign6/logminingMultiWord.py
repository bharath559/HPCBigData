from pyspark import SparkContext
import sys
if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: logmining <file>"
        exit(-1)
sc = SparkContext(appName="logmining")
text_file = sc.textFile(sys.argv[1])
errors = text_file.filter(lambda line: "error" in line)
errors.cache()
count = errors.count()
browser_error = errors.filter(lambda line: "Mozilla" in line)
browser_error.cache()
compatible_error = browser_error.filter(lambda line: "compatible" in line)
compatible_error.cache()
iphone_error = compatible_error.filter(lambda line: "iPhone" in line)
iphone_error.cache()
final_count = iphone_error.count()
print "Mozilla Compatible iPhone error count :%d",final_count
iphone_error.saveAsTextFile("/user/output/multicount")
