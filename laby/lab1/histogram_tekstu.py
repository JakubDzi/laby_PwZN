import argparse
import ascii_graph
import os

parser = argparse.ArgumentParser(description="Program robi histogram wyrazów w podanym pliku tekstowym")
parser.add_argument('file', help='nazwa pliku do wczytania')
parser.add_argument('-n', '--number', help='dla ilu wyrazów wyświetlić histogram (domyślnie 10)', type=int, default=10)
parser.add_argument('-l', '--length', help='minimalna długość słowa (domyślnie 0)', type=int, default=0)
parser.add_argument('-b', '--block', help='plik z ignorowanymi wyrazami', type=str, default='')
args = parser.parse_args()
zlicz = {}
bloklist = {}
with open(args.file, encoding='utf-8') as f:
    if args.block != '':
        with open(args.block, encoding='utf-8') as fb:
            for line in fb:
                wyrazy = (line.strip().split())
                for wyraz in wyrazy:
                    bloklist[wyraz] = 1
    for line in f:
        wyrazy = (line.strip().split())
        for wyraz in wyrazy:
            if (wyraz not in zlicz) & (len(wyraz) >= args.length) & (wyraz not in bloklist):
                zlicz[wyraz] = 1
            elif(len(wyraz) >= args.length) & (wyraz not in bloklist):
                zlicz[wyraz] += 1
    zlicz = dict(sorted(zlicz.items(), key=lambda item: item[1], reverse=True))
    zlista = [(k, v) for k, v in zlicz.items()]
    graph = ascii_graph.Pyasciigraph()
    cnt = 0
    os.system('color')
    for line in graph.graph('Histogram wyrazów', zlista):
        if cnt <= args.number+1:
            if cnt == 0:
                print('\x1b[0;37;40m', end='')
            elif cnt == 1:
                print('\x1b[7;30;40m', end='')
            else:
                kolorint = (cnt % 2)*3+31
                print('\x1b[0;%s;40m' % kolorint, end='')
            print(line)
            cnt += 1
    print('\x1b[0m', end='')
