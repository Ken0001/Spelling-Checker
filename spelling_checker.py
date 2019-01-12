import re, collections
def words(text):
    return re.findall('[a-z]+', text.lower())#将文本中的单词分离开 返回一个列表
def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model
NWORDS = train(words(open('dictionary.txt').read()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts = [a + c + b for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
    return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    # print(candidates)
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

    return mylist

while(1):
    userInput = input("Enter your word:")
    correct(userInput)
    #print(correct(userInput))