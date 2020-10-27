

words = {}
special_chars = {'!', '@', '$', '#'}
i = 0

with open("/home/jezil2210/words.txt", "r") as w:
     for word in w.readlines():
         for char in special_chars:
             while (i <= 99): 
                 if (i <= 9):
                    i = '0' + str(i)  
                 else:
                    i = str(i) 
                 print (word.strip() + str(i) + char)
                 i = int(i)
                 i+=1
             i=0
