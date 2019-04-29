import sys
import getopt
from Predictor import Predictor


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, "h:d:t:p:", ["date=", "time=", "plate="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    print(opts)
    for opt, arg in opts:
        print(opt)
        print(arg)
        if opt == '-h':
            print 'main.py -d <date> -t <time> -p <plate>'
            sys.exit()
        elif opt in ("-d", "--date"):
            date = arg
        elif opt in ("-t", "--time"):
            time = arg
        elif opt in ("-p", "--plate"):
            plate = arg

    print(date)
    result = Predictor().predict(plate, date, time)
    print(result['msg'])


if __name__ == "__main__":
    print(sys.argv[1:])
    main(sys.argv[1:])
