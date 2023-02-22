# hardware configuration
# all pin numbers are corresponding to physical P1 connector!

config = {
    "hx711": {
        "CLK": 38,
        "DAT": 40,
        "ref": -1992 # calibration yields 100 g <-> readout 214500
    },
    "pca9685": {
        "freq": 60,
        "valvechannels": range(12),  # 0..11
        "valvepositions": [  # (open, closed)
            (120, 380),  # ch 0
            (140, 400),  # ch 1
            (330, 515),  # ch 2
            (600, 390),  # ch 3
            (180, 440),  # ch 4
            (130, 390),  # ch 5
            (210, 470),  # ch 6
            (150, 410),  # ch 7
            (120, 380),  # ch 8
            (600, 380),  # ch 9
            (290, 550),  # ch 10
            (150, 400)  # ch 11
        ],
        "fingerchannel": 12,
        "fingerpositions": (280, 430, 450),  # retracted, above bell, bell
        "lightpin": 16,
        "lightpwmchannel": 13,
        "lightpositions": (0, 500)
    },

    "pump": {
        "MOTOR": 32
    },

    "bomba":{
        "PUMP": 35
    },
     "ws2812": {
        "DIN": 12
    },
    "mqtt": {
        "SERVER": "localhost",
        "TOPICPREFIX": "Hector9000/Main/"
    }
}
