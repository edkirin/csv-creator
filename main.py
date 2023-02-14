import csv
import random
from faker import Faker
from models import ImportActionEnum


fake = Faker()

def create_importer_general_csv_data(number_of_records: int) -> None:
    with open("importer-general-data.csv", mode="w") as csv_file:
        file_writer = csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)

        file_writer.writerow([
            "asset_id",
            "asset_action",
            "serial_number",
            "brand_id",
            "model_id",
        ])

        for _ in range(number_of_records):
            file_writer.writerow([
                fake.pystr(min_chars=20, max_chars=20),
                ImportActionEnum.INSERT.value,
                fake.random_number(digits=30, fix_len=True),
                fake.random_number(),
                fake.random_number(),
            ])


def main():
    create_importer_general_csv_data(100)


if __name__ == "__main__":
    main()
