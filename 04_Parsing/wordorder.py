import sys

count_VO = 0
count_OV = 0

# File name needs to be changed when the code is applied to different languages.
with open("ko_kaist-ud-train.conllu") as f:
    sent = []
    for line in f:
        if line != '\n':
            if line[0] != '#':
                line = line.split('\t')
                sent.append(line)
        else:
            for s in sent:
                if s[7] == 'obj':
                    if int(s[6]) < int(s[0]):
                        count_VO += 1
                    else:
                        count_OV += 1

            sent = []

p_VO = count_VO / (count_VO + count_OV)
p_OV = count_OV / (count_VO + count_OV)

print(p_VO)
print(p_OV)
