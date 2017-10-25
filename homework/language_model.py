import sys
res_adr=sys.argv[1]

res_words = {}
res_tags = {}
amount = 0
stream = sys.stdin.readlines()

for line in stream:
    if line[0] == '#' or line[0] == '\n':
        continue
    else:
        amount = amount + 1
        tokens = line.split('\t')
        if tokens[3] not in res_tags:
            res_tags[tokens[3]] = 1
        else:
            res_tags[tokens[3]] = res_tags[tokens[2]] + 1
        if tokens[1] not in res_words:
            res_words[tokens[1]] = {}
            res_words[tokens[1]][tokens[3]] = 1
            res_words[tokens[1]]['count'] = 1
        else:
            res_words[tokens[1]]['count'] = res_words[tokens[1]]['count'] + 1
            if tokens[3] not in res_words[tokens[1]]:
                res_words[tokens[1]][tokens[3]] = 1
            else:
                res_words[tokens[1]][tokens[3]] = res_words[tokens[1]][tokens[3]] + 1
save = open(res_adr, 'w')
save.write('# P\tcount\ttag\tform\n')

for tags in res_tags:
    tag_proba = res_tags[tags]/amount
    save.write('%f\t%d\t%s\t_\n' % (tag_proba,res_tags[tags],tags))

for words in res_words:
    for tags in res_words[words]:
        if tags != 'count':
            word_per_tag_proba = res_words[words][tags]/res_words[words]['count']
            save.write('%f\t%d\t%s\t%s\n' % (word_per_tag_proba,res_words[words][tags],tags,words))
