#%%
from mrjob.job import MRJob
# %%
# Create a class called Bacon_count, which inherits, or takes properties, 
# from the MRJob class. We create this class to be called to run the full 
# MapReduce job with MRJob
class Bacon_count(MRJob):
    # create a mapper() function to take (self, _, line) as params
    # mapper() function will assign the input to key-value pairs:
    def mapper(self, _, line):
        # use the Python convention of an underscore to indicate that 
        # won’t use this param. The line param will be the line of text taken from the raw input file
        # The function will loop through each word in the line of text, as described below
        # Call the split() method on each line to break the text into a list of words
        for word in line.split():
            if word.lower() == "bacon":  # convert each work to lowercase
                # if word matches "bacon" return generator object:
                yield "bacon", 1
        # convert each work to lowercase
    
    # call reducer function
    def reducer(self, key, values):
        yield key, sum(values)

# call funtion
if __name__ == "__main__":
   Bacon_count.run()

