from tld import get_tld
import argparse

parser = argparse.ArgumentParser(usage="python3 domain.py -f file", add_help=False)
parser.add_argument("-f", "--file", dest="file", help="Select a target list file (e.g. list.txt )")
args = parser.parse_args()

if args.file:
    for line in open(args.file):
        line = line.strip('\n')
        #print(line)
        try:
            result=get_tld(line, as_object=True, fix_protocol=True)
            root_domain = result.fld
            print(root_domain)
            with open('success.txt', 'a+', encoding='utf-8') as f:
                f.write(root_domain + '\n')
        except:
            pass

if args.file is None:
    parser.print_help()
    exit(0)