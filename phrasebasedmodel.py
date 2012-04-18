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

class Phrase_Based_Model:
    """
    Phrase Based Model class - containing all functionality outlined in
    the aforementioned algorithm
    """
    def __init__(self, word_alignments, sent_pairs, alignment_table):
        """
        Class constructor. 
        Input: Word level alignment mapping between english->foreign
        Input: Sentence pairs (e,f). Data structure is a list of lists, where
               e is represented by sent_pairs[0] and f by sent_pairs[1]    
        """

        #each phrase pair from the sentence pair is generated using word
        #alignment because its words match up consistently
        self.alignment_table = alignment_table
        self.eng_sent = sent_pairs[0]

        self.for_sent = sent_pairs[1]
        self.word_alignments = word_alignments

        self.eng_set = set()#defaultdict(list)
        self.phrase_pairs = list()#defaultdict(list)

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
        print "e_start =", e_start
        if f_end == 0: # check if at least one alignment point
            print "YES F_END == 0"
            return set()

        for e,f in self.word_alignments:
            print e,f
            if e < e_start or e > e_end:
                print "YES E<ESTART OR E>END"

                return set()
        # add phrase pairs (incl. additional unaligned f)
        count_e = f_start
        print "initial count_e = ", count_e
            
        while count_f != len(sent_e): 
            #i'm guessing NOT ALIGNED to mean all its possible alignments
            #that have not been considered yet
            count_f = f_end
            print "count_f = ", count_f

            while count_e != len(sent_f):
                self.eng_set.add((e_start, f_start))
                #add phrase pair 
                #(e_start..e_end, fs..fe)
                count_e += 1

            count_f -= 1

        return self.eng_set     

    def execute(self, eng_sent, for_sent):
        """
        Execution of the phrase pair extraction algorithm
        Input: Sentence pair (e,f)
        Output: 
        """    
        for e_start in range(1, len(eng_sent)):
            for e_end in range(e_start, len(eng_sent)):
                # find the minimally matching foreign phrase
                f_start = len(for_sent)
                f_end = 0

                for e,f in self.word_alignments:

                    if e_start <= e <= e_end: #hmm
                        #print "YES - estart<=e<=eend"
                        f_start = min(f, f_start)
                        f_end = max(f, f_end)
  
                print "Passing fstart = %d, fend = %d, estart = %d\
                        eend = %d" %(f_start, f_end, e_start, e_end)
                #print "fstart = %s\n f_end = %s\n, e_start = %s\n, e_end = %s\n"  % (f_start,f_end,e_start,e_end)
                extraction = self.extract(f_start, f_end, e_start, e_end)
                print "extraction= ", extraction
                #self.phrase_pairs.append(extraction)
        #print "Now outputting self.phrase_pairs"
        #print "-------------------------------"

        #for item in self.phrase_pairs:
            #print item
e = "michael assumes that he will stay in the house".split()
f = "michael geht davon aus dass er im haus bleibt".split()

word_alignments = [(1,1),(2,2),(2,3),(2,4),(3,6),(4,7),(5,10),
                   (6,10),(7,8),(8,8),(9,9)]

sent_pairs = list(e), list(f)
#word_alignments = zip(e,f) #Word-word alignments

alignment_table = list() #The alignment table
[alignment_table.append((x,y)) for x in e for y in f]


pbm = Phrase_Based_Model(word_alignments, sent_pairs, alignment_table)
pbm.execute(pbm.eng_sent, pbm.for_sent)
print len(pbm.phrase_pairs)
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
