import renderer.pbrt.PBRTRenderer as PBRTRenderer
import utils.TestCaseHelper as TestCaseHelper
import utils.SceneHelper as SceneHelper
# import utils.ResultsViewer as ResultsViewer

import argparse

BUDGET_IS_SPP = True
BUDGET_STRING = "equalSPP" if BUDGET_IS_SPP else "equalTime"
RUN_NAME = "firstRun"
TEST_CASE = "vspg-main"
DIR_NAME = f"0805-{TEST_CASE}-{RUN_NAME}-{BUDGET_STRING}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scene', '-t', default='', type=str)
    parser.add_argument('--render', action='store_true')
    parser.add_argument('--no-render', dest='render', action='store_false')
    parser.set_defaults(render=True)
    parser.add_argument('--viewer', action='store_true')
    parser.add_argument('--no-viewer', dest='viewer', action='store_false')
    parser.set_defaults(viewer=True)
    args = parser.parse_args()

    # path to the PBRT installation (e.g., folder or a soft link to it)
    # pbrtDir = "./pbrt-renderer/"
    pbrtDir = "/home/kehan/Develop/pbrt-v4-Distance-Guiding-guidedrr-vspg/install/"
    # path to store the results
    resultsDir = f"./pbrt-results/{DIR_NAME}"
    # path to store the AOV buffers
    buffersDir = f"./pbrt-buffers/{DIR_NAME}"
    # path to store the post-processed results and the HTML viewer
    viewerOutputDir = f"./pbrt-viewers/{DIR_NAME}"

    # Loading the test case descriptions from a file
    testCases, testCaseDescription = TestCaseHelper.loadTestCases(f"testcases/pbrt/{TEST_CASE}")

    # Loading the scenes to run the test cases (e.g., pbrt-scenes can be a folder or a soft link to it)
    [scenes, scenesDir] = SceneHelper.loadScenes("scenes/pbrt/scenesconfig-equalspp") 

    if args.render:
        # Setup the PBRT renderer
        pbrt = PBRTRenderer.PBRTRenderer(pbrtDir, resultsDir, buffersDir, scenesDir)

        if args.scene != "":
            if not args.scene in scenes.keys():
                print(f"ERROR scene = \'{args.scene}\' is NOT part of the scenes.")
            
            scene = args.scene
            sceneInfo = scenes[scene]
            for testCase in testCases:
                pbrt.runTestCase(scene, sceneInfo, testCase, budgetIsSPP=BUDGET_IS_SPP, stats=True)

        else:
            #for each scene and each scene variant
            for scene, sceneInfo in scenes.items():
                #run each test case defined in the test cases file
                for testCase in testCases:
                    pbrt.runTestCase(scene, sceneInfo, testCase, budgetIsSPP=BUDGET_IS_SPP, stats=True)

    # if args.viewer and args.scene == "":
    #     #after running all test cases for all scenes prepare the results in an interactive HTML viewer 
    #     viewer = ResultsViewer.ResultsViewer("./utils/webviewer")
    #     viewer.generateHTMLS(viewerOutputDir, resultsDir, scenesDir, scenes, testCaseDescription, testCases, showReference=False, perScene=False)