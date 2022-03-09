## UNIX administration

* UNIX - proprietary system
* GNU/Linux - open-source UNIX-like system 

## Why UNIX?    

* costs, security, flexibility, re, efficiency
* Personalization:
  * Desktop environments - GNOME, xfce, ...
  * Window Manager - i3 (tiling), kwin (stacking), dwm (dynamic), ...
* Virtual Machine: VirtualBox (Oracle), KVM, ...
## CLI 

**GUI make easy tasks easy, while CLI make difficult tasks possible**

### Moving around : 
* relative paths/absolute paths    
	```/home/user/.../```    
	```. ./ or ../```
* hidden files ```.```
### Options and man: 
* ```ls``` - list content
* options, ```man``` (systemwide) or ```help``` (shell)
* ```file``` - get file type
* ```apropos``` - look for pattern in help texts
* ```grep``` - print rows containing pattern (super useful with ```pipe |``` operator)
### Read/Write files
* ```>```, ```>>``` operators for create/overwrite (append) in files
* ```less``` - read text files
* ```vi``` & ```nano``` text editors
### Finding stuff:	
* ```which``` - locate executable
* ```find . -name '...'``` find a file by name, recursively
### Wildcards:	
* ```*``` Matches any characters
* ```?``` Matches any single character
* ```[characters]``` Matches any character that is a member of the 
  set characters
* ```{...}``` Arrays, see ```{a..z}```, ```{1..9}```
* ```mkdir 2021{01..12}{01..30}```
* ```*[[:lower:]123]``` Any file ending with a lowercase letter or
  the numerals “1”, “2”, or “3”
* ```[![:digit:]]*``` Any file not beginning with a numeral :
### Get efficient: 	

* ```alias``` - personalize commands
* ```clear``` - clear terminal, same as Ctrl+l
* ```history``` - see terminal history (```!123``` run 123th command)
* `Ctrl + r`    -    search through previous commands 

### Permissions:	
* owner, group, external
* ```sudo ...``` superuser do
* ```su <user>``` switch user
* ```chown <user> <file>``` change owner
* ```chgrp <group> <file>``` change group
* ```chmod``` change permissions (octal numbers) 
	* execute needed to run files and enter folder 

### Install:		
* Package managers (snap, apt, conda, pip,...)
* Package dependencies
* ```apt-get install ...``` install package (install dependencies as well) 
* ```dpkg --install <file.deb>``` install package file (not installing dependencies)
### Kill something:
* Stop process Ctrl + C
* ```kill <PID>``` - stop process with PID
* ```xkill``` - stop by click
* `killall` ... - stop all instances of ...
* ```top``` or ```htop``` - show processes
* ```reboot``` - restart system
* ```shutdown x``` - shutdown system in x minutes
### Keyboard: 
* ```setxkbmap gb,de -grp:win_switch``` Use keyboard layouts British and German, switch by pressing WIN key        

