from main import clustering

with open('result.txt','w+') as fileout:
    print 'running lda'
    text = clustering('lda',3,10)
    fileout.write('LDA K=3\n')
    fileout.write(text+'\n\n')
    text = clustering('lda',4,10)
    fileout.write('LDA K=4\n')
    fileout.write(text+'\n\n')
    text = clustering('lda',5,10)
    fileout.write('LDA K=5\n')
    fileout.write(text+'\n\n')
    text = clustering('btm',3,10)
    print 'running btm'
    fileout.write('BTM K=3\n')
    fileout.write(text+'\n\n')
    text = clustering('btm',4,10)
    fileout.write('BTM K=4\n')
    fileout.write(text+'\n\n')
    text = clustering('btm',5,10)
    fileout.write('BTM K=5\n')
    fileout.write(text+'\n\n')
    fileout.flush()