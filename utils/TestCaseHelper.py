import os, sys, importlib

class TestCase:
    def __init__(self, name, data, common_parameters):
        self.name = name
        self.parameters = mergeParameters(common_parameters, data["parameters"])
        self.description = data["description"]
        self.skipViewer = False
        if data.__contains__("skipViewer"):
            self.skipViewer = data["skipViewer"]

def loadTestCases(testCases):
    testCases = []
    sys.path.append(os.path.dirname(testCases))
    tcs = importlib.import_module(os.path.basename(testCases))
    
    for testCase in tcs.testCases: 
        testCases.append(TestCase(testCase, tcs.testCases[testCase], tcs.common_parameters))
    return testCases, tcs.testCase_description

def mergeParameters(common_parameters, testCase_parameters):
    parameters = testCase_parameters
    for cparameter in common_parameters:
        if not parameters.__contains__(cparameter):
            parameters[cparameter] = common_parameters[cparameter]
    return parameters