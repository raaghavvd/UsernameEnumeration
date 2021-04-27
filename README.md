# UsernameEnumeration
Project for C5770
**Instructions**:
The following files exist inside the docker:
check.py     enumerator.py     emailID.txt     usernames.txt     newlinks.txt     error_msgs.txt     msg2.txt       

check.py – A simple script to check if TOR is working i.e., IP addresses are changing.
enumerator.py – The main username enumeration tool
emailID.txt – Enter the email Ids to be tested in this file
usernames.txt – Enter the usernames to be tested in this file
newlinks.txt – Enter the links to be tested in this file
error_msgs.txt – Enter the error messages related to the runProgram function (-P option)
msg2.txt - Enter the error messages related to the accountNotPresent function (-NP option)

This tool currently supports 50 websites. The complete website list is listed in the main_database excel file. 
1.	Choose a website to perform the enumeration from the excel file.
2.	Copy the corresponding link from the excel file to newlinks.txt file
3.	Enter the email ids or usernames to be tested in emailID.txt or usernames.txt files, respectively.
4.	Copy the Error Messages from the excel file to error_msgs.txt or msg2.txt files, respectively
5.	Run the tool 

	Some sites do not work properly with TOR. Refer to Excel file to see which sites do not work with TOR
	Sites like abc.com, abcnews.com, espn.com, marvel.com, and disney.com are owned by the Walt Disney Company and hence work under the same user account. Hence, checking for usernames present on parent company, disneyplus.com will be sufficient and checking the other sites individually is not necessary. Similarly, enumerating for theverge.com covers Sbnation.com, polygon.com, Eater.com, and thevox.com
	Most of the sites work with -P flag and error_msgs.txt. The -NP flag and msg2.txt files are rarely used. This tool will be updated continuously, and new sites will be added. 




Installation:
# Clone the UsernameEnumeration Repository:
$ git clone https://github.com/raaghavvd/UsernameEnumeration.git 

#Go to the UsernameEnumeration directory:
$ cd UsernameEnumeration

# Run the script.sh file to build the docker image and run this as a container :
$ ./script.sh

# Start TOR by using the following command:
$ tor &
Press the ENTER key when it says “Bootstrapped 100% (done)”

# Run the enumerator tool:
$ python3 enumerator.py -P -email tor


Usage:
$ python3 enumerator.py -P[-NP] -email[-username] [tor]

-P or -NP     P denotes to check if the error message indicates the username/email to exist
                     NP denotes to check if the error message indicates the current username doesn’t exist

-email or -username         email means website takes email id as input
                                             username means website takes usernames as input

tor – to run the tool with tor – changes IP addresses [This parameter is optional]


Examples:
python3 enumerator.py -P -email tor
python3 enumerator.py -P -username
python3 enumerator.py -NP -email










