import PyPDF4 as pd

filename = input('Path to the file: ')

file = open(filename, 'rb')
pdfReader = pd.PdfFileReader(file)


tried = 0

if not pdfReader.isEncrypted:
    print('The file is not encrypted! You can successfully open it!')

else:
    wordListFile = open('word.txt', 'r')
    body = wordListFile.read().lower()
    words = body.split('\n') # create the password column list

    for i in range(len(words)):
        word = words[i]
        print('Trying decryption by: {}'.format(word))
        result = pdfReader.decrypt(word)   #place to implement the  passwords
        if result == 1:
            print('Success! The password is: ' + word)
            break

        elif result == 0:
            tried += 1
            print('Passwords tried: ' + str(tried))
            continue

"""
1) a) file location of pdf
   b) read the pdf file
2) if file has no pass open it
3) if the file has pass start brute force
   a) word file --> read-line--> split each word (column the words)
   b) try each word by using for loops and len 
   c) data to show = count,word used and password
   d) place to implement the pass
   e) if result =1 password found and break or result=2 and continue to find
   
"""