### Spelling Checker
This program will get user input and check it right or not in the dictionary.txt, and then it will list the three most relevant words.
I use Bayes' theorem to choose words

>This function calculate the number of occurrences of each word 
```python=
def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model
```

>NWORDS[w] means "w" show up times in the dictionary.txt
```python=
NWORDS = train(words(file('big.txt').read()))
```

>Edit a word can use split, delete, transpose, replace, and insert

```python=
def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)
```
>This function will find most three words if the input is a wrong word
```python=
def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    mylist=[]
    M1 = max(candidates, key=NWORDS.get)
    print(M1)
    candidates.remove(M1)
    mylist.append(M1)
    if(candidates):
      M2 = max(candidates, key=NWORDS.get)
      mylist.append(M2)
      print(M2)
      candidates.remove(M2)
    if(candidates):
      M3 = max(candidates, key=NWORDS.get)
      mylist.append(M3)
      print(M3)
```
Reference:
>  https://blog.csdn.net/u013830811/article/details/46539919
