def URLify(st):
    ss=st.strip()
    return ss.replace(" ","%20")
st="Mr John Smith        "
print(URLify(st))