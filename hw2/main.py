import sys

import topicmodel

def clustering(model,K,n):
    if model=='lda':
        func = topicmodel.run_lda
        loc = 'data/0.txt'
    elif model == 'btm':
        func = topicmodel.run_btm
        loc = 'data/'
    res = func(loc,K,n)
    return '\n'.join(res)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'Usage: python %s <model> <K> <n>' % sys.argv[0]
    model = sys.argv[1]
    K = int(sys.argv[2])
    n = int(sys.argv[3])
    print clustering(model,K,n)