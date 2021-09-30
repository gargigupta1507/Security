#!/usr/bin/python2.7

#character set English albhabet say 26 A-Z (n)
#write a program to bruteforce a password of length 8 (k)

#number of combinations = n^k = 26^8
#print all passwords in a file: password.txt

#write passwords in file
file = open("1_password.txt", "w")

#Recursion logic
def generatePass(charset, n, k, prefix):
    if (k == 0):
        print prefix
        file.write(prefix + "\n")
        return

    for i in range (n):
        newprefix = prefix + charset[i];
        generatePass(charset, n, k-1, newprefix)

#Wrapper function
def allPasswords(charset, k):
    n = len(charset)
    generatePass(charset, n, k, "")


#Driver function

#charset = ["a","b","c","d","e","f","g","h","i","j"]
charset = ["a","b"]
k = 2

allPasswords(charset,k)
file.close()

