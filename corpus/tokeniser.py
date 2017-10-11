import sys
text = sys.stdin.readlines()
sentence_1 = 1
for i in range (0, len(text)):
    line = text[i].strip()
    if line == "":
        continue
    print("#sent_id =",i+1,"\n"+"#text=",line)
    token_id = 1
    punctuation = [".",",","?","!",":",";"]
    for symbols in punctuation:
        line = line.replace(symbols, " " + symbols)
    sentence_id = line.split(" ")
    tokens = line.split(" ")
    for token in tokens:
        print("%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_"%(token_id, token))
        token_id=token_id+1
    print()
