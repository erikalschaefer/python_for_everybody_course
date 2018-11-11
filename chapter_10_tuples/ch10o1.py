"""Chapter 10-1 practice on tuples."""

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()

for word in words:
    t.append((len(word) , word))

print ('The first loop builds a list of tuples, where each tuple is preceded by its length:' , t)
print ('---------------------------------------------')

t.sort(reverse=True)
print ('After it puts the tuple in order', t)

res = list()
for length, word in t:
    res.append(word)
print('----------------------------')
print ('FINAL LIST', res)