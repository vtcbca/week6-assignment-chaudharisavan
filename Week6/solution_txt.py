Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> with open ("E://sem-3//python.txt",'w') as f:
     l1="Python is a popular general-purpose programming language.\n"
     l2="It was created by Guido van Rossum, and released in 1991.\n"
     l3="It is used in machine learning, web development, desktop applications, and many other fields. \n"
     l4="Fortunately for beginners, Python has a simple, easy-to-use syntax. \n"
     l5="This makes Python a great language to learn for beginners.\n"
     l6="Why Learn Python?\n"
     l7="Python is easy to learn.\n"
     l8="Its syntax is easy and code is very readable.\n"
     l9="Python has a lot of applications.\n"
     l10="It's used for developing web applications, data science, rapid application development, and so on.\n"
     l11="Python allows you to write programs in fewer lines of code than most of the programming languages.\n"
     l12="The popularity of Python is growing rapidly.\n"
     l13="Now it's one of the most popular programming languages.\n"
     f.writelines([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13])
  
# 1.read it python.txt and print it reverse order
     with open ("E://sem-3//python.txt","r") as f:
          data=f.readlines()
     print(data)
     for i in reversed(data):
          print(i.strip())
#2. Read Python.txt file and Print total number of lines and words in it.
with open("E://sem-3//python.txt","r",newline='')  as f:
     data=f.readlines()
     totallines=len(data)
     print("total no of lines:{}".format(totallines))
     content=f.readlines()
     line=content.split()
     totalword=(len(line))
     print("total no of word:{}".format(totalword))
#3.Read Python.txt file and Print unique word with its count.
with open("E://sem-3//python.txt","r") as f:
     contents=f.read()
     word=contents.split()
     words_count=[]
     for  i in word:
          if i in words_count:
               words_count[i]=words_count[i]++1
          else:
               words_count=1
     count=0
     for i in words_count:
          if words_count[i]==1:
               count=count+1
     print("unique words:",words_count)
     print("count of wunique words:{}".format(count))
#4.  Program 4: Read Python.txt file and Print largest and smallest word from it.
with open("E://sem-3//python.txt","r",newline='') as f:
     data=f.read0()
     words=data.split()
     if words:
         smallest_word = min(words, key=len)
         largest_word = max(words, key=len)
         print(f"Smallest word: {smallest_word}")
         print(f"Largest word: {largest_word}")
     else:
         print("The file is empty.")
#5 Read Python.txt file. Convert it into upper case and write into another file uppper.txt
with open ("E://sem-3//python.txt","r",newline='') as f:
     d=f.readlines()
     upper_file=d.upper()
with open ("E://sem-3//upper.txt","w") as f1:
     f1.write(upper_file)
     
     