#Login idea
name = raw_input("Please enter a name or type 'create' to create a new character\n")
if name == 'create' or 'Create':
    tempname = raw_input('Ok, please name your new character\n')
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
