scenesDirectory = "/home/kehan/Develop/openpgl-pbrt-v4-scenes/"

scenes = {
    "JungleRuins" : [
        [
            # "-volume-homo",
            "-volume-hetero",
        ], [1920, 1080], 
        100, # time
    ],

    "country-kitchen" : [
        [
            "-volume-hetero",
            # "-volume-hetero-maj5",
            # "-volume-hetero-maj10",
            # "-volume-hetero-maj20",
        ], [1920, 1080], 
        100, # time
    ],

    "landscape" : [
        [
            "",
        ], [1920, 1080], 
        100, # time
    ],

    "290skydemo" : [
        [
            # "-shallow", 
            # "-med", 
            #"-deep",
            "-deeper",
            # "-even-deeper"
        ], [1920,1080], 
        100, # time
    ],

    "earth" : [
        [
            "",
            # "-achromatic",
            # "-density0",
            # "-density3",
            # "-density5",
        ], [1920,1080], 
        120, # time
    ],

    "oriental-lantern" : [
        [
            "",
        ], [1920, 1080], 
        120, # time
    ],

    # "museum" : [
    #     [
    #         "-hetero",
    #     ], [1920, 1080], 
    #     300, # time
    # ],

    # "cornell-box-lightshaft" : [
    #     [
    #         "-hetero-scale0.3-g0",
    #     ], [1920, 1080], 
    #     120, # time
    # ],

    # "cornell-box-ball" : [
    #     [
    #         "-hetero",
    #     ], [1920, 1080], 
    #     300, # time
    # ],

    # "simple-disney-cloud" : [
    #     [
    #         # "-cornell-box-backlight",
    #         "-simple-surface-pointlight",
    #     ], [1920,1080], 
    #     120, # time
    # ],
}