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
    
    """

    def __init__(self, mapped_sents):
        """
      
        """
        #self.mapped_sents = mapped_sents
        alignments = [(['the', 'house'], ['das', 'haus']),
                 (['the', 'book'], ['das', 'buch']),
                 (['a', 'book'], ['ein', 'buch'])]

        self.table_ef = defaultdict(lambda: defaultdict(int)) #t(e|f) table
        self.count_ef = defaultdict(lambda: defaultdict(int)) #count(e|f) table
        self.total_f = defaultdict(int) #total(f) table
        self.s_total_e = defaultdict(int) #s_total(e) table

    def extract(self, f_start, f_end, e_start, e_end):
    """
    The extraction of word alignments for sentence pairs.
    Input: Word alignment A for sentence pair (e,f)
    Output: Set of phrase pairs BP
    """
    if f_end == 0: # check if at least one alignment point
        return {}




    def execute(self):




      

#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
