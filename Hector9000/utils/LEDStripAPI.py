#!/usr/bin/env python3
# -*- coding: utf8 -*-
##
#   LEDStripAPI.py       API interface class for Hector9000 LED Strip
#

import abc


def debugOut(name: str, value: str):
    print("=> %s: %d" % (name, value))


class LEDStripAPI(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def standart(self,type):
        pass

    @abc.abstractmethod
    def dosedrink(self,type):
        pass

    @abc.abstractmethod
    def servos(self,type):
        pass

