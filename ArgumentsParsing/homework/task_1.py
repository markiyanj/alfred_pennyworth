import argparse
import csv


def beer_review(path, year, mode):
    with open(f'{path}/{year}.csv', 'r') as f:
        reader = csv.reader(f)
        with open(f'{args.destination_path}/{args.destination_filename}', mode=mode) as f:
            writer = csv.writer(f)
            for line in reader:
                if mode == 'a':
                    if line[0].startswith('brewery_name'):
                        continue
                writer.writerow(line)


def check_mode(num):
    if num == 0:
        return 'w'
    return 'a'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-sy", "--start_year",
                        required=False,
                        dest="start_year",
                        help="start year",
                        default=1998)
    parser.add_argument("-ey", "--end_year",
                        required=False,
                        dest="end_year",
                        help="end year",
                        default=1999)
    parser.add_argument("-p", "--path",
                        required=True,
                        dest="path",
                        help="path to source file")
    parser.add_argument("-d_p", "--destination_path",
                        required=False,
                        dest="destination_path",
                        help="destination path",
                        default="local_beer_review")
    parser.add_argument("-d_f", "--destination_filename",
                        required=False,
                        dest="destination_filename",
                        help="destination filename",
                        default="all_review.csv")
    args = parser.parse_args()

    count = 0
    for i in range(int(args.start_year), int(args.end_year) + 1):
        if count == 0:
            mode = "w"
        else:
            mode = "a"
        if i == 2005 or i == 2006:
            for j in range(1, 3):
                year = f'{i}-{j}'
                beer_review(args.path, year, check_mode(count))
                count += 1
        elif i == 2007 or i == 2008:
            for j in range(1, 13):
                year = f'{i}-{j}'
                beer_review(args.path, year, check_mode(count))
                count += 1
        else:
            beer_review(args.path, i, check_mode(count))
        count += 1
