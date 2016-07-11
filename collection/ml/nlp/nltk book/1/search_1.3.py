import nltk
# load texts
from nltk.book import *

# show every occurrence of a given word, together
text1.concordance("monstrous")

# find words which appear in the context that same as parameter
text1.similar("monstrous")

# find same context of words
text2.common_contexts(["monstrous", "very"])

# determine location of a word in the text
text4.dispersion_plot(["citizens", "democray", "freedom", "duties", "America"])

