import sys
#open the file ready for reading
fd = open('model.txt', 'r')
frequent_tag = 'x' # variable to store the most frequent tag we have seen
last_max = 0 # variable to store the comparison
word_tag = {} # word_tag{'cat'} = 'NOUN'
word_prob = {} #word_prob{'cat'} = 0.6
for line in fd.readlines():
  line = line.strip()
  if line[0] == "#":
      continue
  line = line.split('\t')
  if int(line[1])>last_max:
    last_max = int(line[1])
    frequent_tag = line[2]
  surface_form = line[3]
  prob = float(line[0])
  tag = line[2]
  if surface_form not in word_tag:
    word_tag[surface_form] = tag
    word_prob[surface_form] = prob
input = sys.stdin.readlines()
for line in input:
    line = line.strip()
    if "\t" not in line:
        print(line)
        continue
    line = line.split("\t")
    if line[1] in word_tag:
        line[3] = word_tag[line[1]]
    else:
        line[3] = frequent_tag
    print("\t".join(line))
