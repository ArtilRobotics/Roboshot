# hardware configuration
# all pin numbers are corresponding to physical P1 connector!

config = {
    "hx711": {
        "CLK": 38,
        "DAT": 40,
        "ref": -2461  # calibration yields 100 g <-> readout 214500
    },
    "pca9685": {
        "freq": 60,
        "valvechannels": range(12),  # 0..11
        "valvepositions": [  # (open, closed)
            (600, 390),  # ch 0
            (600, 390),  # ch 1
            (375, 515),  # ch 2
            (600, 390),  # ch 3
            (600, 450),  # ch 4
            (600, 390),  # ch 5
            (650, 470),  # ch 6
            (600, 410),  # ch 7
            (600, 390),  # ch 8
            (600, 390),  # ch 9
            (390, 600),  # ch 10
            (600, 380)  # ch 11
        ],
        "fingerchannel": 12,
        "fingerpositions": (280, 430, 450),  # retracted, above bell, bell
        "lightpin": 22,
        "lightpwmchannel": 13,
        "lightpositions": (0, 500)
    },

    "pump": {
        "MOTOR": 18
    },

     "ws2812": {
        "DIN": 12
    },
    "mqtt": {
        "SERVER": "localhost",
        "TOPICPREFIX": "Hector9000/Main/"
    }
}
