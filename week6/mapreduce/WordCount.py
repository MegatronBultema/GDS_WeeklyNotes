
from mrjob.job import MRJob

class MyMR(MRJob):
    
    # key = _, value = line
    def mapper(self, _, line):
        words = line.split()
        
        for word in words:
            yield (word, 1)
    
    # key = word, value = count
    def reducer(self, word, count):
        yield (word, sum(count))
    
if __name__ == '__main__': 
    MyMR.run()