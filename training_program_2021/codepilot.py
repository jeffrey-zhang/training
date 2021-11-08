# define a function to read ini file
def read_ini(filename):
    # open the file
    with open(filename, 'r') as f:
        # read the file
        content = f.read()
    # split the file into lines
    lines = content.split('\n')
    # define a dictionary to store the data
    data = {}
    # loop over the lines
    for line in lines:
        # split the line into words
        words = line.split('=')
        # if there are two words
        if len(words) == 2:
            # add the data to the dictionary
            data[words[0]] = words[1]
    # return the dictionary
    return data

# define a compare function to