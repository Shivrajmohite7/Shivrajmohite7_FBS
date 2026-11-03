import re

text = """
Welcome to TechNova Solutions Pvt Ltd!

Our company was established in 2015.
For more information, contact us at:
Email: support@technova.com
HR Email: hr.tech@gmail.com
pr.abc@gmail.com
Sales Email: sales123@yahoo.in

Contact Numbers:
9876543210
8765432109
+91-9988776655
+91-9394949334
+91-3994949434
020-45678901

Employee Details:
Name: Rahul Sharma, Age: 25, Salary: 45000
Name: Priya Patil, Age: 28, Salary: 55000
Name: Amit Verma, Age: 32, Salary: 65000
Name: Sneha Kulkarni, Age: 24, Salary: 40000

Employee IDs:
EMP101, EMP102, EMP103, EMP104

Website:
https://www.technova.com
http://www.google.com
https://www.python.org

Product Details:
Laptop - Price: 55000
Mobile - Price: 25000
Keyboard - Price: 1500
Mouse - Price: 800

Dates:
12-05-2025
25/08/2024
2025-11-03

Some random text:
PARROT
Python is easy to learn.
Python123 is a programming language.
Regex is powerful.
abc123xyz
HELLO123
test@123

Address:
Pune, Maharashtra, India
Mumbai, Maharashtra, India
Delhi, India """

# print(text)

# Extract all digits from the text.
d1=re.findall(r'\d',text)
print(d1)

# Extract all numbers from the text.
d2=re.findall(r'[\d]+',text)
print(d2)

# Extract all uppercase words.
d3=re.findall(r'[A-Z]+',text)
print(d3)

d3 = re.findall(r'[A-Z]{2,}', text)
print(d3)

# find all words in text 
d4=re.findall(r'[a-zA-Z]{2,}',text)
print(d4)

# extract all lowercase words 
d5=re.findall(r'\b[a-z]+\b',text)
print(d5)

# Find all words starting with P.

d6=re.findall(r'P[A-Za-z]{2,}',text)
print(d6)

# Find all words ending with a
d7=re.findall(r'\b[A-Za-z]+a\b',text)
print(d7)

# Extract all numbers containing exactly 3 digits.
d8=re.findall(r'[\d]{3}',text)
print(d8)

# Find all words having exactly 5 characters.
d9=re.findall(r'\b[A-Za-z]{5}\b',text)
print(d9)

# Extract all email addresses.
# hr.tech@gmail.com
pat = r"[a-z]+\.[a-z]+@[a-z]+\.[a-z]{2,}"
# pat = r'[a-z]+\.[a-z]+@[a-z]+\.[a-z]{2,}'
d10=re.findall(pat,text)
print(d10)

# Extract all mobile numbers containing exactly 10 digits.

d11=re.findall(r'[0-9]{10}',text)
print(d11)

# Extract all mobile numbers containing exactly 10 digits.

pat=r"\+91[- ][0-9]{10}"

d12=re.findall(pat,text)
print(d12)

pat=r'\+91[-][0-9]{10}'
d14=re.findall(pat,text)
print(d14)