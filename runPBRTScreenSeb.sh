#!/bin/bash
#set -e
CURRENTDIR=${PWD}

PBRTDIR=/home/kehan/Develop/pbrt-v4-Distance-Guiding-guidedrr-vspg/install/
RESULTSDIR=./pbrt-results-seb/test

TESTCONFIG=testcases/pbrt/volumeguiding
#TESTCASE=reference
SCENESCONFIG=scenesconfigpbrt
#SCENE=CoronaBenchmark2

HOSTS=("c01" "c02" "c03" "c04" "c05" "c06" "c07" "c08" "c09")
SCENES=("pool" "CoronaBenchmark2" "CoronaBenchmark2" "JungleRuins" "JungleRuins" "country-kitchen" "country-kitchen" "290skydemo" "290skydemo")
VARIANTS=("" "" "-volume-homo" "" "-volume-homo" "" "-volume-homo" "-deep" "-deeper")

#HOSTS=( "c06" "c07" "c08" "c09")
#SCENES=("JungleRuins" "country-kitchen" "oriental-lantern" "290skydemo")
#VARIANTS=("-volume-hetero" "-volume-hetero" "" "-deeper")

#SCENES=("JungleRuins" "oriental-lantern" "290skydemo" "290skydemo")
#VARIANTS=("" "" "-even-deeper" "-super-deep")

#SCENES=("oriental-lantern" "290skydemo")
#VARIANTS=( "" "-super-deep")

SPP=128
#TIME=172800
TIME=0
#TIME=360

for i in {0..0} ; do
    SCENE=${SCENES[i]}
    VARIANT=${VARIANTS[i]}
    echo ${SCENE}
    PYTHONCMD="python3 runPBRTTestCaseSeb.py --pbrtdir ${PBRTDIR} --resultsdir ${RESULTSDIR} --scenesconfig ${SCENESCONFIG} --testconfig ${TESTCONFIG} --scene ${SCENE} --variant='${VARIANT}' --spp ${SPP} --time ${TIME}"
    echo $PYTHONCMD
    SCRIPT="screen -S PBRTTestCase -X stuff $'cd ${CURRENTDIR} ; ${PYTHONCMD} ; exit \n'"
    ssh ${HOSTS[i]} "screen -ls | awk '{print $1}' | xargs -I{} screen -X -S {} quit"
    sleep 1
    ssh ${HOSTS[i]} "screen -dmS PBRTTestCase"
    sleep 1
    echo ${HOSTS[i]}
    echo ${SCRIPT}
    ssh ${HOSTS[i]} "${SCRIPT}"
done