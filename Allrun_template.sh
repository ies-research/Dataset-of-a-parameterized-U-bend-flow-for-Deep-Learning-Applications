#!/bin/bash

#########Import
#########And
#########Source Stuff

source /usr/lib/openfoam/OpenFOAM-plus/etc/bashrc

mkdir /work/input /work/output
mkdir /work/input/net /work/input/para /work/input/pic
mkdir /work/output/net /work/output/para /work/output/pic

#########Create Mesh  
#########And
#########Run OpenFOAM

blockMesh > /work/log.blockmesh
splitMeshRegions -cellZones -overwrite
checkMesh > /work/log.checkMesh
rm -r constant/polyMesh
ausgabe=$(awk 'BEGIN {ausgabe=10000} {if ($1 == "Mesh" && $2 == "OK.") {ausgabe=0}} END {print ausgabe}' ../work/log.checkMesh) 
if [ "$ausgabe" -eq "0" ]
then
chtMultiRegionSimpleFoam > /work/log.chtMultiRegionSimpleFoam

#########AWK Results 
#########And
#########Postprocess

objectivep=$(awk 'END {print $2}' postProcessing/fluid/pressureLoss/0/surfaceFieldValue.dat)
res=$(awk 'END {print $5}' postProcessing/fluid/residualsFluid/0/residuals.dat) 
ausgabe=$(awk "BEGIN {if ($res >= 0.0001) {print 11000} else {print $objectivep}}")
fi
objectiveT=$(awk 'END {print $2}' postProcessing/solid/objectiveValue/0/surfaceFieldValue.dat)
ausgabe2=$(awk "BEGIN {if ($ausgabe >= 10000) {print $ausgabe} else {print $objectiveT}}")
echo $ausgabe > results_tmp.out
echo $ausgabe2 >> results_tmp.out

#########Extract
#########Data
#########to the defined formats

#####Parameterdata
mv /work/params.in /work/input/para/params
mv results_tmp.out /work/output/para/targets
vergl=${ausgabe%.*}
if [ "$vergl" -ge "10000" ]
then
echo "Job aborted" 
else

#####Imagedata
./createBilder

#####Meshdata

/venv/bin/python loadnetfiles.py 

fi
#####delete everything else
rm /work/para* /work/Job* /work/log.*
####close Docker
exit 

