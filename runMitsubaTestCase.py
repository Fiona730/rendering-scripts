import renderer.mitsuba.MitsubaRenderer as MitsubaRenderer
import utils.TestCaseHelper as TestCaseHelper
import utils.SceneHelper as SceneHelper

import utils.ResultsViewer as ResultsViewer

# path to the Mitsuba installation (dist) folder (e.g., folder or a soft link to it)
mts_dir = "./mitsuba-renderer/"
# optional: path to the Mitsuba dependency folder (e.g., folder or a soft link to it)
mts_deps = "./mitsuba-deps/"

# path to store the results
resultsDir = "./mitsuba-results/guiding"
# path to store the post-processed results and the HTML viewer
viewerOutputDir = "./mitsuba-viewers/guiding"

# Loading the test case descriptions from a file
testCases = TestCaseHelper.loadTestCases("examples/mitsuba/testcases/references")
testCaseDescription = TestCaseHelper.loadTestCaseDescription("examples/mitsuba/testcases/references")

# Loading the scenes to run the test cases (e.g., pbrt-scenes can be a folder or a soft link to it)
[scenes, scenesDir] = SceneHelper.loadScenes("mitsuba-scenes/scenesconfig") 

# Setup the Mitsuba renderer
mts = MitsubaRenderer.MitsubaRenderer(mts_dir, resultsDir, scenesDir, deps_dir = mts_deps)

#for each scene and each scene variant
for scene, sceneVariants, resolution in scenes:
    for variant in sceneVariants:
        #run each test case defined in the test cases file
        for testCase in testCases:    
            mts.runTestCase(scene, variant, resolution, testCase, spp = 16)

#after running all test cases for all scenes prepare the results in an interactive HTML viewer 
viewer = ResultsViewer.ResultsViewer("./utils/webviewer")
viewer.generateHTMLS(viewerOutputDir, resultsDir, scenesDir, scenes, testCaseDescription, testCases, showReference=False, perScene=False)