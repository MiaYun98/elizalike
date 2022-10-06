# !/usr/bin/python3
'''
LING/CSE 472 Assignment 1: elizalike.py
- Updated by JCrowgey and LPoulson for Spring 2011
- Updated by Olga Zamaraeva for Spring 2018
- Updated by Naomi Tachikawa Shapiro for Spring 2021
- Updated by Sara Ng for Spring 2022

This script provides a simple automated conversation agent, in the style of
Weizenbaum's Eliza. Invoke by typing:

       python3 elizalike.py

from a command prompt or Unix shell.

This starter script handles input and output, gives an example of a regular
expression in Python, and provides a series of comments (preceded by #) that
outline what has been created for you and what you should add (i.e., TODO).

Regular expressions documentation in python
https://docs.python.org/3/library/re.html
Regular expression Scratch space
https://regexr.com/
'''
import re
import sys


def reply(text):
    # Python regular expression example ~
    # Replace all instances of "you are" with "---Elizalike-is---":
    # Note how '(\W)' is used to mark word boundaries and '\g<1>' and '\g<2>'
    # are used to retain whatever non-word character was in the input.
    # pat = r'(\W)?[Yy]ou are(\W)'
    # replace = '\g<1>I am\g<2>'
    # text = re.sub(pattern=pat, repl=replace, string=text)

    # A brief note about the above syntax ~
    # The function `re.sub()` takes three arguments: a regular expression
    # (`pattern`) to search for in the text, a replacement string (`repl`) to
    # replace it with, and the string to operate on (`string`). The function
    # returns a new string, which the above expression is storing in the
    # variable `text`.

    # TODO: Add statements for changing 2nd-person references in the input to
    # 3rd-person references (temporarily):
    # pat = r'(\W)?[Yy]ou(\W)'
    # replace = '\g<1>Them\g<2>'
    # text = re.sub(pattern=pat, repl=replace, string=text)

    # TODO: Add other transformations of the input that do not have to do with
    # personal deixis:
    # Add two Elizalike responses that involve finding a keyword in the input and
    # changing the whole string to something different.
    find_result = re.findall(r'suprised', text)
    if find_result:
        replace = 'Wow, that is cool.'
        text = replace

    find_result = re.findall(r'depressed|sad', text)
    if find_result:
        replace = 'What is going on?'
        text = replace

    # Add two Elizalike responses that involve finding a keyword in the input and
    # returning an output that retains some part of the input.
    find_result = re.findall(r'I forgot', text)
    if find_result:
        pat = r'(\W)?I forgot(\W)'
        replace = '\g<1>Yeah,\g<2>'
        text = re.sub(pattern=pat, repl=replace, string=text)

    find_result = re.findall(r'Oh, yes.', text)
    if find_result:
        text = re.sub('Oh, yes.', '', string=text)

    # 2nd person to 1st person making Temp to not get spaghetti
    pat = r'(\W)?[Yy]ou are(\W)'
    replace = '\g<1>%%%%1%\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?[Yy]ou were(\W)'
    replace = '\g<1>%%%%5%\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?Your(\W)'
    replace = '\g<1>%%%%6%\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?your(\W)'
    replace = '\g<1>%%%%3%\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?Yours(\W)'
    replace = '\g<1>%%%%7%\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?yours(\W)'
    replace = '\g<1>%%%%4%\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    # TODO: Add statements for changing 1st-person references to 2nd-person
    # references:
    pat = r'(\W)?My(\W)'
    replace = '\g<1>Your\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?my(\W)'
    replace = '\g<1>your\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?mine(\W)'
    replace = '\g<1>yours\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?I was(\W)'
    replace = '\g<1>you were\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?[Ii](\W)'
    replace = '\g<1>You\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)am(\W)'
    replace = '\g<1>are\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?I was(\W)'
    replace = '\g<1>I were\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?me(\W)'
    replace = '\g<1>you\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    # TODO: Add statements for changing 3rd-person Elizalike references to
    # 1st-person references:
    pat = r'(\W)?[Ee]lizalike is(\W)'
    replace = '\g<1>I am\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    # Temp change back to the original
    pat = r'(\W)?%%%%1%(\W)'
    replace = '\g<1>I am\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?%%%%5%(\W)'
    replace = '\g<1>I was\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?%%%%2%(\W)'
    replace = '\g<1>I\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?%%%%6%(\W)'
    replace = '\g<1>My\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?%%%%3%(\W)'
    replace = '\g<1>my\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?%%%%7%(\W)'
    replace = '\g<1>Mine\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?%%%%4%(\W)'
    replace = '\g<1>mine\g<2>'
    text = re.sub(pattern=pat, repl=replace, string=text)

    # Insert 'Elizalike: ' at the beginning of the text to identify it as
    # Elizalike's response
    text = f'Elizalike: {text}'

    # Return Elizalike's reply to the `main()` function
    return text

def main():
    print("Welcome to Elizalike. Talk to me! (Or type 'bye' to quit.)\n")

    # Start an infinite loop
    while True:

        # Read in the user's input
        text = input("Patient: ")

        # Allow the user to leave therepy
        if re.search(r'^(good)?bye', text, flags=re.I):
            print("Elizalike: Well, it was nice talking to you!\n")
            sys.exit()

        # Get Elizalike's response from the `reply()` function
        rep = reply(text)

        # Print Elizalike's reply to the console
        print(rep)


if __name__ == "__main__":
    main()
