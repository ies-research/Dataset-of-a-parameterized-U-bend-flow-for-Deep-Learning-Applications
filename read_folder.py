import os
import json
import numpy as np

class read_folder:
    def __init__(self, path, name):
        self.name = name
        self.path = path
        self.main(self.path, f"{self.path}{self.name}")

    def get_folder_info(self,path, key, data):
        if not key == "":
            key = f"{key}_"
        for ele in os.listdir(path):        
            if os.path.isdir(os.path.join(path, ele)):
                self.get_folder_info(os.path.join(path, ele),f"{key}{ele}", data)
            else:
                data[f"{key}{ele.split('.')[0]}"] = os.path.join(path, ele)

    def get_exp(self,path):
        data2 = {}
        for ele in os.listdir(path):
            data = {}
            if os.path.isdir(os.path.join(path, ele)):
                data2[ele] = {}
                self.get_folder_info(os.path.join(path, ele), "", data2[ele])
        if "input" in data2 and len(data2["input"]) == 8: #get sufficent Samples to the .json file only
            data.update(data2) #get sufficent Samples to the .json file only
        #data.update(data2) #get all Samples to the .json file
        return data

    def get_all(self,path):
        data = {}
        for i, ele in enumerate(os.listdir(path)):
            if os.path.isdir(os.path.join(path, ele)):
                key = f"{ele}"
                value= self.get_exp(os.path.join(path, ele))
                if value: 
                    data[key] = value
            if i % 500 == 499: 
                print(i)
            #if i == 25:         #to get an overview
            #    return data     #of the outputfile
        return data

    def write_json(self, path, name, indent=4):
        try:
            with open(path, "w") as f:
                json.dump(name, f, indent=indent)

            print("Json file {0} created.".format(path))
        except ValueError:
            print("Error writing json file.")


    def main(self, path, name):
        data = self.get_all(path)
        self.write_json(name, data)

if __name__ == "__main__":
    path="./"
    name="dataset_10000_red.json"
    read_folder(path,name)

