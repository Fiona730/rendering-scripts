testCase_description = {
    "title" : "VSPG tests in PBRT",
    "short" : "Comparing path tracing with and without path guiding using PBRT's guidedvolpathvspg integrator.",
    "long" : "This test compares ..."
}

common_parameters = {
    "integrator": "guidedvolpathvspg",
    "maxdepth" : ["integer", 20],
    "minrrdepth" : ["integer", 20],
    "usenee" : ["bool", True],
    "surfaceguiding" : ["bool", False],
    "volumeguiding" : ["bool", False],
    "storeGuidingCache" : ["bool", False],
    "loadGuidingCache" : ["bool", False],
    "guidingCacheFileName" : ["string", ""],

    "rrguiding" : ["bool", False],
    "surfacerrguiding" : ["bool", False],
    "volumerrguiding" : ["bool", False],

    "vspprimaryguiding" : ["bool", False],
    "vspsecondaryguiding" : ["bool", False],
    "vspmisratio": ["float", 0.0],
    "vspcriterion" : ["integer", 0],
    "vspresampling" : ["bool", False],
    "productdistanceguiding" : ["bool", False],
    "Villemin" : ["bool", False],
    "collisionProbabilityBias" : ["bool", False],

    "storeVSPBuffer" : ["bool", False],
    "loadVSPBuffer" : ["bool", False],
    "vspBufferFileName" : ["string", ""],

    "storeTrBuffer" : ["bool", False],
    "loadTrBuffer" : ["bool", False],
    "trBufferFileName" : ["string", ""],

    "storeContributionEstimate" : ["bool", False],
    "loadContributionEstimate" : ["bool", False],
    "contributionEstimateFileName" : ["string", ""],
}

testCases = {
    "resampling_storeTr" : {
        "parameters" : {
            "vspresampling" : ["bool", True],

            "storeTrBuffer" : ["bool", True],
            "trBufferFileName" : ["string", "$SCENE_TR$-trBuffer-256spp.exr"],
        },
        "description" : "resampling for delta tracking and store transmittance estimate",
    },
}