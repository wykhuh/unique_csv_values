import csv
import argparse
import os


def setup_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,
                    help="name of input CSV that need to be processed")
    ap.add_argument("-o", "--output", required=True,
                    help="name of output CSV that has unique values")

    return vars(ap.parse_args())


def get_unique_values_for(path):
    all_values = []

    with open(path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if row:
                all_values.append(row[0])

    return set(all_values)


def output_file_exists(path):
    return os.path.exists(path)


def create_output_file(path):
    open(path, "w+")


def append_existing_file(path, data):
    with open(path, 'a') as f:
        csv_writer = csv.writer(f)
        for datum in data:
            csv_writer.writerow([datum])


args = setup_args()
input_file = args['input']
output_file = f"output_data/{args['output']}"


input_values = get_unique_values_for(input_file)

if(output_file_exists(output_file)):
    existing_values = get_unique_values_for(output_file)
    diff_values = set(input_values).difference(existing_values)
    print(f"appending file...{len(diff_values)} values")

    if(len(diff_values)):
        append_existing_file(output_file, list(diff_values))
else:
    create_output_file(output_file)
    diff_values = set(input_values)
    print(f"creating file...{len(diff_values)} values")

    append_existing_file(output_file, list(diff_values))
