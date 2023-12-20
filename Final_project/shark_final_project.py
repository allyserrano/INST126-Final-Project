
#import pandas for dataframe for the csv file and os to access/manipulate files and re for the regular expressions
import os
import pandas as pd
import re

# #get the current working directory path
directory_path = os.getcwd()
print(directory_path)

folder_path = "INST126/Final_project/shark.attack_dataset/" #path to specific folder for data
dataset_folder_path = os.path.join(directory_path, folder_path) #joins path of cwd and path to the folder

print("Dataset folder path:", dataset_folder_path) # checking if this is printing what it should be with print statements
print("Welcome! Below you will see the contents under this folder") #welcomes user


seen_from_wd = [] #makes empty list for files

if os.path.exists(dataset_folder_path): #if this exists then...
    seen_from_wd = os.listdir(dataset_folder_path)#the program will save the listed contents of the "shark.attack_dataset" folder where the csv file is located
    print(f"Contents of '{dataset_folder_path}': \n\t{seen_from_wd}")


    files_dictionary = {} #creating a dictionary for the files in the dataset folder
    file_pattern = re.compile(r'.*\.csv$')#regular expression to match what files in folder end with "csv"

    for file_name in seen_from_wd: #iterating each file in the list from seen_from_wd
        file_path = os.path.join(dataset_folder_path, file_name) #joins path to file
        print(f"Checking file: {file_path}") #print statement, mostly used to check on the code while I was working
        if file_pattern.match(file_name): #if the file name matches with the csv pattern then...
            files_dictionary[file_name] = file_path #store the path in the dictionary
            try:
                pandas_dataframe = pd.read_csv(file_path) #reads the csv file
                print(f"\nDataFrame for '{file_name}':\n{pandas_dataframe}") #print dataframe if successful
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
            except pd.errors.EmptyDataError: #in case the csv file is empty and there it can't read or print the dataframe
                print(f"File '{file_path}' is empty or not a valid CSV file.")
else:
    print(f"Folder '{dataset_folder_path}' does not exist.")











 















