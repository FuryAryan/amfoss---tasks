password for level 1 was found by first entering ssh with port number and adress in terminal and entering password as bandit0 and after going in directory bandit0 we click ls to look inside and then display the file with cat command.


password for level 2 was found by chanching the directory to bandit 1 and entering password that was found for level and with using ls we got the file name as - and using cat we look at the password.


password for level 3 was stored in a file name spaces in this name which had spaces in the name of the file so we had to use "\" this between the spaces between the file name so after using cat we get our password.

password for level 4 was stored in a directory named as inhere when we use ls it is empty so we have to use ls -la to list all and the there is a file as .hidden so we have to enter cat .hidden.


password for level 5 was stored in inhere directory but inhere directory contained 10 files which had only one human readable file so i had to find the file conating ascii text which is human readable text and it was -file07 which had password for level 5.


password for level 6 was stored in inhere directory which had many directories inside so we have to find the 1033 byte file which was human readable that was .file2 in maybehere07 which contained the password for level 6.


password for level 7 was in inhere directory which was empty so when we use find and specify the details of file giving the size and user and group name we get many files and every file shows permission denied except one file so i copied its path and used cat command for that then it gave the password.


password for level 8 was in data.txt which has many passwords inside but with using grep and as per hint it is in the line of millionth so using grep command with millionth we get the password with it.
u

password for level 9 was in the file data.txt which had many passwords inside it but the password for next level was unique password so i had to sort the file data.txt and use command "sort data.txt | uniq -u" to get the password.
