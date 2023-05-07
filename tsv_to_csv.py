import re
# Convert tsv file to csv file
with open("Data/genie_public_clinical_data_v13.tsv", "r") as tsv_file:
    with open("Data/genie_public_clinical_data_v13.csv", "w") as csv_file:
        for line in tsv_file:
            file_content = re.sub("\t", ",", line)
            csv_file.write(file_content)

print("Success")