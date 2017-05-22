
from mrjob.job import MRJob

class MyMR(MRJob):
    
    def mapper(self, _, line):
        if line.startswith('#'):
            return
        fields = line.split()
        key = fields[2]
        if key in ['Kirk', 'Spock', 'McCoy']:
            number_str = fields[1]
            if number_str == 'ace':
                value = 11
            elif number_str in ['king','queen','jack']:
                value = 10
            else:
                value = int(number_str)
            yield (key, value)
        else:
            return
    
    # just a reminder, don't get hung up on names for key, value pairs
    def reducer(self, apple_juice, summer_day): 
        yield (apple_juice, sum(summer_day))
    
if __name__ == '__main__': 
    MyMR.run()