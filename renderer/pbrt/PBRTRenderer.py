import os
import copy
import fnmatch

class PBRTRenderer:
    def __init__(self, pbrtInstallDir, resultsDir, scenesDir):
        self.pbrtInstallDir = pbrtInstallDir
        self.resultsDir = resultsDir
        self.scenesDir = scenesDir

        os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH'] + ":" + self.pbrtInstallDir +"lib"
        os.environ['PATH'] = os.environ['PATH'] + ":" + self.pbrtInstallDir +"bin"

        makeSafeDir(self.resultsDir)

    def runTestCase(self, scene, sceneInfo, testCase, budgetIsSPP = True, stats = False):
        sceneVariant = sceneInfo[0]
        resolution = sceneInfo[1]
        budget = sceneInfo[2]

        sceneVariantConcat = scene + sceneVariant
        resultsSceneDir = os.path.join(self.resultsDir, sceneVariantConcat)
        makeSafeDir(resultsSceneDir)
        logDir = os.path.join(resultsSceneDir, "log")
        makeSafeDir(logDir)

        fileName = sceneVariantConcat + "-" + testCase.name
        outFile = os.path.join(resultsSceneDir, fileName + ".exr")
        logFile = os.path.join(logDir, fileName + ".log")

        if os.path.exists(outFile):
            print('WARNING: ', outFile, ' already exists')

        parameters = copy.deepcopy(testCase.parameters)
        for parameter in parameters:
            value = parameters[parameter][1]
            if isinstance(value, str):
                if "$SCENE$" in value:
                    parameters[parameter][1] = value.replace("$SCENE$", os.path.join(self.resultsDir, sceneVariantConcat, sceneVariantConcat))
                    #print(value)
                    #print(parameters[parameter][1])
        
        integratorString = extractIntegrator(parameters)
        filmString = extractFilm(resolution, parameters, fileName + ".exr")
        tmpTestCaseFileName = os.path.join(self.scenesDir, scene, fileName + ".pbrt")
        
        tmpSceneFile = open(tmpTestCaseFileName,"w")
        tmpSceneFile.write(filmString)
        tmpSceneFile.write("\n")
        tmpSceneFile.write(integratorString)
        tmpSceneFile.write("\n")
        tmpSceneFile.write("Include \"" + sceneVariantConcat + "_auto.pbrt" + "\"")
        tmpSceneFile.write("\n")
        tmpSceneFile.close()

        budgetType = "spp" if budgetIsSPP else "time"

        command = "pbrt"
        command += " " + tmpTestCaseFileName
        if stats:
            command += " --stats "
        #command += " --nthreads " + str(1)
        command += f" --{budgetType} {budget}"
        command += " --outfile " + str(outFile)
        command += " 2>&1 | tee " + str(logFile)
        print(command)
        os.system(command)
        if not readLogFileNeedRerunVolume(logFile):
            break

        if os.path.isfile(tmpTestCaseFileName):
            os.remove(tmpTestCaseFileName)

def makeSafeDir(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)

def readLogFileNeedRerunVolume(logfile):
    with open(logfile, 'r') as log:
        list_of_lines = log.readlines()
    for line in list_of_lines:
        if fnmatch.fnmatch(line, "*: medium is not defined.\n"):
            return True
    return False

def extractFilm(resolution, parameters, outputFileName):
    filmString = ""
    filmString += "Film " +"\"rgb\"" + "\n"
    
    filmString += "\"string filename\" " + "\"" + outputFileName +"\""+ "\n"
    filmString += "\"integer xresolution\" ["+ str(resolution[0]) + "]" + "\n"
    filmString += "\"integer yresolution\" ["+ str(resolution[1]) + "]" + "\n"
    if parameters.__contains__("maxcomponentvalue"):
        filmString += "\"float maxcomponentvalue\" ["+ str(parameters["maxcomponentvalue"][1]) + "]" + "\n"
    return filmString

def extractIntegrator(parameters):
    integratorString = ""

    integratorString += "Integrator \"" + parameters["integrator"] + "\"\n"
    for parameter in  parameters:
        if parameter != "integrator" and parameter != "maxcomponentvalue":
            if str(parameters[parameter][0]) == "bool":
                integratorString += "\t" + "\"" + str(parameters[parameter][0]) + " " + str(parameter) + "\" " +  str(parameters[parameter][1]).lower() + "\n"
            elif str(parameters[parameter][0]) == "string":
                integratorString += "\t" + "\"" + str(parameters[parameter][0]) + " " + str(parameter) + "\" \"" +  str(parameters[parameter][1]) + "\"\n"
            else:
                integratorString += "\t" + "\"" + str(parameters[parameter][0]) + " " + str(parameter) + "\" " +  str(parameters[parameter][1]) + "\n"
    return integratorString

def run(sceneFile, outfile, spp = 64):
    command = "pbrt"
    command += " " + sceneFile
    command += " --spp " + str(spp)
    command += " --outfile " + str(outfile)
    command += " > " + outfile.replace(".exr", ".log")
    print(command)
    os.system(command)