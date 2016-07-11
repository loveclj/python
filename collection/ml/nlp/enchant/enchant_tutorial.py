import enchant
from enchant.checker import SpellChecker
from enchant.tokenize import get_tokenizer

# module enchant description
# http://pythonhosted.org/pyenchant/tutorial.html#id9

# language is US-English, not English
us_dict = enchant.Dict("en_US")
# language is English
en_dict = enchant.Dict("en")

# "color" is US-English, "colour" is English, "colorr" is wrong
test_words = ["color", "colour", "colorr"]

print "#### test US-English ####"
# check US-English
for word in test_words:
    # check word is correct or not
    if us_dict.check(word):
        print "word is correct"
    else:
        print "word is error"
        print "word may be: ",
        print us_dict.suggest(word)


print "#### test combine dictionary ####"
# combine dictionary, add words in file to dictionary
combine_dict = enchant.DictWithPWL("en_US", "my_words.text")
if combine_dict.check(test_words[1]):
    print "combine dictionary has the word: %s" %(test_words[1])
else:
    print "combine dictionary doesn't have word: %s" %(test_words[1])

print "#### test SpellChecker ####"
test_text = "it's okay, tomorow is a god choise"
chkr = SpellChecker("en_US")
chkr.set_text(test_text)
# return error words_list
# god is an error, but it's a spell error
for err in chkr:
    print "[ERROR]: %s " %(err.word)

print "#### test tokenizer ####"
test_tokenizer_text = "It rains dog and cat. What? Dog and cat?"
tknzr = get_tokenizer("en_US")
tknzr_rlt = tknzr(test_tokenizer_text)
# return is a tuple, first is word, second is position
for w in tknzr_rlt:
    print w

