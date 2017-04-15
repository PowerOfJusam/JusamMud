
useraccount = open('accounts.txt', 'r+')
registeredusers = useraccount.read()
print registeredusers

#The function to handle adding new users to accounts.txt which repeats if name is under 2 characters and checks to see if all alpha with no spaces.
def getnewuser():
    tempname = raw_input('Please name your new character.\n')
    tempname.capitalize()
    if len(tempname) > 2 and len(tempname) < 20 and tempname.isalpha() not in registeredusers:
        useraccount.write(tempname)
    else:
        print "Name must be greater then two characters, less then 20 characters, contain no numbers, symbols or spaces.\n"
        tempname = None
        getnewuser()

#Character login where you get the option to enter an already created character or type create to run the function getnewuser
name = raw_input("Please enter a name or type 'create' to create a new character\n")
if name.lower() == 'create':
    getnewuser()

#loads name file.
#searches for name and if name isn't there writes name to file on next line
#prompts for a password
#writes password to file after name
#asks for password again
#looks up name after tempname [search for name in file followed by:] for password after name
#if password = after tempname pw then creates character

#login with a character already created
#if name isn't create search file for name
#if name found move to request password
#load all text after name[:] search to variable password
#prompt for password
#if password = variable password log into game
#if not, print wrong password, try again, disconnect.
