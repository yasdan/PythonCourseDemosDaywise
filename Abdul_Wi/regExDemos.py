import re     # needed for regular expressions

# Find all function
text = "Hello! how are you?"
res = re.findall("are", text)
print(res)

# search function
res=re.search("are",text)
print(res," The match found at ",res.start())

# split function
res= re.split(" ",text)
print(res)
for word in res:
    print(word)

# sub() replaces the matches with our text
res= re.sub("o","A",text)
print(res)

# sub() replaces the mathes with our text with first 'n' occurence
res= re.sub("o","O",text,1)
print(res)

#meta characters applying
res= re.search("^Hello",text)
print(res)

res= re.search("^how",text)
print(res)

res=re.search(r"\by",text)
print(res)

res=re.search(r"\bw",text)
print(res)

p = re.compile(r'\b(\w+)\s+\1\b')
res=p.search('Paris in the the spring').group()
#res=p.search(text).group()
print(res)


email ="abdul1234@gmail.com"
pat=re.compile(r"\b[a-z]*\d+")
res= pat.search(email)
print(res)
pat1=re.compile(r"\d+")
res1= pat1.search(email)
print(res1)
pat2=re.compile(r"@\D*")
res2=pat2.search(email)
print(res2)

strno="969"
no= int(strno)
print(no,no+100 )

slist = re.split(r'\@',email)
print(slist)
hs= re.split(r'[a-z]+',email)
print(hs)
ilist = re.split(r'@+',email)
print(ilist)

jk=re.split(r'\.+',email)
print(jk)

res=re.split(r'[\d]',email)
res1= re.split(r'(\w)',email)
print(res)
print(res1)
lk=re.findall(r'(\w+)',email)
print("lk  is",lk)
#gk= re.findall(r"(\@.....)",email)
gk= re.findall(r"(\@\w*)",email)
print(gk)
#dt= re.findall(r"(\....)",email)
dt= re.findall(r"(\.\w*)",email)

print(dt)
comp_list=[lk[0],gk,dt]
print(comp_list)
