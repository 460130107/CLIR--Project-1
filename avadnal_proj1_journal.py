#Andrew Vadnal
#326558
#24/4/2012
#Project 1 (Phrase Based Model)
#Journal
'''
============= The allocated time for this project is 24 hours.=============

Hour 1. Spent in the tutorial before the Easter week break. Was primarily
reading the supplied paper for the Phrase Based Model. It looks really
interesting, and I can understand how it relates to real world translations.
Seems much more practical than the simple word alignments seen in the previous
assignment using IBM Model 1. However, I did not get through the entire paper
and will continue to read it next time.

Hour 2. Read the remainder of the section of the Phrase Based Model in addition
to the subsequent sections on log-linear models and lexical weighting/word
penalties. If I decide to implement a PBM, I plan to implement the outlined
algorithm first. If time permits, I will incorporate some of the aforementioned
techniques in order to observe whether this improves the quality of the returned
phrase pairs. I will now investigate the higher IBM Models (Model 2 and 3
possibily).

Hour 3. Read about IBM Model 2. Found IBM Model 2 algorithm: http://www-
rohan.sdsu.edu/~gawron/mt_plus/mt/course_core/lectures/assignment_five.pdf
Continued researching IBM Model 2.

Hour 4. Reading about IBM Model 3, still not sure whether or not to implement
the IBM Models or not. I feel like challenging myself by implementing a
completely new algorithm. At this point in time, the Phrase Based Model
interests me the most. Started reading about the Compressed Term Index approach
(chapter 4 - provided).

Hour 5. Skimmed through the remainder of chapter 4 and began reading chapter 5
of the Compressed Term Index. Read this purely out of curiousity, in order to
get an idea of the sort of implementable CLIR components. Based on what I have
read, I'm going to stick with the implementation of a Phrase Based Model; using
the provided algorithm in the Koehn paper (chapter 5).

Hour 6. Started development. Setting up the file, implementing the phrase
extraction algorithm - figure 5.5, Koehn chapter 5 -
http://langtech.github.com/clir/materials/koehn-05.pdf. WORD ALIGNMENT, so
instead of inputting pairs of words like in the IBM Model 1 assignment, give as
input word-level alignments.

Hour 7-8. Development. My current uncertainties arise primarily from the data
structures to use and what is meant by the two loop conditions: "until fe
aligned" and "fs aligned". For the time being, I'm assuming that this means
'while each fe has been processed against every fs and vice versa'. I initially
used the defaultdict data structure primarily because it was used in the
previous assignment, however it doesn't look like this algorithm really requires
the need for dictionaries so I'm going to be using sets for storing phrase pairs
and word alignments initially. This is subject to change, as when I start
compiling and testing the chosen data structures may or may not be adequate.
Continued development will tell.

Hour 8-14. Development. Spent a little too much time messing  around with the
data structures I was implementing. (A good 1-2 hours messing around in the
Python shell I'll shamely admit) This was a combination of both starting
development without being 100% certain of the data I was going to be getting and
how it was going to be stored and also not knowing how to process Python lists
and sets as well as I would have liked. Despite this, I feel like I've furthered
my understanding of the algorithm - but still require some questions to be
answered. I will ask Steven these in the tutorial on 18/4. These questions
involve the program input itself, as to whether I am processing the entire
alignment table or if I'm specifying a list  of correct 1-1, word to word
alignments and processing them instead. The Koehn paper mentions 'word-aligned
sentence pairs', but also draws on the importance of an alignment table (which I
failed to include in my code during Hour 7-8) in processing the phrase pairs.
I'm currently outputting a value consistent with the paper in regards to the
number of contiguous English phrase pairs (which is 36) from the hard coded
sentence examples, however the list contains all null vals. I believe this
problem should be simple to remedy, given that my uncertainties are clarified
and I feel I'm certainly more than half way there in regards to a complete
algorithm implementation.

Hour 15. Spent in the tutorial. It was a helpful tutorial, as I was able to
identify some errors in the way I was handling data in my program. Firstly, I
learned that the program input itself is the word alignments, namely a list of
(e,f) offset pairs instead of the actual words themselves. I was neglecting this
data completely up until this point, and how it fits into the algorithm is more
evident to me now. I have hard-coded the word alignments in that correspond to
the phrase table in the Koehn paper for the time being. My current uncertainty
is still regarding the two loop exit conditions: 'until fe aligned' and 'until
fs aligned'. The way I understand the algorithm is that we are extracting phrase
pairs from a populated phrase table (courtesy of the word alignment list) - and
not actually doing any physical aligning. I feel like I might have to do some
hacking with different exit conditions to see if desirable output is achieved.
If I have no luck, I'll most likely turn to Google. If this fails as well, I'll
send Steven an email to see if he can help out.

Hour 15-18. After tracing through my code, I discovered that my two repeat loops
were never being reached. This was due to the empty set being returned each
time, as the condition e < e_start or e > e_end was being met each run through
the extract function. Further, it was only processing the first word alignment
pair each time, as the function was returning set() each run through the for
loop, and would begin at this same position each time the extract function was
called. I worked around this by adding a global counter, which was calling (for
e) word_alignment[counter][0] each time the check was performed, where counter <
length of word alignment table. I'm suspecting that the check listed in the
algorithm might not cover all the possible cases that should be checked. See how
I go in the tutorial tomorrow.

Hour 19. Spent in the tutorial. My suspicions were correct, in that the
aforementioned for loop was not covering all possible conditions. Added in
checks to see if the phrase pairs are being consistent with the word alignment.
4 in total. An empty set is no longer being returned each time. However, I'm
unsure if I'm adding in the phrase pairs correctly - as described in line 12 of
the extract function.  I'm also still unsure about the two exit conditions
specified. I feel I'm about 80% complete at this point in time - just needing to
properly add in the phrase pairs (which I should be obtaining correctly) and
understanding the two exit conditions.

Hour 20-24. Finished off the assignment. It is now replicating the output
produced in the Koehn paper which I am happy about. Never quite worked out
exactly what the two while exit conditions were, but using 2 while true loops
seemed to be a nice work around. Found some crucial bugs in my code from last
time - which were both occurring in the extract function. (I can't remember why
but) I commented out the population of my f_index array - which kept a track of
the the foreign index values in my word alignment list, causing these indexes to
not be processed at all. Secondly the phrase pair I was adding was (e_start,fs)
instead of ((e_start,e_end), (fs_fe)). Lastly, I had been getting confused with
the way this algorithm had generated output. For example, given output like
[(a,b), (c,d)] (which are all numerical + a phrase pair) I was referencing my
word table by key (a,b) and getting out one value. What I didn't realise was
that (a,b) is in fact A RANGE. This allowed me to reference my original sentence
and print out all words which corresponded to the lower bound a and the upper
bound b for both english and foreign. Once these issues were figured out,
resolving my past issues were relatively trivial.
'''
