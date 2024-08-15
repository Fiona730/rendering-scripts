testCase_description = {
    "title" : "Time reference for guiding with guidedvolpath",
    "short" : "Comparing path tracing with and without path guiding using PBRT's guidedvolpath integrator.",
    "long" : "This test compares ..."
}

common_parameters = {
    "integrator": "guidedvolpath",
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
}

testCases = {
    "deltaTracking" : {
        "parameters" : {
            "surfaceguiding" : ["bool", False],
            "volumeguiding" : ["bool", False],
        },
        "description" : "delta tracking",
    },

    "dirGuiding" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
        },
        "description" : "directional guiding",
    },
}