testCase_description = {
    "title" : "Time reference for guiding with guidedvolpath",
    "short" : "Comparing path tracing with and without path guiding using PBRT's guidedvolpath integrator.",
    "long" : "This test compares ..."
}

common_parameters = {
    "integrator": "volpath",
    "maxdepth" : ["integer", 20],
}

testCases = {
    "deltaTracking" : {
        "parameters" : {
        },
        "description" : "delta tracking",
    },
}