import argparse


parser = argparse.ArgumentParser(description='Powiedz Witam serdecznie pana --name')
parser.add_argument('--name', type=str, help='Twoje imie prosze Pana!' )
parser.add_argument('--wiek', type=str, help='Twoj wiek prosze Pana!!' )

args = parser.parse_args()

print('Witam serdecznie pana ' + args.name)

print('Witam serdecznie pana! Panski wiek! ' + args.wiek)
