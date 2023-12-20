
SHARK ATTACK DATA FINAL PROJECT


What the program does
-------------------------------------------------------------------------------------------------------------------------------------------------------

0. This program demonstrates a simple code that webscrapes a csv file that was downloaded from the website 
"Keggle" and was placed into the "Final Project" folder. This file contains data about shark attacks specific information that was 
recorded about the attack as well.Some additional packages the user will install will be pandas. At the command line,if they have python 
they can type "pip install pandas" and that should allow them to be able to use that package for this program. 

1. The first thing the program does is it imports the os, pandas, and the re libraries.
Pandas was used to read the file and show a dataframe for the csv file, the os is used 
for accessing files and such and the re library is used for the regular expressions.

2. Next, the program gets the current working directory path and assigns that to a variable.
Then in my program I checked to see if the "shark.attack_dataset" folder existed and it
came back as True. 

3. Then the program is basically saying that if the folder exists, then it will list the contents
inside the "shark.attack_dataset" folder.

4. After this, in order to complete my requirements from the checklist, I created a dictionary and 
used regular expressions to filter out what file I need through a pattern.

5. Then, the program creates a completed path to get to the shark attack csv file by joining the path to the folder and to the file and if it matches 
the csv pattern from the regular expression, then the program will save that path to the files in the dictionary I had created.

6. The program then reads the csv file with pandas in order to create a dataframe.

7. Lastly, the program will print out a title stating that this is the dataframe from the shark attack csv file and it also prints out the dataframe.







How to use the program
-----------------------------------------------------------------------------------------------------------------------------------------------------------
1. download the project from GitHub repo using this on your terminal:
git clone <repository_url>

2. Make sure you have a close up-to-date version to Python 3 (you can check by typing "python --version" on your terminal) and have read the insturctions above on 
"what the program does" for installing pandas uner bullet 0.

3. type "cd" and the path to the project directory on your terminal. For example:
cd /Users/ally/Desktop/INST126/Final_project/INST126/Final_project/shark.attack_dataset. If you have mac and don't know the path
then go to finder on your mac and "control click" on the desired file and click on "get info".

4. type python shark_final_project.py in your terminal to execute the program




