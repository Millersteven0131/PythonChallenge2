import os
import csv
total_votes=0
candidate_list=[]
vote_count=0
vote_dataset={}
winning_count=0
csvpath=os.path.join('PyPoll','Resources','election_data.csv')
vote_dataset_percentage = {}
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes+= 1
        candidates_name=(row[2])
        if candidates_name not in candidate_list:
            candidate_list.append(candidates_name)
            vote_dataset[candidates_name]=0
        vote_count=int(row[0])
        vote_dataset[candidates_name]=vote_dataset[candidates_name]+1
    total_num_of_votes = sum(list(vote_dataset.values()))
    for candidate_name, winning_val in vote_dataset.items():
        if winning_val>winning_count:
            winning_count=winning_val
            winning_candidate=candidate_name
        vote_percentage = winning_val/total_num_of_votes
        vote_dataset_percentage[candidate_name] = float(str(vote_percentage)[:5])*100

print(total_votes)
print(vote_dataset)
print('Winning Candidate:', winning_candidate)
print('Vote Percentage for each candidiate', vote_dataset_percentage)


candidates = []
for key, value in vote_dataset.items():
    c_dict = {
        "name": key,
        "votes":value
    }
    candidates.append(c_dict)

candidates2 = []
for key, value in vote_dataset_percentage.items():
   c_dict = {
        "name": key,
        "pct":value
    }
   candidates2.append(c_dict)


txt_file_path = os.path.join('PyPoll','PyPollAnalysis.txt')
with open(txt_file_path, 'w') as f:
    f.write('Election Results\n')
    f.write(f'Total Votes:{total_votes}\n')
  
    
    for i in range(len(candidates)):
        f.write(f'{candidates[i]["name"]}: {candidates2[i]["pct"]}% ({candidates[i]["votes"]})\n')


    f.write(f'Winner:{winning_candidate}\n')
    f.close()