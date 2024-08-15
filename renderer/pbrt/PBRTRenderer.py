import os
import copy
import fnmatch

class PBRTRenderer:
    def __init__(self, pbrtInstallDir, resultsDir, buffersDir, scenesDir):
        self.pbrtInstallDir = pbrtInstallDir
        self.resultsDir = resultsDir
        self.buffersDir = buffersDir
        self.scenesDir = scenesDir
        
        LDLibPathConcat = self.pbrtInstallDir +"lib" + ":" + self.pbrtInstallDir +"lib64"
        if 'LD_LIBRARY_PATH' in os.environ:
            os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH'] + ":" + LDLibPathConcat
        else:
            os.environ['LD_LIBRARY_PATH'] = LDLibPathConcat

        PathConcat = self.pbrtInstallDir +"bin"
        if 'PATH' in os.environ:
            os.environ['PATH'] = os.environ['PATH'] + ":" + PathConcat
        else:
            os.environ['PATH'] = PathConcat

        makeSafeDir(self.resultsDir)
        makeSafeDir(self.buffersDir)

    def runTestCase(self, scene, sceneInfo, testCase, budgetIsSPP = True, stats = False, nthreads = 90):
        sceneVariant = sceneInfo[0]
        resolution = sceneInfo[1]
        budget = sceneInfo[2]

        budgetType = "spp" if budgetIsSPP else "time"

        for var in sceneVariant:
            sceneVariantConcat = str(scene + var)
            resultsSceneDir = os.path.join(self.resultsDir, sceneVariantConcat)
            makeSafeDir(resultsSceneDir)
            logDir = os.path.join(resultsSceneDir, "log")
            makeSafeDir(logDir)
            
            buffersSceneDir = os.path.join(self.buffersDir, sceneVariantConcat)
            if testCase.parameters.__contains__("storeVSPBuffer") \
                and testCase.parameters["storeVSPBuffer"][1] == True:
                makeSafeDir(buffersSceneDir)

            trBufferDir = os.path.join(self.scenesDir, scene, "transmittanceBuffer")
            if testCase.parameters.__contains__("storeTrBuffer") \
                and testCase.parameters["storeTrBuffer"][1] == True:
                makeSafeDir(trBufferDir)

            sceneFileName = f"{sceneVariantConcat}-{testCase.name}"
            outputFileName = f"{sceneFileName}-{budget}{budgetType}"
            outFile = os.path.join(resultsSceneDir, outputFileName + ".exr")
            logFile = os.path.join(logDir, outputFileName + ".log")

            if os.path.exists(outFile):
                print('WARNING: ', outFile, ' already exists')
            else:
                parameters = copy.deepcopy(testCase.parameters)
                for parameter in parameters:
                    # value = parameters[parameter][1]
                    # if isinstance(value, str):
                    #     if "$SCENE$" in value:
                    #         parameters[parameter][1] = value.replace("$SCENE$", os.path.join(self.resultsDir, sceneVariantConcat, sceneVariantConcat))

                    if parameter == "trBufferFileName":
                        value = parameters[parameter][1]
                        if "$SCENE_TR$" in value:
                            parameters[parameter][1] = value.replace("$SCENE_TR$", os.path.join(trBufferDir, f"{sceneVariantConcat}"))
                    elif parameter == "vspBufferFileName":
                        value = parameters[parameter][1]
                        if "$BUFFER$" in value:
                            parameters[parameter][1] = value.replace("$BUFFER$", os.path.join(buffersSceneDir, outputFileName + ".exr"))
                
                integratorString = extractIntegrator(parameters)
                filmString = extractFilm(resolution, parameters, outputFileName + ".exr")
                tmpTestCaseFileName = os.path.join(self.scenesDir, scene, sceneFileName + ".pbrt")
                
                tmpSceneFile = open(tmpTestCaseFileName,"w")
                tmpSceneFile.write(filmString)
                tmpSceneFile.write("\n")
                tmpSceneFile.write(integratorString)
                tmpSceneFile.write("\n")
                tmpSceneFile.write("Include \"" + sceneVariantConcat + "_auto.pbrt" + "\"")
                tmpSceneFile.write("\n")
                tmpSceneFile.close()

                command = "pbrt"
                command += " " + tmpTestCaseFileName
                if stats:
                    command += " --stats "
                command += " --nthreads " + str(nthreads)
                command += f" --seed 0 --{budgetType} {budget}"
                command += " --outfile " + str(outFile)
                command += " 2>&1 | tee " + str(logFile)
                
                while True:
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
    command += " --seed 0 --spp " + str(spp)
    command += " --outfile " + str(outfile)
    command += " > " + outfile.replace(".exr", ".log")
    print(command)
    os.system(command)