# reads Links.csv and produces a csv with unique taxon names.
# The input and output CSVs  are used for Flourish network graph.
import csv

with open("input_data/Links.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    all_words = []
    for row in csv_reader:

        all_words.append(row[0])
        all_words.append(row[1])

unique_words = set(all_words)

with open('output_data/unique_points.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['source', 'weight'])

    for word in unique_words:
        writer.writerow([word, 1])
