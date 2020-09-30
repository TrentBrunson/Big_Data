#%%
import nltk
from nltk import word_tokenize
#%%
text = word_tokenize("I enjoy biking on the trails")
output = nltk.pos_tag(text)
print(output)
# %%
text = word_tokenize("Coding is fun!")
output = nltk.pos_tag(text)
print(output)
# %%
text = word_tokenize("According to a more specific definition presented by Trasatti,[2] the absolute electrode potential is the difference in electronic energy between a point inside the metal (Fermi level) of an electrode and a point outside the electrolyte in which the electrode is submerged (an electron at rest in vacuum).")
output = nltk.pos_tag(text)
print(output)
# %%
text = word_tokenize("NLP failed for the previous technical example.")
output = nltk.pos_tag(text)
print(output)