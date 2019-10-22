import tempfile
import urllib.request
import time
import shutil
import io

file_columns = {'constructors'          : ['constructorId', 'constructorRef', 'teamName', 'nationality', 'url'],
                'races'                 : ['raceId', 'year', 'round', 'circuitId', 'circuitName', 'date', 'time', 'url'],
                'circuits'              : ['circuitId', 'circuitRef' , 'circuitName', 'location',
                                           'country', 'lat', 'lng', 'alt', 'url'],
                'results'               : ['resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'position',
                                           'postionText', 'positionOrder', 'points', 'laps', 'time', 'milliseconds',
                                           'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId'],
                'driver'                : ['driverId', 'driverRef', 'number', 'code', 'forename', 'surname',
                                           'dob', 'nationality', 'url'],
                'driver_standings'      : ['driverStandingsId', 'raceId', 'driverId', 'points', 'position',
                                           'positionText', 'wins'],
                'qualifying'            : ['qualifyingId', 'raceId', 'driverId', 'constructorId', 'number', 'position',
                                           'q1', 'q2', 'q3'],
                'status'                : ['statusId', 'status']
}

def main():
    url = 'http://ergast.com/downloads/f1db_csv.zip'
    dst = '/Users/freekkalter/f1_data_analysis/f1db_csv/'
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

if __name__ == '__main__':
    main()
