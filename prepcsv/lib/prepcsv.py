import tempfile
import urllib.request
import requests as req
import time
import shutil
import io
import sys
import os
from pathlib import Path

file_columns = {'constructors'          : ['constructorId', 'constructorRef', 'teamName', 'nationality', 'url'],
                'races'                 : ['raceId', 'year', 'round', 'circuitId', 'circuitName', 'date', 'time', 'url'],
                'circuits'              : ['circuitId', 'circuitRef' , 'circuitName', 'location',
                                           'country', 'lat', 'lng', 'alt', 'url'],
                'results'               : ['resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'position',
                                           'postionText', 'positionOrder', 'points', 'laps', 'time', 'milliseconds',
                                           'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId'],
                'drivers'                : ['driverId', 'driverRef', 'number', 'code', 'forename', 'surname',
                                           'dob', 'nationality', 'url'],
                'driver_standings'      : ['driverStandingsId', 'raceId', 'driverId', 'points', 'position',
                                           'positionText', 'wins'],
                'qualifying'            : ['qualifyingId', 'raceId', 'driverId', 'constructorId', 'number', 'position',
                                           'q1', 'q2', 'q3'],
                'status'                : ['statusId', 'status']
}

def new_data(url, dst):
    res = req.head(url)
    new_size = int(res.headers['Content-Length'])
    try:
        with open(dst+'/zipped_size') as fh:
            size = int(fh.readline().strip())
            if new_size > size:
                print(new_size, size)
                return new_size
    except FileNotFoundError:
        return new_size
    return -1


def main():
    p = Path(os.path.realpath(__file__))

    url = 'http://ergast.com/downloads/f1db_csv.zip'
    dst = os.path.join(p.parent.parent.parent, 'f1db_csv/')
    wait = False
    if len(sys.argv) > 1 and sys.argv[1] == '--wait':
        wait = True
    new_size = new_data(url, dst)
    if not wait and new_size < 0:
        print('no new data')
        sys.exit(0)

    if wait:
        while True:
            print('no new data found, waiting')
            time.sleep(60*10) # 10 minutes
            new_size = new_data(url, dst)
            if new_size > 0:
                print('new data found')
                break
            else:
                print(time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime()), 'still waiting')
    with tempfile.TemporaryDirectory() as tmpdirname:
        filename = f'{tmpdirname}/f1db_csv.zip'
        urllib.request.urlretrieve(url, filename=filename)
        print('downloaded file')
        shutil.unpack_archive(filename, extract_dir=f'{tmpdirname}/f1db_csv/')
        print('unpacked file')
        shutil.rmtree(dst, ignore_errors=True)
        shutil.copytree(f'{tmpdirname}/f1db_csv', dst)
        print('moved to destination')

    for filename, columns in file_columns.items():
        with open(f'{dst}/{filename}.csv', 'r+', encoding='utf-8') as fh:
            content = fh.read()
            fh.seek(0)
            print(','.join(columns), file=fh)
            fh.write(content)
    print('added columnnames')
    with open(dst + '/zipped_size', 'w') as fh:
        fh.write(str(new_size))
    print('written new zipped size')

if __name__ == '__main__':
    main()
