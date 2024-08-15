import renderer.pbrt.PBRTRenderer as PBRTRenderer
import utils.TestCaseHelper as TestCaseHelper
import utils.SceneHelper as SceneHelper

import utils.ResultsViewer as ResultsViewer

# path to the PBRT installation
pbrt_dir = "/home/kehan/Develop/pbrt-v4-Distance-Guiding-guidedrr-vspg/install/"
# path to store the results
results_dir = "./pbrt-results-seb/volumeguiding3"

viewer_output_dir = "./pbrt-viewers-seb/volumeguiding3"

# Loading the test case descriptions from a file
[testCases, testCaseDescription] = TestCaseHelper.loadTestCases("testcases/pbrt/volumeguiding")

# Loading the scenes to run the test cases
[scenes, scenes_dir] = SceneHelper.loadScenes("/home/kehan/Develop/openpgl-pbrt-v4-scenes-seb/scenesconfig") 

# Setup the PBRT renderer
pbrt = PBRTRenderer.PBRTRenderer(pbrt_dir, results_dir, "./arggghhh_WHY", scenes_dir)

for scene, sceneInfo in scenes.items():
    print(testCases)
    for testCase in testCases:    
        print(testCase)
        pbrt.runTestCase(scene, sceneInfo, testCase, budgetIsSPP = True, stats = True)

#after running all test cases for all scenes prepare the results in an interactive HTML viewer 
viewer = ResultsViewer.ResultsViewer("./utils/webviewer")
viewer.generateHTMLS(viewer_output_dir, results_dir, scenes_dir, scenes, testCaseDescription, testCases, showReference=True, perScene=False, errors=["PosNeg","relMSE"])