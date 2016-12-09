# Fingerprint-classification
The Henry Classification System for fingerprint grouping.

Each of the fingers is assigned an index as follows:
+ Left Pinky = 10
+ Left Ring = 9
+ Left Middle = 8
+ Left Index = 7
+ Left Thumb = 6
+ Right Pinky = 5
+ Right Ring = 4
+ Right Middle = 3
+ Right Index = 2
+ Right Thumb = 1

Fingers can have three types of patterns - Arches, Loops and Whorls. If a finger contains a Whorl pattern it is given a score based on its index:
- 10 and 9 have a score of 1.
- 8 and 7 have a score of 2.
- 6 and 5 have a score of 4.
- 4 and 3 have a score of 8.
- 2 and 1 have a score of 16.

The grouping ratio for the fingerprints is:
__N / D__  
where the numerator N = 1 + Score for even indices,  
and the denominator D = 1 + Score for odd indices.

There are up to 1024 primary groupings available through this method.

####Usage:
_f = Fingerprint()_  
_A = ['W', 'L', 'A', 'L', 'W', 'W', 'A', 'L', 'A', 'W']_  
_f.Henry(A)_  
__[6, 21]__  

