import renderer.blender.BlenderRenderer as BlenderRenderer
import utils.TestCaseHelper as TestCaseHelper
import utils.SceneHelper as SceneHelper

import utils.ResultsViewer as ResultsViewer

# path to the Blender installation (e.g., folder or a soft link to it)
blender_dir = "./blender-renderer/"

# path to store the results
resultsDir = "./blender-results/guiding"
# path to store the post-processed results and the HTML viewer
viewerOutputDir = "./blender-viewers/guiding"

# Loading the test case descriptions from a file
testCases = TestCaseHelper.loadTestCases("examples/blender/testcases/guiding")
testCaseDescription = TestCaseHelper.loadTestCaseDescription("examples/blender/testcases/guiding")

# Loading the scenes to run the test cases (e.g., blender-scenes can be a folder or a soft link to it)
[scenes, scenesDir] = SceneHelper.loadScenes("blender-scenes/scenesconfig") 

# Setup the Blender renderer
blender = BlenderRenderer.BlenderRenderer(blender_dir, resultsDir, scenesDir)

#for each scene and each scene variant
for scene, sceneVariants, resolution in scenes:
    for variant in sceneVariants:
        #run each test case defined in the test cases file
        for testCase in testCases:    
            blender.runTestCase(scene, variant, resolution, testCase, spp = 16, deleteTestCaseJSON=True)

#after running all test cases for all scenes prepare the results in an interactive HTML viewer 
viewer = ResultsViewer.ResultsViewer("./utils/webviewer")
viewer.generateHTMLS(viewerOutputDir, resultsDir, scenesDir, scenes, testCaseDescription, testCases, showReference=False, perScene=False)

