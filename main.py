#%%
import os
import time
import subprocess 
import numpy as np
 
from export_blockmesh_file import export_blockmesh_file
from export_batch_file import export_batch_file
from read_folder import read_folder

base_path=os.getcwd()
print(base_path)

###Important! Path should be relative for the json file.
#Data will be loaded in a different place then it was generated!
data_path=f"./data"

def cycle(Start=1, End=10001, parallel_jobs=1000):

    for Job_ID in range(Start,End,1):  

        sample_path=f"{data_path}/sample.{Job_ID}"
        if not os.path.isdir(sample_path):
            os.mkdir(sample_path)

        #### generate parameters
        params = np.random.rand(28) 

        #### give parameters to generate a interface file for the meshing process in OpenFOAM
        export_blockmesh_file(params,sample_path)

        #### generate Slurm file and copy run script into the working directory 
        export_batch_file(sample_path,Job_ID)
        os.system(f"cp {base_path}/Allrun_template.sh {sample_path}/Allrun.sh")

        os.chdir(sample_path)

        #### check how many jobs are Running and are in Que. 
        #### To not overcrowd the server
        var = int(os.popen("squeue -u jdecke |wc -l").read()) #edit Username!
        while var > parallel_jobs:
            time.sleep(10)
            var = int(os.popen("squeue -u jdecke |wc -l").read()) #edit Username!

        #### start the new Slurmfile
        if os.path.exists(f'{os.getcwd()}/Job_{Job_ID}.sh'):
            subprocess.run(['sbatch', f'{os.getcwd()}/Job_{Job_ID}.sh'])
            print(f'Job Nr: {Job_ID} started')
        else:
            print(f'Job Nr: {Job_ID} not started')

        os.chdir(base_path) 

def wait_to_make_json(datasetname="default"):
    var = int(os.popen("squeue -u jdecke | wc -l").read()) #edit Username!
    while var > 2:
        time.sleep(30)
        var = int(os.popen("squeue -u jdecke | wc -l").read()) #edit Username!
    read_folder(data_path, datasetname)

if __name__ == "__main__":
    cycle(Start=0, End=10001, parallel_jobs=1000)
    wait_to_make_json(datasetname = "dataset_10000_all.json")