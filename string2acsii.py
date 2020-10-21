# https://www.facebook.com/jyothiprakash.patnaikuni/posts/107593291135289
# subscribed by jyothiprakash patnaik



#convert String in to ascii PY
dist={}
string="om sai ram"
list_ls=string.split()
for sub in list_ls:
    for ch in sub:
        dist[ch]=ord(ch)

print(dist)

