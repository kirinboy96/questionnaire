import os
import csv
import pathlib
import collections


class make_csv(object):
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = collections.defaultdict(int)
        self.column=["Food", "Count"]
        """
        CSVファイルがなければ作成
        さらにヘッダーをつける
        """
        if not os.path.exists(csv_file):
            pathlib.Path(csv_file).touch()
            with open(self.csv_file,"w") as qustion_file:
                fieldnames = ["Food", "Count"]
                writer = csv.DictWriter(qustion_file, fieldnames=fieldnames)
                # ヘッダーを付ける
                writer.writeheader()

    def load_data(self):
        """
        CSVファイルに入っているデータをdict型で返す
        その際、Countはint型にする
        """
        with open(self.csv_file, 'r+') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data[row["Food"]] = int(
                    row["Count"])
        return self.data

    def save(self):
        """Save data to csv file."""
        # TODO (jsakai) Use locking mechanism for avoiding dead lock issue
        with open(self.csv_file, 'w+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column)
            writer.writeheader()

            for food, count in self.data.items():
                writer.writerow({
                    'Food': food,
                    'Count': count
                })

    def increase(self,food):
        self.data[food]+=1
        self.save()

