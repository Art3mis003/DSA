def encode(strs):
    answer=""
    for s in strs:
        answer+= str(len(s)) + "$" + s
    return answer

def decode(str):
    answer, i=[],0
    while i < len(str):
        j=i
        while str[j]!= '$':
            j+=1
            length= int(str[i:j])
            answer.append(str[j+1 : j+1+length])
            i= j+1+ length
    return answer

array=["hello", "world"]
k= encode(array)
print(k)
j=decode(k)
print(j)

