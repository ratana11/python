#20180419 thu
#https://stepik.org/lesson/23217/step/6?unit=6784
# 1.Where in the Genome Does DNA Replication Begin? (Part1)



# 1.3 Hidden Messages in the Replication Origin (Part2)
def FrequencyMap(Text, k):
    # your code here
    freq = {}
    n=len(Text)
    for i in range (n-k+1):
        Pattern = Text [i:i+k]
        if Pattern not in freq:
            freq [Pattern] = 1
# if a pattern found is not already  in the dictionary freq{}, it is assigned a value of 1 and added to the list
        else:
            freq [Pattern] +=1
# however, if the pattern is already in the dictionary, its value should go up by 1 (so if it has been found, it is initially given a pattern of 1, and then this adds another 1 if it is found again
    return freq
	    

print (FrequencyMap ("CGATATATCCATAG", 3))

def FrequencyMap1(Text, k):
    freq = {}
    n = len(Text)
    for i in range (n-k+1):
        Pattern = Text [i:i+k]
        if Pattern not in freq:
            freq [Pattern] = 1
        else:
            freq [Pattern] += 1
    return freq
print (FrequencyMap1 ("CGATATATCCATAGATCGTAG", 3))
