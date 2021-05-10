# hackerrank_python
if __name__ == '__main__':
    
    n = int(input())
# list to store the data element
lst = []

# loop through n times
for i in range(n):
   
    # splited input strings 
    s = input().split()

    # command extraction from splited strings
    command = s[0]

    # extraction of arguments 
    args = s[1:]

    # condition
    if command !="print":
        # here we adding strings of commands
        command += "("+ ",".join(args) +")"
        eval("lst."+command)
    else:
        print(lst)
