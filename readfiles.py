text_file = "test.txt"
def read_file(text_file):
    '''
    Function that reads a text file and returns the data from the text file
    '''
    with open(text_file,"r") as handle:
        data = handle.read()
        return data
