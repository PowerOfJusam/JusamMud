
#The function to handle adding new users to accounts.txt which repeats if name is under 2 characters and checks to see if all alpha with no spaces.
def getnewuser():
#this has to be in the function and not outside it. I had a dream about this bug and fixed it in my dream. So when it is outside the function it will
#add the users when the server starts but won't load more users into registereduers when a new user is created and thus create duplicates if the same name is entered after the read.
    useraccount = open('accounts.txt', 'r')
    registeredusers = useraccount.read().split('\n')
    useraccount.close()

    nameExists = False
    tempname = raw_input('Please name your new character.\n')
    tempname = tempname.capitalize()
    #iterate through each element and check to see if the user already exists
    for user in registeredusers:
        if user == tempname:
            nameExists = True
            break
    #if the length is between 2 and 20
    if len(tempname) > 2 and len(tempname) < 20:
        #if the name contains only characters
        if tempname.isalpha():
            #if the name does not exist
            if nameExists == False:
                #searches for name and if name isn't there writes name to file on next line
                useraccount = open('accounts.txt','a')
                useraccount.write(tempname + '\n')
                useraccount.close()
            else:
                #the name exists, so let our user know
                print "Name exists. Please try another name."
                getnewuser()
        else:
            print "The name may only contain characters."
            getnewuser()
    else:
        print "Name must be greater then two characters, less then 20 characters."
        getnewuser()

#Character login where you get the option to enter an already created character or type create to run the function getnewuser
name = raw_input("Please enter a name or type 'create' to create a new character\n")
if name.lower() == 'create':
    getnewuser()
#loads name file.

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
#if not, print wrong password, try again, disc
