# update 20.07.2020:
# make probabilities sum up to 1

import numpy


infile_n_best_stags_arcs = 'exa.tsv'

infile_gold_pos = 'exa-gold-pos.txt'


out_file = 'filtered_stags_output_only_gold_pos_test_exa.tsv'
outf = open(out_file, 'w')

def readFile(path):
    sentences = []
    sentence = []
    for line in open(path):
        line = line.strip()
        if not line:
            if len(sentence) > 0:
                sentences.append(sentence)
                sentence = []
        else:
            word = [x.strip() for x in line.strip().split("\t")]
            sentence.append(word)
    if len(sentence) > 0:
        sentences.append(sentence)
    print("number of sents: ", len(sentences))
    return sentences

sents = readFile(infile_n_best_stags_arcs)
pos = []

def count_sum_of_probabilities(lst_of_stags):
    return float(sum(float(x.split(':')[1]) for x in lst_of_stags))

import numpy as np

from scipy import signal, ndimage

def smooth1d(array, window_size=None, kernel='gaussian'):
    #https://www.programcreek.com/python/example/100550/scipy.signal.gaussian
    """Apply a centered window smoothing to a 1D array.

    Parameters
    ----------
    array : ndarray
        the array to apply the smoothing to
    window_size : int
        the size of the smoothing window
    kernel : str
        the type of smoothing (`gaussian`, `mean`)

    Returns
    -------
    the smoothed array (same dim as input)
    """

    # some defaults
    if window_size is None:
        if len(array) >= 9:
            window_size = 9
        elif len(array) >= 7:
            window_size = 7
        elif len(array) >= 5:
            window_size = 5
        elif len(array) >= 3:
            window_size = 3

    if window_size % 2 == 0:
        raise ValueError('Window should be an odd number.')

    if isinstance(kernel, str):
        if kernel == 'gaussian':
            kernel = signal.gaussian(window_size, 1)
        elif kernel == 'mean':
            kernel = np.ones(window_size)
        else:
            raise NotImplementedError('Kernel: ' + kernel)
    kernel = kernel / np.asarray(kernel).sum()
    return ndimage.filters.convolve1d(array, kernel, mode='mirror')


def rescale_stag_probs(lst_of_stags):
    lst_of_st = [x.split(':')[0] for x in lst_of_stags]
    lst_of_probs = [float(x.split(':')[1]) for x in lst_of_stags]
    print('72: ', lst_of_probs)

    smoothed_list = smooth1d(lst_of_probs)
    #print('sm_list', smoothed_list)

    normalizer = 1 / float(sum(smoothed_list))
    numListNormalized = [x * normalizer for x in smoothed_list]
    #print('Normalized list is\n{}\n'.format(numListNormalized))

    print('Sum of all items in numListNormalized is {}'.format(sum(numListNormalized)))
    lst_of_smoothed_probs = [ '%.5f' % elem for elem in numListNormalized]
    #print('aaaa', lst_of_smoothed_probs)
    new_list = []
    for x, y in zip(lst_of_st, lst_of_smoothed_probs):
        new_list.append(str(x)+':'+str(y))
    print('103', new_list)
    return new_list


with open(infile_gold_pos, 'r') as inf:
    for line in inf:
        pos.append(line.split(' '))

assert len(sents) == len (pos)

for s, p in zip(sents,pos):
    #print(sents)
    assert len(s) == len(p)
    for w, ps in zip(s,p):
        ls_arcs = [a for a in w[2].split('|')[:20]]
        print('number of stags: ', len(w[3:]))
        ls_st = [x for x in w[3:] if ps.strip() + ' <>' in x]
        print('number of stags with gold pos: ', len(ls_st))
        print('gold POS: ', ps.strip(), 'first 20 stags with gold pos: ', ls_st[:20])
        # if there are no stags with gold POS,
        # take the first 20 of already predicted
        if len(ls_st) == 0:
            ls_st = [x for x in w[3:23]]
        # if the sum of the probabilities does not account to 1,
        # introduce new probabilities:
        """ if float(ls_st[0].split('):')[1])<0.1:
            ls_st[0] = ls_st[0].split('):')[0]+'):0.9' """
        #if count_sum_of_probabilities(ls_st[:20]) < 0.9990:
        #    print('kkkk', count_sum_of_probabilities(ls_st[:20]))
        ls_st = rescale_stag_probs(ls_st[:20])
        print()
        new_w = w[0:3] + ls_st[:21]
        outf.write('\t'.join(new_w)+'\n')
    outf.write('\n')

outf.close()
