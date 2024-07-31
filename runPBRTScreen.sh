#!/bin/bash
CURRENTDIR=${PWD}

# HOSTS=("c01" "c02" "c03" "c04" "c05" "c06" "c07" "c08" "c09")
# SCENES=("JungleRuins" "country-kitchen" "landscape" "290skydemo" "earth" "oriental-lantern")

# HOSTS=("c02" "c03" "c04" "c05" "c06" "c07")
# SCENES=("JungleRuins" "country-kitchen" "landscape" "290skydemo" "earth" "oriental-lantern")

# HOSTS=("c02" "c03" "c04" "c05")
# SCENES=("oriental-lantern" "museum" "cornell-box-lightshaft" "cornell-box-ball")

# HOSTS=("c01" "c02" "c03")
# SCENES=("JungleRuins" "country-kitchen" "landscape")

# HOSTS=("c01" "c02" "c03")
# SCENES=("country-kitchen" "landscape" "earth")

# HOSTS=("c01" "c02" "c03")
# SCENES=("country-kitchen" "landscape" "earth")

HOSTS=("c02")
SCENES=("earth")

NUM=${#SCENES[@]}
let NUM=$NUM-1

for i in $(seq 0 $NUM) ; do
    SCENE=${SCENES[i]}
    PYTHONCMD="python3 runPBRTTestCase.py --scene ${SCENE}"
    SCRIPT="screen -S PBRTPerNode -X stuff $'cd ${CURRENTDIR} ; ${PYTHONCMD} ; exit \n'"
    ssh ${HOSTS[i]} "screen -ls | awk '{print $1}' | xargs -I{} screen -X -S {} quit"
    sleep 1
    ssh ${HOSTS[i]} "screen -dmS PBRTPerNode"
    sleep 1
    echo ${HOSTS[i]}
    echo ${SCRIPT}
    ssh ${HOSTS[i]} "${SCRIPT}"
done