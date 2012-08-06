#!/usr/bin/env python

import os
import sys
import time
import getpass

## Get users home directory
HOME = os.getenv('HOME')

## Get local hostname
HOST = os.uname()[1] 

## Get user name
USER = getpass.getuser() 

## Function: configure ~/.progrc to include the path to the progress file.
def Setup():
    
    try:
        os.system("rm $HOME/.progrc")
    except os.error:
        sys.stderr.write("* Creating a new config file '~/.progrc'.")

    PATH = raw_input("* Where shall I record your progress (PATH + FILENAME)?: ")
    os.system("echo 'PATH\t" + PATH + "' > $HOME/.progrc") 

    if not os.path.exists(PATH):
        os.system("touch " + PATH)
        print "* Created " + PATH 

    BACKUPS = raw_input("* Where shall I backup your progress file (PATH with trailing '/')?: ")
    os.system("echo 'BACKUPS\t" + BACKUPS + "' >> $HOME/.progrc")

    if not os.path.exists(BACKUPS):
        os.system("mkdir -p " + BACKUPS)
        print "* Created " + BACKUPS

    print "* Setup is complete"

## Function: find progress file
def PathFinder(choice):

    # Read contents of ~/.progrc.
    lines = tuple(open(HOME + '/.progrc', 'r'))

    # Find line beginning with 'PATH'
    for line in lines:
        if line.startswith(choice):

            # Extract second tab-delimited item
            return line.split('\t')[1].rstrip('\n')

## Function: append a line to the progress file.
def Update():
    
    # Find the progress file.
    ProgressFile = PathFinder('PATH')
    
    # Get time stamp
    TimeStamp = time.strftime("%a %d %b %Y %H:%M:%S +0000", time.localtime()) 
    
    # Prompt user for a comment.
    comment = raw_input('Comment: ') 

    # Write time stmap and comment to the progress file.
    os.system("echo '[" + str(TimeStamp) + ", " + USER + "@" + str(HOST) + "]\t" + str(comment) + "' >> " + ProgressFile)

## Function: display the contents of the progress file.
def Review():
    
    # Find the progress file.
    ProgressFile = PathFinder('PATH')

    # Display contents to screen
    os.system("cat -b " + ProgressFile)

## Function: backup the progress file.
def Backup():
    
    # Find the progress file.
    ProgressFile = PathFinder('PATH')
    
    # Find the backup path :w
    BackupPath = PathFinder('BACKUPS')

    TimeStamp = time.strftime("-%d%b%Y-%H:%M:%S", time.localtime()) 

    BackupFile = BackupPath + "backup" + TimeStamp

    # Write the backup file
    os.system("cp " + ProgressFile + " " + BackupFile)


## Dunction: delete last [#] updates from progress file
def Delete(n=1):

    # Backup current progress file
    Backup()

    # Find the progress file.
    ProgressFile = PathFinder('PATH')
    temp = ProgressFile + ".tmp"

    # Delete last n entries.
    os.system("head -n -" + str(n) + " " + ProgressFile + " > " + temp)
    os.system("mv -f " + temp + " " + ProgressFile)

## Function: display the help/usage screen.
def Help():
    
    print "\nHelp: prog.py [OPTIONS]\n"
    print "  -s  --setup\tSetup your progress file."
    print "  -u  --update\tUpdate your progress progress."
    print "  -r  --review\tReview your progress."
    print "  -b  --backup\tBackup your progress file."
    print "  -d [#]  --delete [#]\t Delete last [#] update(s)."
    print "  -h  --help\tDisplay this screen.\n"
    sys.exit(0)

## Function: parse the user's command-line arguments
def ParseArgs(args):
    
    i = 1 

    while (i < len(args)):
        a = args[i]

        if a == "--setup" or a == "-s":
            Setup()
            i += 1

        elif a == "--update" or a == "-u":
            Update()
            i += 1

        elif a == "--review" or a== "-r":
            Review()
            i += 1

        elif a == "--backup" or a == "-b": 
            Backup()
            i += 1

        elif a == "--delete" or a == "-d":
            # If at end of 'args' then 'n' not specified i.e. n=1.
            if (i+1) == len(args):
                Delete(1)
            
            # If NOT at end of args AND next parameter is a number
            # then 'n' is specified.
            elif args[i+1].startswith('-') == False:
                Delete(args[i+1])
 
            # If NOT at end of args AND next parameter is NOT a number
            # then 'n' not specified i.e. n=1.
            else:
                Delete(1)

            i += 2

        elif a == "--help" or a == "-h":
            Help()
            i += 1

        else:
            print "Unrecognised command '" + a + "'"
            print "Try --help, -h for help"
            sys.exit(1)

## Function: main control loop
def Execute():
    
    ParseArgs(sys.argv)
    
## Start the main control loop
Execute()
