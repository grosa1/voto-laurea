import sys

exams_data = sys.argv[1]

tot_exams = 0
tot_credits = 0
na_credits = 0

print('ESAME | CREDITI | VOTO:\n')
with open(exams_data, 'r') as f:
    index = 0
    for row in f:
        row = row.split(',')
        if 'NA' in row[2]:
            na_credits += int(row[1])
            continue

        index += 1
        print(str(index) + '. ' + row[0] + ' | ' + row[1] + ' | ' + row[2])
        
        ### row[2]=vote, row[1]=credits
        tot_exams += (int(row[2]) * int(row[1]))
        tot_credits += int(row[1])

vote_30 = round((tot_exams/tot_credits),2)
vote_110 = (vote_30 * 11) / 3

print('#############################################\n')
print('media: ' + str(round(vote_30,2)) + '\n')
print('base di laurea: ' + str(round(vote_110,2)))
    


