import argparse

parser = argparse.ArgumentParser(description="opis")
parser.add_argument('file', help='nazwa pliku')
parser.add_argument('-n','--number',help='liczba',type=int)
parser.add_argument('-bpar', '--bpar', help='flaga', action='store_true')
args = parser.parse_args()
print(f'{args.file = }')
print(f'{args.number = }')
print(f'{args.bpar = }')