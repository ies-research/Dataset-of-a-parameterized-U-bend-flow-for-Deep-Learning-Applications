from math import cos, sin, pi
import sys

class export_batch_file:
    def __init__(self, path,Job_ID ):

        self.path = path
        self.Job_ID =Job_ID
        self.make_file()

    def make_file(self):
        f = open(f"{self.path}/Job_{self.Job_ID}.sh", "w")
        f.write("#!/bin/bash\n")
        f.write("#SBATCH --output=log.dockerrun\n")
        f.write("#SBATCH --time=04:00:00\n")
        f.write("#SBATCH --ntasks=1\n")
        f.write("#SBATCH --cpus-per-task=1\n")
        f.write("#SBATCH --mem=2000\n")
        f.write(f"#SBATCH --job-name=Sample_{self.Job_ID}\n")
        f.write("#SBATCH --partition=main\n")
        f.write("date;hostname;pwd\n")
        f.write("srun podman pull jdecke/foamy:latest\n") #required per node only the first time
        f.write("srun podman run --privileged --rm -v $PWD/:/work/ --workdir /mnt/ --entrypoint ./Startrun.sh foamy:latest \n")
        f.write("sleep 5s\n")
        f.write(f"scancel -n Sample_{self.Job_ID}\n")
        f.write("echo 'canceled'\n")
        f.close()
