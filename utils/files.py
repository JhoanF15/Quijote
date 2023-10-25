def readFile(name):
  with open(name, "r", encoding="utf-8" ) as file:
    return file.read()

def wordCount(text):
  return len(text.split())

def uniqueWordCount(text):
    
    unique_words = set(text.split())
    return len(unique_words)

def findContent(text, word):

    words = text.split()
    count = words.count(word)
    return count

