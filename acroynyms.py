input=str(input('enter a  phrase:'))
text=input.split()
a=''
for i in text:
    a=a+(i[0]).upper()
print(a)