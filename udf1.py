@outputSchema("getfirstname:chararray")
def fname(name):
# The received input is of type chararray. On accessing each element of the
# array, the ASCII equivalent value is returned. so, using the function
# 'chr' the character is derived and the name is derived till space is encountered.
# Once space is encountered, we exit the loop
        for pos, nam in enumerate(name):
            if pos == 0:
                fname = chr(name[0])
            elif name[pos] == 32:
                break
            else:
                fname = fname + chr(name[pos])
        return(fname)
