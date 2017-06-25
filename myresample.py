#!/usr/bin/env python

# myresample:
# Script to resample tickdata into Open High Low Close Volume bars
# Was developed to resample Bitcoincharts csv data
# requires pandas. (pip install pandas)

import pandas as pd

import argparse

import sys
import os.path


parser = argparse.ArgumentParser(description='Myresample: resample tick data into OHLCV')
parser._action_groups.pop()

required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

required.add_argument('--file', nargs=1, help='Path to input csv file')


optional.add_argument('--outfile', nargs='?', help='Path to output csv file '
                                                   '(default: "resampled" + "file" + "period".csv)')

optional.add_argument('--period', nargs='?',
                      help='Resample period (default: 15min). '
                         'Pandas format (see more at: '
                         'http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases )')
optional.add_argument('--fillna', nargs='?',
                      help='How to fill N/A values (default: 0.0).')
optional.add_argument('--sep', nargs='?',
                      help='Output csv separator (default: ,).')


args = parser.parse_args()

if args.file is None:
    parser.print_help()
    sys.exit(0)

if args.file[0] is None or not os.path.isfile(args.file[0]):
    print('File "%s" not found.' % args.file[0])
    sys.exit(1)


file = args.file[0]
period = args.period or '15min'
fillna = args.fillna or 0.0
sep = args.sep or ','
outfile = os.path.join(os.path.dirname(file), ('resampled_' + os.path.splitext(os.path.basename(file))[0]
                                               + '_' + period + '.csv'))

if args.outfile is not None:
    outfile = args.outfile[0]


df = pd.read_csv(file, names=['Date_Time', 'Price', 'Volume'])
df.set_index(['Date_Time'], inplace=True)
df.index = pd.to_datetime(df.index, unit='s')

bars = df.Price.resample(period).ohlc()
print('counted ohlc')
volumes = df.Volume.resample(period).sum().fillna(fillna)

ohlcv = pd.concat([bars, volumes], axis=1)
ohlcv.to_csv(outfile, index_label='date', sep=sep)

print('Done. Resampled data into %s' % outfile)
