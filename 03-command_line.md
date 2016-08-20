# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

cp copies a file
mv moves a file
cd changes directories
pwd shows current full path
ls lists the contents of the current directory
mkdir makes a new directory
rmdir removes a directory (empty)
| takes the output of the first command and inputs it to the second
rm removes a file
* is a wildcard character and will match all (if you want to see all .txt files ls *.txt will list them)
---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls lists all files (not hidden)
-a includes hidden files
-l is the long format
adding the h flag makes the file sizes human-readable
so lh will be long format, human readable
and lah will be long format, all files, human readable
-t organizes the files by modification time
-Glp will list long format, hide the group information and append a file type flag to the list

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:
-u displays by access time which can be useful for finding something recent
-R (recursive?) displays the ls information for subdirectories as well
-m displays the options as a compact, comma-separated list
-1 lists one file per line
-S sorts by file size



---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.
xargs breaks a list of arguments into individual commands, executes these commands individually. Additionally it appears that xargs can be used for parallelization as well which is a function I was not previously familiar with! Going to have to check that out as well.  
ex: 
find /home/user/folder/ -print | xargs rm 
will remove the files in the path even if just running rm * in the given directory would have failed due to there being too many arguments.

