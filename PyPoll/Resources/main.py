#Libarary allows to excess path objects across operating systems
import os

#Libarary allows to read and write to the csv files
import csv

#Building the path to the csv file and storing it into the object
csvpath = os.path.join("..","Resources","election_data.csv")

#Opening the csvfile for reading
with open(csvpath) as csvfile:

    #Returns a reader object which will iterate over lines in given csvfile
    csvreader = csv.reader(csvfile, delimiter=',')

    #To skip the headers stored in the csv file and stored them in the variable
    heading = next(csvreader, None) 
    
    #To store total votes
    total_votes = 0

    #To store the all the votes according to BallotID (Column A)
    ballot_list = []

    #Unique Candidate names values from the Candidate (Column C)
    election_candidate_list = []

    #All the Candidate names values from the Candidate (Column C)
    vote_cast_list = []
   
    #Counter variable to check Candidate match
    candidate_vote_count = 0

    # Dictionary to store all the candidates names, number of votes for each of them and having percentage of votes each candidate 
    candidate_votes_dict = {}
    
    #Checking the result where the candidate does not match
    checker = False

    #Looping variables
    i = 0
    j = 0

    #To store name of unique candidate
    election_candidate_name = ""

    #To calculate and store value of percentage of votes each unique candidate have
    percentage_of_votes = 0
    
    #This part of the code is to check the Total number of votes accoding to the Column A (Ballot ID) of the csv file 
    #vote_cast_list contains all the candidates who stood for an election and got votes having multiple records for single candidate
    #election_candidate_list contains unique candidates who stood for an election and got votes
    for csvrow in csvreader:
        ballot_list.append(csvrow[1])
        total_votes = len(ballot_list)
        vote_cast_list.append(csvrow[2].strip())
        if csvrow[2] not in election_candidate_list:
            election_candidate_list.append(csvrow[2].strip())
    

    #This part of code is checking if there are n numbers of candidates who stood in the election having any name, this will return the vote count and percentage of votes according to the votes cast
    # i is the looing variable used for the candidates stood in the election example  "Charles Casper Stockham" "Diana DeGette" "Raymon Anthony Doane" etc 
    # j is loooping variable used for every vote "Charles Casper Stockham" "Diana DeGette" "Raymon Anthony Doane" etc got 
    # "candidate_votes_dict", Creating this dictionary with having all the candidates names, number of votes for each of them and having percentage of votes each candidate 
    # "candidate_votes_dict" contains (Candidates Names) as Key and (Number of Votes for each of them and having Percentage of Votes each candidate) as List of values associated with the key
    for i in range(0, int(len(election_candidate_list))):
        for j in range(0,int(len(vote_cast_list))): 
            if election_candidate_list[i] == vote_cast_list[j]:
                election_candidate_name = election_candidate_list[i]
                candidate_vote_count = candidate_vote_count + 1
            else:
                checker = True
        j = 0
        i= i + 1
        if checker == True:
            percentage_of_votes = round(float(100 * candidate_vote_count/total_votes),3)
            candidate_votes_dict[election_candidate_name] = []
            candidate_votes_dict[election_candidate_name].append([percentage_of_votes,candidate_vote_count])
            candidate_vote_count = 0
            election_candidate_name = ""
            percentage_of_votes = 0
            
    
   #Calculating and storing the election winner as per the values in the candidate_votes_dict
    election_winner = max(candidate_votes_dict, key=candidate_votes_dict.get)

#Created a list and assign all the values to print on the console and write into the file election_results.txt      
print_analysis = []
    
print_analysis.append("Election Results")
print_analysis.append("--------------------------------------------")
print_analysis.append(f"Total Votes: {total_votes}")
print_analysis.append("--------------------------------------------")
#Fetching the key value pair for each candidate to print
for key in candidate_votes_dict:
         for value in candidate_votes_dict[key]:
            print_analysis.append(f"{key}: {value[0]}%   ({value[1]})")
print_analysis.append("--------------------------------------------")
print_analysis.append(f"Winner: {election_winner}")
print_analysis.append("--------------------------------------------")

#To create Analysis folder/directory for the text file
analysis_path = os.path.join("..","Analysis")

#To create or overwrite file inside the Analysis folder/directory
election_results_txt_path = os.path.join("..","Analysis","election_results.txt")

#Try to execute this part of code and throw an exception at run-time "The file or directory does not exist"
try:
    #Checking whether the Analysis folder/directory exists 
    if not os.path.exists(analysis_path):
        
        #If not exist create the Analysis folder/directory first 
        os.makedir(analysis_path)
        
        #Create or overwrite the file election_results.txt
        with open(election_results_txt_path, 'w') as election_file:
            for to_print in print_analysis:

                #To write all the statements in the print_analysis list to the file election_results.txt
                election_file.write(to_print + '\n')
                
                #To print the output on the Terminal
                print(to_print)
    else:
        #Create or overwrite the file election_results.txt
        with open(election_results_txt_path, 'w') as election_file:
            for to_print in print_analysis:
                
                #To write all the statements in the print_analysis list to the file election_results.txt
                election_file.write(to_print + '\n')
                
                #To print the output on the Terminal
                print(to_print)
    
except:
   print("The file or directory does not exist")