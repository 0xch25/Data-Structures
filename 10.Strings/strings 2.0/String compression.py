strg="aaabbcccc"
st=""
for s in sorted(set(strg)):
    st+=s
    c=strg.count(s)
    st+="%s"%c
print(st)
