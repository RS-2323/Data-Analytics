#Web scraping and crawling recursively for a link
"""
Code Challenge 2
Write a generator "trange", which generates a sequence of time tuples from 
start to stop incremented by step.
 A time tuple is a 3-tuple of integers: (hours, minutes, seconds)

Example
for time in trange((10, 10, 10), (13, 50, 15), (0, 15, 12) ):
    print(time)

will return

(10, 10, 10)
(10, 25, 22)
(10, 40, 34)
(10, 55, 46)
(11, 10, 58)
(11, 26, 10)
(11, 41, 22)
(11, 56, 34)
(12, 11, 46)
(12, 26, 58)
(12, 42, 10)
(12, 57, 22)
(13, 12, 34)
(13, 27, 46)
(13, 42, 58)
"""