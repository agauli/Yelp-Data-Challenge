import sys
import csv
def mapper():
    reader = csv.reader(sys.stdin, delimiter=',')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    for line in reader:
        try:
            if(len(line)) == 56:
                city = line[38]
                alcohol  = line[3]
                writer.writerow([city, alcohol])
        except ValueError:
            continue
if __name__ == "__main__":
    mapper()
