

#HOW TO RUN:
**this script is tested on linux ONLY**
 
1. re-make OnlineBTM/src
2. run preprocess.py
3. put the generated corpus file into data/ and rename it as 0.txt
4. run 
     >python main.py model K n 

      model='lda' or 'btm'.

      **if you are not using linux, you may have to modify topicmodel.py line 23 based on your system**
5. or run test.py to execute pre-defined procedure