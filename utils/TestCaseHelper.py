import os, sys, importlib

class TestCase:
    def __init__(self, name, data, common_parameters):
        self.name = name
        self.parameters = mergeParameters(common_parameters, data["parameters"])
        self.description = data["description"]
        self.skipViewer = False
        if data.__contains__("skipViewer"):
            self.skipViewer = data["skipViewer"]

def loadTestCases(testCasesFile):
    testCasesList = []
    sys.path.append(os.path.dirname(testCasesFile))
    tcs = importlib.import_module(os.path.basename(testCasesFile))
    
    for testCase in tcs.testCases: 
        testCasesList.append(TestCase(testCase, tcs.testCases[testCase], tcs.common_parameters))
    return testCasesList, tcs.testCase_description

def mergeParameters(common_parameters, testCase_parameters):
    parameters = testCase_parameters
    for cparameter in common_parameters:
        if not parameters.__contains__(cparameter):
            parameters[cparameter] = common_parameters[cparameter]
    return parameters