
#The function to handle adding new users to accounts.txt which repeats if name is under 2 characters and checks to see if all alpha with no spaces.
def getnewuser():
#this has to be in the function and not outside it. I had a dream about this bug and fixed it in my dream. So when it is outside the function it will
#add the users when the server starts but won't load more users into registereduers when a new user is created and thus create duplicates if the same name is entered after the read.
    useraccount = open('accounts.txt', 'r')
    registeredusers = useraccount.read().split('\n')
    useraccount.close()
    #namePassed used to prompt for new password if the new player named passed and finished transferring into accounts.txt file.
    namePassed = False
    nameExists = False
    tempname = raw_input('Please name your new character.\n')
    tempname = tempname.capitalize()
    #iterate through each element and check to see if the user already exists
    for user in registeredusers:
        if user == tempname + ':':
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
                #adds the : between name and password for later file searching to verify user accounts.
                useraccount.write(tempname + ":")
                useraccount.close()
                namePassed = True
                print "Welcome to Jusam Mud " + tempname
            else:
                #the name exists, so let our user know
                print "Name exists. Please try another name."
                namePassed = False
                getnewuser()
        else:
            print "The name may only contain characters."
            namePassed = False
            getnewuser()
    else:
        print "Name must be greater then two characters, less then 20 characters."
        namePassed = False
        getnewuser()
    if namePassed == True:
        getnewpassword(tempname)
#creating the function to get new password upon character creation. Passed tempname to getnewpassword
def getnewpassword(tempname):
    passwordPassed = False
    passwordComplete = False
    newpassword = raw_input('Please enter a password for ' + tempname + '.' + ' Please note that you cannot use spaces when creating a password.\n')
#makes sure there are no spaces in password.
    if ' ' in newpassword:
        print 'Sorry but your password has a space in it. Remember, you cannot have spaces in your password. Try again.\n'
        getnewpassword(tempname)
        passwordPassed = False
    else:
        print "Password accepted.\n"
        passwordPassed = True
#asks for password input again and checks to see if both password variables match.
    if passwordPassed == True:
        retypedpassword = raw_input('Please enter your password again.\n')
        if newpassword == retypedpassword:
            print "User account created."
            setuserpassword = retypedpassword
            passwordComplete = True
        else:
            print "passwords don't match. Please try again"
            getnewpassword(tempname)
#attempts to write password after username and :. works but gives an IO error.
    if passwordComplete == True:
        settingpassword = open('accounts.txt','r+')
        for line in settingpassword:
            if tempname in line:
                settingpassword.write(setuserpassword + '\n')
                settingpassword.close()

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

#if name found move to request password
#load all text after name[:] search to variable password
#prompt for password
#if password = variable password log into game
#if not, print wrong password, try again, disc
