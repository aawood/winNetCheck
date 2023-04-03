# winNetCheck
A python routine for checking if other windows PCs on the network are offline, or if your external IP has changed.

I created this as I kept finding that my home-based web server was offline, either because a Windows update had restarted it, or my ISP had changed my external IP address. As such, this routine does two things; first, it checks a set list of other servers to see if any are offline, and second, it checks your current external IP address to see if it matches the one expected. It uses Toast notifications to alert to any issues, or to confirm if no issues were found.


# Setup
Setup requires editing the two text files:

externalIP.txt
This should have one line, which is your expected external IPV4 address. If that ever changes, you should update this file to match.

servers.txt
This is a list of other Windows PCs on your network to check, by internal IPV4 address. You should have one server IP per line.

You can adjust the filenames this looks for in the WinNetCheck.py file. If you want, you can also change "active" to False, at which point WinNetCheck will print it's messages rather than sending them as Toast Notifications.
