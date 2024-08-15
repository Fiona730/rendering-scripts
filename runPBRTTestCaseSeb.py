import sys

import PBRTRenderer
import TestCaseHelper
import SceneHelper

import argparse

if __name__ == '__main__':


    print(sys.argv)
    
    if len(sys.argv) > 2:

        parser = argparse.ArgumentParser(description='Process some integers.')

        parser.add_argument('--testconfig', '-tc', type=str)
        parser.add_argument('--testcase', '-t', default='', type=str)
        parser.add_argument('--scene', '-s', default='', type=str)
        parser.add_argument('--scenesconfig', '-sc', default='', type=str)
        parser.add_argument('--variant', '-v', default='', type=str)
        parser.add_argument('--resultsdir', '-r', default='./results', type=str)
        parser.add_argument('--pbrtdir', '-m', default='', type=str)
        parser.add_argument('--spp', '-spp', default='64', type=int)
        parser.add_argument('--time', '-time', default='0', type=int)

        args = parser.parse_args(sys.argv[1:])
        print(args)
        
        # path to the Mitsuba installation
        pbrt_dir = args.pbrtdir
        # path to store the results
        results_dir = args.resultsdir

        spp = args.spp
        time = args.time

        # Loading the test case descriptions from a file
        [testCases, testCaseDescription] = TestCaseHelper.loadTestCases(args.testconfig)

        # Loading the scenes to run the test cases
        [scenes, scenes_dir] = SceneHelper.loadScenes(args.scenesconfig) 

        # Setup the Mitsuba renderer
        pbrt = PBRTRenderer.PBRTRenderer(pbrt_dir, results_dir, scenes_dir)
        foundScene = False
        for scenecfg in scenes:
            if scenecfg[0] == args.scene:
                foundScene = True
                scene = args.scene
                variant = args.variant
                resolution = scenecfg[2]
                #maxComponentValue = scenecfg[3]
                if args.testcase != "":
                    foundTestCase = False
                    for testCase in testCases:
                        if testCase.name == args.testcase:
                            foundTestCase = True
                            pbrt.runTestCase(scene, variant, resolution, testCase, spp = spp, time = time, stats=True)
                    if not foundTestCase:
                        print("ERROR testcase = \'" + args.testcase + "\' is NOT part of the test cases in \'" + args.testconfig + "\'\n")
                else:
                    for testCase in testCases:
                        pbrt.runTestCase(scene, variant, resolution, testCase, spp = spp, time = time, stats=True)
        if not foundScene:
                    print("ERROR scene = \'" + args.scene + "\' is NOT part of the scenes in \'" + args.scenesconfig + "\'\n")
    #else:
        #toneMap("../example/CoronaBenchmark_ref.exr", "../example/CoronaBenchmark_tm.png", 3)