"""
File: backups.py
Author: Jonah Miller

This script backups all of my relevant files and folders to a specific
place. 

Each backup is placed in a folder named by the backup date. You can
tell the script how many of these backups you want to keep. Default is 2.
"""

# Import statements
#--------------------------------------------------------------------------
import os                    # For file operations.
from datetime import date    # The day the backup was made
from subprocess import call  # For running shell commands
#--------------------------------------------------------------------------

# Constant definitions
#--------------------------------------------------------------------------
HOME = '/home/jonah/' # Home directory. For convenience
TODAY = date.today() # The date the backup was made

# The home directory for the backup file tree
TREEHOME = '/home/jonah/Dropbox/config_file_backup'

# The number of backups the script keeps
N_BACKUPS = 3;

# Files to back up.  FORMAT: The data structure is a dictionary and
# list structure. The keys of the dictionary are the directories, and
# each item a key points to is a list of files in the given key's
# directory to copy. 
FILES = {HOME:['.bashrc', '.bash_profile','.emacs','.mapleinit','.profile',
               '.vimrc','.Xauthority','.Xdefaults','.xinitrc','.xmobarrc'],
         HOME+'.emacs.d/':[],
         HOME+'elisp/':[],
         HOME+'MapleStuff/':[],
         HOME+'.mednafen/':['mednafen.cfg'],
         HOME+'.xmonad/':['xmonad.hs'],
         '/etc/':['dhcpcd.conf', 'dnsmasq.conf','fstab','ntp.conf',
                  'pacman.conf', 'profile','rc.conf','rysncd.conf',
                  'logrotate.conf','slim.conf','sysctl.conf','vimrc'],
         '/etc/acpi/':[],
         '/etc/iptables/':[],
         '/etc/profile.d/':['maple16.sh','myscripts.sh'],
         '/etc/laptop-mode/':['laptop-mode.conf','cpufreq.conf'],
         '/etc/laptop-mode/conf.d/':[]}
#--------------------------------------------------------------------------


# Function definitions
#--------------------------------------------------------------------------
def make_directory_tree(directory_list):
#--------------------------------------------------------------------------


#--------------------------------------------------------------------------
def main():
    os.chdir(TREEHOME) # Changes directory to the home tree
    
#--------------------------------------------------------------------------
