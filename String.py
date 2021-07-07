#String Utility

print("Hello World")

text = "Hello"
print(text)

a = "ABC"
print(len(a))

text = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(text)

a = """
Hello
world
"""
print(a)

s = "SAMIR"
#print(s[0])
#print(s[1])
#print(s[2])

for i in "SAMIR":
    print(i)

mail = "samir@nsu.edu.bd"
if "@iub.edu.bd" in mail:
    print("IUB MAIL!")
else:
    print("Wrong mail!")