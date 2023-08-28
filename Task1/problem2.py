import re

#The Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8 
def Coleman_Liau(l,s,w):
    L=(l/w) * 100
    S=(s/w) * 100
    return round((0.0588 * L) - (0.296 * S) - 15.8)
#to print output
def grade (x):
    if x<1:
        print("Before Grade 1")
    elif x>=16:
        print("Grade 16+") 
    else:
        print(f"Grade {x}")

#taking input from user   
paragraph=input("Enter Paragraph: ")

#used function 
# re.findall(pattern, string): Finds all occurrences of the pattern in the string and returns them as a list.
# re.split(pattern, string): Splits the string based on the occurrences of the pattern and returns a list of substrings.

#calculate word
words = len(paragraph.split())
print("Number of words:", words)

#Calculate letters
letters = len(re.findall(r"\w", paragraph))
print("Number of letters:", letters)


# Calculate sentences
sentences = len(re.findall(r"[.!?]+", paragraph))
print("Number of sentences:", sentences)

grade_num=Coleman_Liau(letters,sentences,words)
grade(grade_num)

