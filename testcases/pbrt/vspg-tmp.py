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
    "deltaTracking" : {
        "parameters" : {
            "surfaceguiding" : ["bool", False],
            "volumeguiding" : ["bool", False],

            "storeVSPBuffer" : ["bool", False],
        },
        "description" : "delta tracking",
    },

    # "deltaTracking_resampling" : {
    #     "parameters" : {
    #         "vspresampling" : ["bool", True],
    #     },
    #     "description" : "delta tracking via resampling",
    # },

    "dirGuiding" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],

            "storeVSPBuffer" : ["bool", False],
        },
        "description" : "directional guiding without storing the vsp buffer",
    },

    # "dirGuiding_storeBuffer" : {
    #     "parameters" : {
    #         "surfaceguiding" : ["bool", True],
    #         "volumeguiding" : ["bool", True],

    #         "storeVSPBuffer" : ["bool", True],
    #         "vspBufferFileName" : ["string", "$BUFFER$"],
    #     },
    #     "description" : "directional guiding + store vsp buffer",
    # },

    # "dirGuiding_primaryVSPG_resampling_0.75MIS_contrib" : {
    #     "parameters" : {
    #         "surfaceguiding" : ["bool", True],
    #         "volumeguiding" : ["bool", True],
    #         "vspprimaryguiding" : ["bool", True],
    #         "vspmisratio": ["float", 0.75],
    #         "vspcriterion" : ["integer", 0],
    #         "vspresampling" : ["bool", True],
    #     },
    #     "description" : "directional guiding + primary ray VSPG resampling (0.75MIS, contribution-based)",
    # },

    # "dirGuiding_allVSPG_VilleminNaive_0.75MIS_contrib" : {
    #     "parameters" : {
    #         "surfaceguiding" : ["bool", True],
    #         "volumeguiding" : ["bool", True],
    #         "vspprimaryguiding" : ["bool", True],
    #         "vspsecondaryguiding" : ["bool", True],
    #         "vspmisratio": ["float", 0.75],
    #         "vspcriterion" : ["integer", 0],
    #         "Villemin" : ["bool", True],

    #         "storeVSPBuffer" : ["bool", True],
    #         "vspBufferFileName" : ["string", "$BUFFER$"],
    #     },
    #     "description" : "directional guiding + all ray VSPG Villemin (0.75MIS, contribution-based)",
    # },

    # "dirGuiding_allVSPG_VilleminCollBias_0.75MIS_contrib" : {
    #     "parameters" : {
    #         "surfaceguiding" : ["bool", True],
    #         "volumeguiding" : ["bool", True],
    #         "vspprimaryguiding" : ["bool", True],
    #         "vspsecondaryguiding" : ["bool", True],
    #         "vspmisratio": ["float", 0.75],
    #         "vspcriterion" : ["integer", 0],
    #         "Villemin" : ["bool", True],
    #         "collisionProbabilityBias" : ["bool", True],

    #         "loadTrBuffer" : ["bool", True],
    #         "trBufferFileName" : ["string", "$SCENE_TR$-trBuffer-256spp.exr"],

    #         "storeVSPBuffer" : ["bool", True],
    #         "vspBufferFileName" : ["string", "$BUFFER$"],
    #     },
    #     "description" : "directional guiding + all ray VSPG Villemin CollisionProbabilityBias (0.75MIS, contribution-based)",
    # },

    # "dirGuiding_allVSPG_VilleminCollBias_0.75MIS_var" : {
    #     "parameters" : {
    #         "surfaceguiding" : ["bool", True],
    #         "volumeguiding" : ["bool", True],
    #         "vspprimaryguiding" : ["bool", True],
    #         "vspsecondaryguiding" : ["bool", True],
    #         "vspmisratio": ["float", 0.75],
    #         "vspcriterion" : ["integer", 1],
    #         "Villemin" : ["bool", True],
    #         "collisionProbabilityBias" : ["bool", True],

    #         "loadTrBuffer" : ["bool", True],
    #         "trBufferFileName" : ["string", "$SCENE_TR$-trBuffer-256spp.exr"],

    #         "storeVSPBuffer" : ["bool", True],
    #         "vspBufferFileName" : ["string", "$BUFFER$"],
    #     },
    #     "description" : "directional guiding + all ray VSPG Villemin CollisionProbabilityBias (0.75MIS, variance-based)",
    # },

    # "dirGuiding_primaryVSPG_resampling_0.75MIS_contrib" : {
    #     "parameters" : {
    #         "surfaceguiding" : ["bool", True],
    #         "volumeguiding" : ["bool", True],
    #         "vspprimaryguiding" : ["bool", True],
    #         "vspsecondaryguiding" : ["bool", False],
    #         "vspmisratio": ["float", 0.75],
    #         "vspcriterion" : ["integer", 0],
    #         "vspresampling" : ["bool", True],

    #         "storeVSPBuffer" : ["bool", True],
    #         "vspBufferFileName" : ["string", "$BUFFER$"],
    #     },
    #     "description" : "directional guiding + primary ray VSPG resampling (0.75MIS, contribution-based)",
    # },

    # "dirGuiding_allVSPG_resampling_0.75MIS_contrib" : {
    #     "parameters" : {
    #         "surfaceguiding" : ["bool", True],
    #         "volumeguiding" : ["bool", True],
    #         "vspprimaryguiding" : ["bool", True],
    #         "vspsecondaryguiding" : ["bool", True],
    #         "vspmisratio": ["float", 0.75],
    #         "vspcriterion" : ["integer", 0],
    #         "vspresampling" : ["bool", True],

    #         "storeVSPBuffer" : ["bool", True],
    #         "vspBufferFileName" : ["string", "$BUFFER$"],
    #     },
    #     "description" : "directional guiding + all ray VSPG resampling (0.75MIS, contribution-based)",
    # },

    # "dirGuiding_allVSPG_resampling_0.75MIS_var" : {
    #     "parameters" : {
    #         "surfaceguiding" : ["bool", True],
    #         "volumeguiding" : ["bool", True],
    #         "vspprimaryguiding" : ["bool", True],
    #         "vspsecondaryguiding" : ["bool", True],
    #         "vspmisratio": ["float", 0.75],
    #         "vspcriterion" : ["integer", 1],
    #         "vspresampling" : ["bool", True],

    #         "storeVSPBuffer" : ["bool", True],
    #         "vspBufferFileName" : ["string", "$BUFFER$"],
    #     },
    #     "description" : "directional guiding + all ray VSPG resampling (0.75MIS, variance-based)",
    # },

    # "dirGuiding_allVSPG_productSampling_0.75MIS_var" : {
    #     "parameters" : {
    #         "surfaceguiding" : ["bool", True],
    #         "volumeguiding" : ["bool", True],
    #         "vspprimaryguiding" : ["bool", True],
    #         "vspsecondaryguiding" : ["bool", True],
    #         "vspmisratio": ["float", 0.75],
    #         "vspcriterion" : ["integer", 1],
    #         "vspresampling" : ["bool", True],
    #         "productdistanceguiding" : ["bool", True],

    #         "storeVSPBuffer" : ["bool", True],
    #         "vspBufferFileName" : ["string", "$BUFFER$"],
    #     },
    #     "description" : "directional guiding + all ray VSPG resampling & product distance guiding (0.75MIS, variance-based)",
    # },
}