from urllib.request import urlopen

line_limit = 60

# REMOVE HTML TAGS

html = urlopen("https://likesscoer.github.io").read()
texto = (html.decode('utf-8'))


is_html = False
my_text = ''
for i in texto:
	if i == '<':
		is_html = True
		continue
	if i == '>':
		is_html = False
		continue
	if not is_html:
		my_text += i


strip = my_text.strip()
x = strip.split()


parrafo = ''
for i in x:
	if i == '&nbsp;':
		parrafo += '\n\n'
		continue
	parrafo += i + ' '

new_parrafo = parrafo.replace('&quot;', '"')

f = open('My text.txt', 'w')
f.write(new_parrafo)
f.close()





# ALIGN TEXT

def space_fill(line, limit):
    return line + " " * (limit-len(line))


def split_string (string, limit):
    words = string.split()
    sep = ' '
    res = []
    part = words[0]
    others = words[1:]
    for word in others: 
        if len(sep)+len(word) > limit-len(part):
            res.append(part)
            part = word              
        else:
            part += sep+word

    if part:
        res.append(part)

    result = [space_fill(line, limit) for line in res]
    return result



text = open('My text.txt', 'r')
f = len(text.readlines())


text = open('My text.txt', 'r')
myFile = open('align{}.txt'.format(line_limit), 'w')

for i in range(f):
	x = text.readline()
	if x == '\n':
		myFile.write('\n')
		print('\n')
		continue
	for line in split_string(x, line_limit):
		myFile.write(line + '\n')
		print(line, len(line))

myFile.close()

