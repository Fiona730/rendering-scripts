import os, sys, importlib

def loadScenes(scenes_cfg):
    sys.path.append(os.path.dirname(scenes_cfg))
    scenesCfg = importlib.import_module(os.path.basename(scenes_cfg))
    if scenesCfg.scenesDirectory.startswith("$HERE$"):
        scenesCfg.scenesDirectory = scenesCfg.scenesDirectory.replace("$HERE$", os.path.dirname(scenes_cfg))
    return [scenesCfg.scenes, scenesCfg.scenesDirectory]