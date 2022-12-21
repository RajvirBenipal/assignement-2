#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1
input = "pythoni s a case sensitive language"
print("length of the input string is",len(input))
Reverse_order = input[35::-1]
print("the reverse order is'", Reverse_order ,"'")
phrase = input[10:27]
print('''the sliced string is "''', phrase,'''"''')
New_input = input.replace("a case sensitive","obehct oriented")
print('''updated string is ''',New_input,'''"''')
index_of_a = input.find("a")
print ("the idnex of 'a' is",index_of_a)
updated_input = input.replace(" ","")
print("the new string is '",updated_input,"''") 


# In[10]:


#Q2
intro = '''Hey, ABC here!
My SID is 22XXXXXX
I am from XYZ department and my CGPA is 9.9'''

name = input("Enter your name\n")
SID = input("enter your SID here\n")
department = input("enter your department here\n")
CGPA = input("enter your CGPA here\n")

intro = intro.replace("ABC",na p)
intro = intro.replace("22XXXXXX",SID)
intro = intro.replace("XYZ",department)
intro = intro.replace("9.9",CGPA)


# In[16]:


#Q3
a= 64
b= 24
print ("value of a&b is",a&b)
print ("value of a/b is",a/b)
print("value of a^b",a^b)
print ("value of a<<2 =",a<<2,"b<<2 =",b<<2)
print("a>>2 =",a>>2,"b>>4 =",b>>4)


# In[21]:


#Q4
a = input("Enter a number here")
b = input("Enter a number here")
c = input("Enter a number here")

List_of_nos = [a,b,c]
greatest_no = max(List_of_nos)

print("The Greatest of three nos. is ",greatest_no)


# In[28]:


#Q5
statement = input("Enter any statement here")
if 'name' in statement :
    print("Yes")
else :
    print("No")


# In[ ]:


#Q6
Length_1 = input("enter any Length here")
Length_2 = input("enter any Length here")
Length_3 = input("enter any Length here")

Length_1 =int(Length_1)
Length_2 =int(Length_2)
Length_3 =int(Length_3)

if 'Length_1 + Length_2 > Length_3' and 'Length_2 + Length_3 > Length_1' and 'Length_1 + Length_3 > Length_2' :
    print("Yes")
else :
    print("No")

