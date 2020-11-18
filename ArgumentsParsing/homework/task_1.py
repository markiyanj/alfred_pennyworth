import argparse
import csv
import os
from datetime import datetime


def beer_review(path_to_source, dest_path, file_name, csv_files: list):
    count = 0
    with open(f'{dest_path}/{file_name}', 'w') as file:
        writer = csv.writer(file)
        for i in csv_files:
            with open(f'{path_to_source}/' + i, 'r') as f:
                reader = csv.reader(f)
                if count == 0:
                    for row in reader:
                        writer.writerow(row)
                else:
                    for row in reader:
                        if row[0].startswith('brewery_name'):
                            continue
                        writer.writerow(row)
            count += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path",
                        required=True,
                        dest="path",
                        help="path to source file")
    parser.add_argument("-sy", "--start_year",
                        required=False,
                        dest="start_year",
                        help="start year",
                        default=min(os.listdir('beer_review/'))[:4])
    parser.add_argument("-ey", "--end_year",
                        required=False,
                        dest="end_year",
                        help="end year",
                        default=max(os.listdir('beer_review/'))[:4])

    year = parser.parse_args()

    parser.add_argument("-d_p", "--destination_path",
                        required=False,
                        dest="destination_path",
                        help="destination path",
                        default="local_beer_review")
    parser.add_argument("-d_f", "--destination_filename",
                        required=False,
                        dest="destination_filename",
                        help="destination filename",
                        default=f"{year.start_year}-{year.end_year}_{datetime.now().strftime('%d_%m_%y_%I:%M')}.csv")

    args = parser.parse_args()

    csv_files = []
    for file in os.listdir(args.path):
        for name in range(int(args.start_year), int(args.end_year) + 1):
            if file.startswith(str(name)):
                csv_files.append(file)

    beer_review(args.path, args.destination_path, args.destination_filename, csv_files)
