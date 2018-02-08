# raspBatteryServer
An FTP server that runs on a raspberry pi and a client that goes with it.

You will have to instal pyftpdlib if you havent't alredy.

You are going to have to edit a slightly bit the files. Edit the FTPServer where i have written to edit it. Put there the directory of the folder that you want to . Then, you will have to edit the IP adress of the pi in the frontendClient. This souldn't be edited normally, because my pi creates its own wifi, and it always is the IP adress: 192.168.88.2.
