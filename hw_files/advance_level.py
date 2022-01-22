class Converter:
    SAME_FORMAT_MESSAGE = "You are trying to convert to the same format"
    NOT_SUPPORTED_FORMAT_MESSAGE = "You are trying to convert to the same format"
    EMPTY_FILE_MESSAGE = "You are trying to convert an empty file"

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_ext = file_name.split(".")[-1].lower()

    def __from_csv(self):
        import csv
        with open(self.file_name, "r") as file:
            csv_dict_reader = csv.DictReader(file)
            return list(csv_dict_reader)

    def __from_json(self):
        import json
        with open(self.file_name, "r") as file:
            return json.load(file)

    def __from_pickle(self):
        import pickle
        with open(self.file_name, "rb") as file:
            return pickle.load(file)

    def to_csv(self):
        import csv
        if self.file_ext == "csv":
            print(Converter.SAME_FORMAT_MESSAGE)
            return
        elif self.file_ext == "json":
            file_data = self.__from_json()
        elif self.file_ext == "pickle":
            file_data = self.__from_pickle()
        else:
            print(Converter.NOT_SUPPORTED_FORMAT_MESSAGE)
            return
        if not file_data:
            print(Converter.EMPTY_FILE_MESSAGE)
            return
        with open(f"{self.file_name.split('.')[0]}.csv", "w") as file:
            csv_dict_writer = csv.DictWriter(file, fieldnames=file_data[0].keys())
            csv_dict_writer.writeheader()
            csv_dict_writer.writerows(file_data)

    def to_json(self):
        import json
        if self.file_ext == "json":
            print(Converter.SAME_FORMAT_MESSAGE)
            return
        elif self.file_ext == "csv":
            file_data = self.__from_csv()
        elif self.file_ext == "pickle":
            file_data = self.__from_pickle()
        else:
            print(Converter.NOT_SUPPORTED_FORMAT_MESSAGE)
            return
        if not file_data:
            print(Converter.EMPTY_FILE_MESSAGE)
            return
        with open(f"{self.file_name.split('.')[0]}.json", "w") as file:
            json.dump(file_data, file)

    def to_pickle(self):
        import pickle
        if self.file_ext == "pickle":
            print(Converter.SAME_FORMAT_MESSAGE)
            return
        elif self.file_ext == "csv":
            file_data = self.__from_csv()
        elif self.file_ext == "json":
            file_data = self.__from_json()
        else:
            print(Converter.NOT_SUPPORTED_FORMAT_MESSAGE)
            return
        if not file_data:
            print(Converter.EMPTY_FILE_MESSAGE)
            return
        with open(f"{self.file_name.split('.')[0]}.pickle", "wb") as file:
            pickle.dump(file_data, file)


if __name__ == "__main__":
    converter = Converter("temp.csv")
    converter.to_csv()
    converter.to_json()
    converter.to_pickle()

    converter = Converter("temp.json")
    converter.to_csv()
    converter.to_json()
    converter.to_pickle()

    converter = Converter("temp.pickle")
    converter.to_csv()
    converter.to_json()
    converter.to_pickle()
