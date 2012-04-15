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
    Phrase Based Model class - containing all functionality outlined in the aforementioned algorithm
    """

    def __init__(self):
        """
      
        """
        #self.mapped_sents = mapped_sents
        self.alignments = [(['michael', 'michael']),
                            (['assumes', 'geht']),
                            (['that', 'davon']),
                            (['he', 'aus']),
                            (['will', 'dass']),
                            (['stay', 'er']),
                            (['in', 'im']),
                            (['the', 'haus']),
                            (['house', 'bleibt'])]

    #each phrase pair from the sentence pair is generated using word alignment because
    #its words match up consistently


        self.eng_set = set()#defaultdict(list)
        self.phrase_pairs = set()#defaultdict(list)

        #self.table_ef = defaultdict(lambda: defaultdict(int)) #t(e|f) table
        #self.count_ef = defaultdict(lambda: defaultdict(int)) #count(e|f) table
        #self.total_f = defaultdict(int) #total(f) table
        #self.s_total_e = defaultdict(int) #s_total(e) table

    def extract(self, f_start, f_end, e_start, e_end):
    #this could probably be recursive

    """
    The extraction of word alignments for sentence pairs.
    Input: Word alignment A for sentence pair (e,f)
    Output: Set of phrase pairs BP
    """
    if f_end == 0: # check if at least one alignment point
        return set()

    for e,f in self.alignments:
        if e < e_start or e > e_end:
            return set()
    # add phrase pairs (incl. additional unaligned f)
    count_e = f_start
    print "initial count_e = ", count_e

    for s in self.alignments:
        sent_e = s[0] #english sentence pair
        sent_f = s[1] #foreign sentence pair

        #count_e, count_f = 0 #len(sent_e)
        
        while (count_f != len(sent_e): #i'm guessing NOT ALIGNED to mean all it's possible alignments have not been considered yet
            count_f = f_end
            print "count_f = ", count_f

            while (count_e != len(sent_f)):
                self.eng_set.add((e_start, f_start))  #add phrase pair (e_start..e_end, fs..fe)
                count_f += 1

            count_e -= 1     

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
                for e,f in self.alignments:
                    if e_start <= eng_sent <= e_end:
                        f_start = min(f, f_start)
                        f_end = max(f, f_end)

                self.phrase_pairs.add(self.extract(f_start, f_end, e_start, e_end))


    







      

#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
