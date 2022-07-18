import csv

from data import Data

def write_file(records:list[Data]):

    field_names = [
        'DATE',
        'START TIME',
        'FIREWOOD USAGE KG',
        'FIREWOOD MC (%)',
        'BRIQUETTE USAGE KG',
        'INITIAL PRESSURE',
        'Average LOADING',
        'FLUE GAS',
        'FLUE GAS',
        'FINAL PRESSURE',
        'END TIME'
    ]

    with open('new_data.csv','w') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=field_names)

        writer.writeheader()

        for i in range(0,len(records)):
            writer.writerow({
                'DATE' : records[i].date,
                'START TIME' : records[i].start_time,
                'FIREWOOD USAGE KG' : records[i].firewood_usage_kg,
                'FIREWOOD MC (%)' : records[i].firewood_mc,
                'BRIQUETTE USAGE KG' : records[i].briquette_usage_kg,
                'INITIAL PRESSURE' : records[i].initial_pressure,
                'Average LOADING' : records[i].average_loading,
                'FLUE GAS' : records[i].flue_gas_1,
                'FLUE GAS': records[i].flue_gas_2,
                'FINAL PRESSURE' : records[i].final_pressure,
                'END TIME' : records[i].end_time
            })