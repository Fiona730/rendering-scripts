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
}

testCases = {
    "dir_guiding" : {
        "parameters" : {
            "surfaceguiding" : ["bool", True],
            "volumeguiding" : ["bool", True],
        },
        "description" : "dir_guiding",
    }
}