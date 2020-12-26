from argparse import ArgumentParser
from os import getcwd
from os.path import exists

from pandas import read_csv, DataFrame


def __merge_duplicate_rows(csv_file_path: str, by_column: str, new_csv_file_path: str):
    csv_file = read_csv(csv_file_path)
    new_data = []
    duplicates = {}
    for item in [item for item in csv_file[by_column].iteritems()]:
        if item[1] not in duplicates.keys():
            duplicates[item[1]] = [item[0]]
        else:
            duplicates[item[1]].append(item[0])
    for key in duplicates.keys():
        tmp_values = {}
        for index, value in enumerate(duplicates.get(key)):
            row_values = [item for item in csv_file.iloc[index].items()][1:]
            tmp_values[index] = list(map(lambda val: val[1], row_values))
        duplicates[key] = [sum(x) for x in zip(*list(tmp_values.values()))]

    for key in duplicates.keys():
        new_data.append([key, *duplicates.get(key)])
    DataFrame(new_data, columns=csv_file.columns).to_csv(new_csv_file_path, index=False)


def confirmed_data_by_country(country: str):
    try:
        file = getcwd() + '/data/confirmed.csv'
        file_clean = getcwd() + '/data/confirmed-clean.csv'
        if not exists(file_clean):
            __merge_duplicate_rows(csv_file_path=file,
                                   by_column='Country',
                                   new_csv_file_path=file_clean)
        confirmed = read_csv(file_clean)
        countries = list(map(lambda count: count[1], [c for c in confirmed['Country'].iteritems()]))
        country_index = countries.index(country)
        return confirmed.loc[country_index], confirmed.columns[1:]
    except ValueError:
        print('Country does not exist')
        return None


def deaths_data_by_country(country: str):
    try:
        file = getcwd() + '/data/deaths.csv'
        file_clean = getcwd() + '/data/deaths-clean.csv'
        if not exists(file_clean):
            __merge_duplicate_rows(csv_file_path=file,
                                   by_column='Country',
                                   new_csv_file_path=file_clean)
        confirmed = read_csv(file_clean)
        countries = list(map(lambda count: count[1], [c for c in confirmed['Country'].iteritems()]))
        country_index = countries.index(country)
        return confirmed.loc[country_index], confirmed.columns[1:]
    except ValueError:
        print('Country does not exist')
        return None


def recovered_data_by_country(country: str):
    try:
        file = getcwd() + '/data/recovered.csv'
        file_clean = getcwd() + '/data/recovered-clean.csv'
        if not exists(file_clean):
            __merge_duplicate_rows(csv_file_path=file,
                                   by_column='Country',
                                   new_csv_file_path=file_clean)
        confirmed = read_csv(file_clean)
        countries = list(map(lambda count: count[1], [c for c in confirmed['Country'].iteritems()]))
        country_index = countries.index(country)
        return confirmed.loc[country_index], confirmed.columns[1:]
    except ValueError:
        print('Country does not exist')
        return None


parser = ArgumentParser()
parser.add_argument('--country',
                    help='Country for which you wish to receive data')
parser.add_argument('--data',
                    help='Data you wanna receive, possible arguments are "confirmed", "deaths" and "recovered"')
arguments = parser.parse_args()

if arguments.country is not None and arguments.data is not None:
    if arguments.data == 'confirmed':
        print('CONFIRMED data for ' + str(arguments.country))
        print(confirmed_data_by_country(arguments.country))
    elif arguments.data == 'deaths':
        print('DEATHS data for ' + str(arguments.country))
        print(deaths_data_by_country(arguments.country))
    elif arguments.data == 'recovered':
        print('RECOVERED data for ' + str(arguments.country))
        print(recovered_data_by_country(arguments.country))
    else:
        print('Unrecognized data command. Possible arguments are "confirmed", "deaths" and "recovered"')
else:
    print('You need to provide country and data type')
