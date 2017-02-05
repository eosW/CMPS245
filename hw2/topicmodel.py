import csv,subprocess
from gensim import corpora
from gensim.models import LdaModel


def run_lda(filename,K,n):
    with open(filename) as filein:
        reader = csv.reader(filein,delimiter=' ')
        documents = [row for row in reader]
        dictionary = corpora.Dictionary(documents)
        corpus = [dictionary.doc2bow(text) for text in documents]
        lda = LdaModel(corpus, num_topics=K, id2word=dictionary)
        return ['topic '+str(k)+': '+lda.print_topic(k,n) for k in range(K)]

def run_btm(filedict,K,n):
    subprocess.call(['python','OnlineBTM/script/indexDocs.py',filedict,'bow/','dict.txt'])
    with open('dict.txt') as filein:
        voca = {}
        for l in filein.readlines():
            wid, w = l.strip().split('\t')[:2]
            voca[int(wid)] = w
    W = len(voca)
    subprocess.call(['OnlineBTM/src/run', 'ibtm', str(K), str(W), str(50./K), '0.05', 'bow/', '1', 'model/', '2000000','100'])
    zw_pt = 'model/' + 'k%d.day0.pw_z' % K
    k = 0
    topics = []
    with open(zw_pt) as filein:
        for l in filein:
            vs = [float(v) for v in l.split()]
            wvs = zip(range(len(vs)), vs)
            wvs = sorted(wvs, key=lambda d:d[1], reverse=True)
            #tmps = ' '.join(['%s' % voca[w] for w,v in wvs[:10]])
            tmps = ' '.join(['%f*"%s"' % (v,voca[w]) for w,v in wvs[:n]])
            topics.append((k, tmps))
            k += 1

    return ['topic %d: %s' % (k, s) for k, s in topics]