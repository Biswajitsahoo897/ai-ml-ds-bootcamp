st = input("Enter The Message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if coding == "1" else False

nwords = []

if coding:   # Encoding
    for word in words:
        if len(word) >= 3:
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
        else:
            stnew = word[::-1]
        nwords.append(stnew)
else:        # Decoding
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]      # remove r1 and r2
            stnew = stnew[-1] + stnew[:-1]  # rotate back
        else:
            stnew = word[::-1]
        nwords.append(stnew)

print(" ".join(nwords))
