import os
import copy

class MitsubaRenderer:
    def __init__(self, mitsuba_install_dir, resultsDir, scenesDir, deps_dir = None):
        self.mitsuba_install_dir = mitsuba_install_dir
        self.resultsDir = resultsDir
        self.scenesDir = scenesDir
        self.deps_dir = deps_dir

        os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH'] + ":" + self.mitsuba_install_dir + ":" + self.mitsuba_install_dir +"/lib" + ":" + self.mitsuba_install_dir +"/lib64"
        
        if self.deps_dir:
            os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH'] + ":" + self.deps_dir +"/lib" + ":" + self.deps_dir +"/lib64"
        os.environ['PATH'] = os.environ['PATH'] + ":" + self.mitsuba_install_dir + ":" + self.mitsuba_install_dir +"/bin"

        makeSafeDir(self.resultsDir)

    def runTestCase(self, scene, sceneVariant, resolution, testCase, max_component_value = 0, spp = 64):
        makeSafeDir(self.resultsDir + "/" + scene + sceneVariant)
        parameters = copy.deepcopy(testCase.parameters)

        for parameter in parameters:
            value = parameters[parameter]
            if isinstance(value, str):
                if "$SCENE$" in value:
                    parameters[parameter] = value.replace("$SCENE$", self.resultsDir + "/" + scene + sceneVariant + "/" + scene + sceneVariant)
                    print(value)
                    print(parameters[parameter])

        if not parameters.__contains__("sampleCount"):
            parameters["sampleCount"] = spp
        if not parameters.__contains__("maxComponentValue") and max_component_value > 0:
            parameters["maxComponentValue"] = max_component_value
        
        parameters["width"] = resolution[0]
        parameters["height"] = resolution[1]
        parameterString = extractParameters(parameters)
        sceneFileName = self.scenesDir + scene +"/" + scene + sceneVariant + "_auto.xml"

        outFile = self.resultsDir + "/" + scene + sceneVariant + "/" + scene + sceneVariant + "-" + testCase.name + ".exr"

        command = "mitsuba"
        command += " " + sceneFileName
        command += " " + parameterString
        #command += " --spp " + str(spp)
        command += " -o " + str(outFile)
        command += " > " + outFile.replace(".exr", ".log")
        print(command)
        os.system(command)


    def run(self, sceneFile, outfile, spp = 64):
        command = "pbrt"
        command += " " + sceneFile
        command += " --spp " + str(spp)
        command += " --outfile " + str(outfile)
        command += " > " + outfile.replace(".exr", ".log")
        print(command)
        os.system(command)

def makeSafeDir(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)


def extractParameters(parameters):
    parameterString = ""

    for parameter in  parameters:
        parameterString += "-D " + str(parameter) + "=" + str(parameters[parameter]) + " "       
    return parameterString

def run(sceneFile, outfile, spp = 64):
    command = "mitsuba"
    command += " " + sceneFile
    command += " -o " + str(outfile)
    command += " > " + outfile.replace(".exr", ".log")
    print(command)
    os.system(command)