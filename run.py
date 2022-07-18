from data import Data
from writer import write_file

def get_expected_concept_count():
    try:
        count = int(input("Enter how many records you wish to enter : "))
    except ValueError:
        print("Please enter an integer!\n")
        count = get_expected_concept_count()

    return count

def main():
    while True:
        expected_record_count = get_expected_concept_count()

        records = []

        for i in range(expected_record_count):
            records.append(Data.create_fuel_record())

            print(f"==================== End of record {i+1} ======================")

        try:
            write_file(records)

        except Exception as e:
            print(e)

        break


if __name__ == '__main__':
    main()