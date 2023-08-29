from pyspark import SparkContext

log_file = "log.txt"
sc = SparkContext('local', 'test app')
log_data = sc.textFile(log_file).cache()
numAs = log_data.filter(lambda s: 'a' in s).count() 
numBs = log_data.filter(lambda s: 'b' in s).count()

print(f"Lines with a: {numAs}, lines with b: {numBs}")