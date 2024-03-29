## Overview



This repository contains information and examples on the use of processes and signals in bash.

## Processes



In bash, a process is a program or script that is currently running. Each process is assigned a unique process ID (PID) for identification.



To view all running processes, use the command `ps` or `top`. To view information about a specific process, use the command `ps -p PID` or `top -p PID`.



To start a new process, use the command `command &`, where `command` is the program or script you wish to run. This will run the command in the background, allowing you to continue using the terminal while the process runs.



To stop a running process, use the command `kill PID`, where `PID` is the process ID of the process you wish to stop.




## Additional Resources



- [Bash Process Management](https://ryanstutorials.net/bash-scripting-tutorial/bash-process-management.php)

- [Linux Signals](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_12_02.html)

- [kill command man page](http://manpages.ubuntu.com/manpages/xenial/man1/kill.1.html)


