import os
import copy
import json
import pathlib

class BlenderRenderer:
    def __init__(self, blender_install_dir, resultsDir, scenesDir):
        self.blender_install_dir = blender_install_dir
        self.resultsDir = resultsDir
        self.scenesDir = scenesDir

        makeSafeDir(self.resultsDir)
    
    def runTestCase(self, scene, sceneVariant, resolution, testCase, spp = 64, deleteTestCaseJSON=True):
        makeSafeDir(self.resultsDir + "/" + scene + sceneVariant)

        outFile = self.resultsDir + "/" + scene + sceneVariant + "/" + scene + sceneVariant + "-" + testCase.name + ".exr"
        
        scriptFolder = pathlib.Path(__file__).parent.resolve()

        parameters = copy.deepcopy(testCase.parameters)
        for parameter in parameters:
            value = parameters[parameter]
            if isinstance(value, str):
                if "$SCENE$" in value:
                    parameters[parameter] = value.replace("$SCENE$", self.resultsDir + "/" + scene + sceneVariant + "/" + scene + sceneVariant)
        
        parameters["render.filepath"] = outFile

        parameters["render.resolution_percentage"] = 100
        parameters["render.resolution_x"] = resolution[0]
        parameters["render.resolution_y"] = resolution[1]

        parameters["cycles.samples"] = spp
        #parameters["cycles.time_limit"] = resolution[1]

        testCaseFile = self.resultsDir + "/" + scene + sceneVariant + "/" + scene + sceneVariant + "-" + testCase.name + ".json"
        with open(testCaseFile, 'w') as f:
            json.dump(parameters, f, indent=4)

        sceneFile = self.scenesDir + scene +"/" + scene + sceneVariant + ".blend"

        command = self.blender_install_dir + "/blender"
        command += " --background" 
        command += " " + sceneFile
        command += " -P " + str(scriptFolder) + "/RunBlenderTestCase.py"
        command += " -- "
        command += " -j " + testCaseFile
        command += " > " + outFile.replace(".exr", ".log")
        print(command)
        os.system(command)
        
        if deleteTestCaseJSON and os.path.isfile(testCaseFile):
            os.remove(testCaseFile)
        
    """
    def run(self, sceneFile, outfile, spp = 64):
        command = self.blender_install_dir + "/blender"
        command += " --background" 
        command += " " + sceneFile
        command += "-P blender/RunBlenderTestCase.py"
        command += " -- "
        command += " -s " + str(spp)
        command += " -b " + str(20)
        command += " -g"
        print(command)
        os.system(command)
    """
def makeSafeDir(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)