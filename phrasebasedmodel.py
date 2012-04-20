#Andrew Vadnal
#326558
#[date]
#Project 1 - Phrase Based Model (implementation)

"""
Implementation of the Phrase Based Model outlined in Koehn Chapter 5
http://langtech.github.com/clir/materials/koehn-05.pdf
"""
from __future__ import division
from collections import defaultdict
import nltk_align

class Phrase_Based_Model:
    """
    Phrase Based Model class - containing all functionality outlined in
    the aforementioned algorithm
    """
    def __init__(self, aligned_sent, alignment_table):#word_alignments, sent_pairs, alignment_table):
        """
        Class constructor. 
        Input: Word level alignment mapping between english->foreign
        Input: Sentence pairs (e,f). Data structure is a list of lists, where
               e is represented by sent_pairs[0] and f by sent_pairs[1]    
        """

        #each phrase pair from the sentence pair is generated using word
        #alignment because its words match up consistently
        self.alignment_table = alignment_table

        #methods from NLTK.align module
        self.eng_sent = aligned_sent.words#sent_pairs[0]
        self.for_sent = aligned_sent.mots#sent_pairs[1]
        self.word_alignments = aligned_sent.alignment#word_alignments

        self.eng_set = set()#defaultdict(list)
        self.phrase_pairs = list()#defaultdict(list)

        self.e_count = 0

        #self.table_ef = defaultdict(lambda: defaultdict(int)) #t(e|f) table
        #self.count_ef = defaultdict(lambda: defaultdict(int)) #count(e|f) table
        #self.total_f = defaultdict(int) #total(f) table
        #self.s_total_e = defaultdict(int) #s_total(e) table

    def extract(self, f_start, f_end, e_start, e_end):
        """
        The extraction of word alignments for sentence pairs.
        Input: Word alignment A for sentence pair (e,f)
        Output: Set of phrase pairs BP
        """
        #print "\n"
        #print "args=fstart,fend,estart,eend"
        #print "args=%d,%d,%d,%d"%(f_start,f_end,e_start,e_end)
        #print "\n"
        if f_end == -1: # check if at least one alignment point
            print "YES F_END == 0"
            return set()

        #print len(self.word_alignments)
        #for e,f in self.word_alignments:
        #    print e,f
        for e,f in self.word_alignments:
            if (e_start <= e <= e_end
                and
                f_start <= f <= f_end
                ):
                continue
            
            elif (e_start > e or
                  e_end < e) and (f_start > f or f_end < f):
                continue
            
            elif (f_start > f or
                  f_end < f) and (e_start <= e <= e_end):
                return set()

            elif (e_start > e or
                  e_end < e and f_start <= f <= f_end):
                return set()
                     
        # add phrase pairs (incl. additional unaligned f)
        fs = f_start
        print fs
        f_index = []
        for e,f in self.word_alignments:
            f_index.append(f)


        for i in f_index:
            print i
        while fs != len(self.word_alignments): 
            fe = f_end

            while fe != len(self.word_alignments):
                self.eng_set.add((e_start, f_start))
                #add phrase pair 
                #(e_start..e_end, fs..fe)
                fe += 1
                if fe in f_index or fe > len(self.for_sent)-1:
                    break

            fs -= 1
            if fs in f_index or fs < 0:
                break
            

        return self.eng_set     

    def execute(self, eng_sent, for_sent):
        """
        Execution of the phrase pair extraction algorithm
        Input: Sentence pair (e,f)
        Output: 
        """    
        for e_start in range(0, len(eng_sent)):
            for e_end in range(e_start, len(eng_sent)):
                # find the minimally matching foreign phrase
                f_start = len(for_sent)-1
                f_end = 0

                for e,f in self.word_alignments:

                    if e_start <= e <= e_end: #hmm
                        f_start = min(f, f_start)
                        f_end = max(f, f_end)

                extraction = self.extract(f_start, f_end, e_start, e_end)
                self.phrase_pairs.append(extraction)
                print "extraction= ", extraction
                #self.phrase_pairs.append(extraction)
        #print "Now outputting self.phrase_pairs"
        #print "-------------------------------"

        #for item in self.phrase_pairs:
            #print item
e = "michael assumes that he will stay in the house".split()
f = "michael geht davon aus dass er im haus bleibt".split()
word_alignments = [(0,0),(1,1),(1,2),(1,3),(2,5),(3,6),(4,8),
                   (5,8),(6,7),(7,7),(8,8)]

alignment_table = defaultdict(lambda: defaultdict(int))
for i,j in word_alignments:
    alignment_table[i][j] = 1

aligned_sent = nltk_align.AlignedSent(e, f, word_alignments)


#sent_pairs = list(e), list(f)
#word_alignments = zip(e,f) #Word-word alignments


#alignment_table = list() #The alignment table
#[alignment_table.append((x,y)) for x in e for y in f]


pbm = Phrase_Based_Model(aligned_sent, alignment_table)#word_alignments, sent_pairs, alignment_table)
pbm.execute(pbm.eng_sent, pbm.for_sent)
#print len(pbm.phrase_pairs)
#36 phrase pairs (there are 36 distinct contiguous English phrases)

"""
word_alignments = [(['michael', 'michael']),
             (['assumes', 'geht'])]
eng = list()
foreign = list()

[eng.append(word[0]) for word in word_alignments]
[foreign.append(word[1]) for word in word_alignments]
sent_pairs = list((eng, foreign))

#print pbm.eng_sent

"""


#sent_pairs[0] = eng sentence, [1] = for sentence 

"""
 (['that', 'davon']),
 (['he', 'aus']),
 (['will', 'dass']),
 (['stay', 'er']),
 (['in', 'im']),
 (['the', 'haus']),
 (['house', 'bleibt'])]
"""


#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
