scenesDirectory = "/home/kehan/Develop/openpgl-pbrt-v4-scenes/"

scenes = {
    "JungleRuins" : [
        [
            # "-volume-homo",
            "-volume-hetero",
        ], [1920, 1080], 
        64, # spp
    ],

    "country-kitchen" : [
        [
            "-volume-hetero",
            # "-volume-hetero-maj5",
            # "-volume-hetero-maj10",
            # "-volume-hetero-maj20",
        ], [1920, 1080], 
        64, # spp
    ],

    "landscape" : [
        [
            "",
        ], [1920, 1080], 
        64, # spp
    ],

    "290skydemo" : [
        [
            # "-shallow", 
            # "-med", 
            #"-deep",
            "-deeper",
            # "-even-deeper"
        ], [1920,1080], 
        64, # spp
    ],

    "earth" : [
        [
            "",
            # "-achromatic",
            # "-density0",
            # "-density3",
            # "-density5",
        ], [1920,1080], 
        16, # spp
    ],

    "oriental-lantern" : [
        [
            "",
        ], [1920, 1080], 
        16, # spp
    ],

    # "museum" : [
    #     [
    #         "-hetero",
    #     ], [1920, 1080], 
    #     64, # spp
    # ],

    # "cornell-box-lightshaft" : [
    #     [
    #         "-hetero-scale0.3-g0",
    #     ], [1920, 1080], 
    #     16, # spp
    # ],

    # "cornell-box-ball" : [
    #     [
    #         "-hetero",
    #     ], [1920, 1080], 
    #     64, # spp
    # ],

    # "simple-disney-cloud" : [
    #     [
    #         # "-cornell-box-backlight",
    #         "-simple-surface-pointlight",
    #     ], [1920,1080], 
    #     16, # spp
    # ],
}