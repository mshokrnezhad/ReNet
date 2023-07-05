import config
import numpy as np
rnd = np.random
SERVICE_INIT = config.SERVICE_INIT  # Default configs
SERVICE_SAMPLE = config.SERVICE_SAMPLE  # Sample services


class Service:
    def __init__(self, INPUT):
        # Building INPUT
        self.INPUT = {}
        for key in SERVICE_INIT.keys():
            if ("SAMPLE" in INPUT.keys() and INPUT["SAMPLE"] != ""):
                self.INPUT[key] = SERVICE_SAMPLE[INPUT["SAMPLE"]][key]
            else:
                self.INPUT[key] = INPUT[key] if key in INPUT else SERVICE_INIT[key]
        # Defining base variables
        self.SEED = self.INPUT["SEED"]
        self.NUM_SERVICES = self.INPUT["NUM_SERVICES"]
        # Defining complementary variables
        rnd.seed(self.SEED)
        self.SERVICES = np.arange(self.NUM_SERVICES)
