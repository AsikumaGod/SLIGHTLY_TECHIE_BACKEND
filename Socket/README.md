<h1 style="text-align: center;">PROJECT EXPLANATION</h1>
This project focuses on Python Socket Programming

This project have a server script that binds a port and responds to connections (unlimited amount of concurrent connections)

The server receives a string in the connection as clear text,
There is a configuration file which has the path for a file. The path of the file should be is indicated as “beigefilepath”. Assume there are other configurations in the configuration path that has nothing to do with your script. Eg: beigefilepath=”/var/lib/cohort1.txt”
The script opens the config file and search for an exact match of a string sent by the client script.

The strings are separated by a new line, hence partial match is no match, only exact matches are considered as a match. The script responds with “STRING FOUND”.
If the string is not found, the script responds with “STRING NOT FOUND”.
Exception handling is considered in all cases possible.

Script is clearly commented and adhere to the PEP8 and PEP20
Make your code PEP8 and PEP20 compliant.
The script is be able to run on Linux when called on the command line

The string received is Stripped off any additional characters

<h1 style="text-align:center;">How to run script</h1>
<ol>
<li>Open two separate terminals</li>
<li>Run the server file first with the command "python3 filename.py"</li>
<li>Repeat step 2 with the client script</li>
</ol>
