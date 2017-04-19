
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
#Creating a function to verify user account and password
def verifyaccounts(name):
#note sure if I really need this password = None part.
    checkname = False
    userhasbeenverified = False
#making sure the name is still capitalized just incase.
    name = name.capitalize()
#Loading the accounts into an array for later referencing
    checkaccounts = open('accounts.txt', 'r')
    loadedcheckaccounts = checkaccounts.read().split('\n')
    checkaccounts.close()
    print  "These are used for a later variable that works.\n"
    print loadedcheckaccounts
    loadednames = loadedcheckaccounts
    loadednames = [i.split(':')[0] for i in loadednames]
    print "I need these seperated with the name and then the PW after the :.\n"
    print loadednames
#I need to search for user name in loadedcheckaccounts but the each list is like Jaiven:passwordtest. I just need it to match the part before the : with the name given to be true and move on.
#wildcard * doesn't seem to work.
    for user in loadednames:
        if user == name:
            checkname = True
            break
    if checkname == False:
        print 'Sorry, there is no character by that name or the password is incorrect. Please try again.'
        name = raw_input("Please enter a name or type 'create' to create a new character.\n")
        if name.lower() == 'create':
            getnewuser()
        else:
            verifyaccounts(name)
    if checkname == True:
        password = raw_input('Welcome back to Jusam Mud ' + name + '. ' + 'Please type your password to log into the mud.\n')
#loading name, :, and password into a variable to later check against the array name and password.
    verifieduser = name + ':' + password
#This is where we check the name and password variable to the name and password array.
    for checkverifieduser in loadedcheckaccounts:
         if verifieduser == checkverifieduser:
             print 'we got your id!'
             userhasbeenverified = True
#If they don't match try again.
    if userhasbeenverified == False:
        print 'Sorry, there is no character by that name or the password is incorrect. Please try again.'
        name = raw_input("Please enter a name or type 'create' to create a new character.\n")
        if name.lower() == 'create':
            getnewuser()
        else:
            verifyaccounts(name)

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
#attempts to write password after username and now works due to closing it outside the orig if statement.
    if passwordComplete == True:
        settingpassword = open('accounts.txt','r+')
        for line in settingpassword:
            if tempname in line:
                settingpassword.write(setuserpassword + '\n')
                passwordStored = True
    if passwordStored == True:
                settingpassword.close()

#Character login where you get the option to enter an already created character or type create to run the function getnewuser
name = raw_input("Please enter a name or type 'create' to create a new character.\n")
if name.lower() == 'create':
    getnewuser()
else:
    verifyaccounts(name)
