import config
import numpy as np
rnd = np.random
REQUEST_INIT = config.REQUEST_INIT  # Default configs
REQUEST_SAMPLE = config.REQUEST_SAMPLE  # Sample requests


class Request:
    def __init__(self, INPUT):
        # Building INPUT
        self.INPUT = {}
        for key in REQUEST_INIT.keys():
            if ("SAMPLE" in INPUT.keys() and INPUT["SAMPLE"] != ""):
                self.INPUT[key] = REQUEST_SAMPLE[INPUT["SAMPLE"]][key]
            else:
                self.INPUT[key] = INPUT[key] if key in INPUT else REQUEST_INIT[key]
        # Defining base variables
        self.SEED = self.INPUT["SEED"]
        self.NUM_REQUESTS = self.INPUT["NUM_REQUESTS"]
        self.FIRST_TIER_NODES = self.INPUT["FIRST_TIER_NODES"]
        self.DC_CAPACITY_REQUIREMENT_MU = self.INPUT["DC_CAPACITY_REQUIREMENT_MU"]
        self.DC_CAPACITY_REQUIREMENT_SIGMA = self.INPUT["DC_CAPACITY_REQUIREMENT_SIGMA"]
        self.BW_REQUIREMENT_MU = self.INPUT["BW_REQUIREMENT_MU"]
        self.BW_REQUIREMENT_SIGMA = self.INPUT["BW_REQUIREMENT_SIGMA"]
        self.DLY_REQUIREMENT_MU = self.INPUT["DLY_REQUIREMENT_MU"]
        self.DLY_REQUIREMENT_SIGMA = self.INPUT["DLY_REQUIREMENT_SIGMA"]
        self.BURST_SIZE_MU = self.INPUT["BURST_SIZE_MU"]
        self.BURST_SIZE_SIGMA = self.INPUT["BURST_SIZE_SIGMA"]
        self.SAMPLE = self.INPUT["SAMPLE"]
        # Defining complementary variables
        rnd.seed(self.SEED)
        self.REQUESTS = np.arange(self.NUM_REQUESTS)
        self.ENTRY_NODES = self.initialize_entry_nodes()
        self.DC_CAPACITY_REQUIREMENTS = self.initialize_capacity_requirements()
        self.BW_REQUIREMENTS = self.initialize_bw_requirements()
        self.DELAY_REQUIREMENTS = self.initialize_delay_requirements()
        self.BURST_SIZES = self.initialize_burst_sizes()

    def initialize_entry_nodes(self):
        if self.SAMPLE == "":
            return np.random.choice(self.FIRST_TIER_NODES, size=self.NUM_REQUESTS)
        else:
            return REQUEST_SAMPLE[self.SAMPLE]["ENTRY_NODES"]

    def initialize_capacity_requirements(self):
        mu = self.DC_CAPACITY_REQUIREMENT_MU
        sigma = self.DC_CAPACITY_REQUIREMENT_SIGMA

        dc_capacity_requirements = np.array([np.random.normal(mu, sigma, 1)[0].round(0).astype(int) for r in self.REQUESTS])

        return dc_capacity_requirements

    def initialize_bw_requirements(self):
        mu = self.BW_REQUIREMENT_MU
        sigma = self.BW_REQUIREMENT_SIGMA

        bw_requirements = np.array([np.random.normal(mu, sigma, 1)[0].round(0).astype(int) for r in self.REQUESTS])

        return bw_requirements

    def initialize_delay_requirements(self):
        mu = self.DLY_REQUIREMENT_MU
        sigma = self.DLY_REQUIREMENT_SIGMA

        delay_requirements = np.array([np.random.normal(mu, sigma, 1)[0].round(0).astype(int) for r in self.REQUESTS])

        return delay_requirements

    def initialize_burst_sizes(self):
        mu = self.BURST_SIZE_MU
        sigma = self.BURST_SIZE_SIGMA

        burst_sizes = np.array([np.random.normal(mu, sigma, 1)[0].round(0).astype(int) for r in self.REQUESTS])

        return burst_sizes

    def get_state(self):
        request_features = []

        for r in self.REQUESTS:
            request_feature = []
            request_feature.append(self.ENTRY_NODES[r])
            request_feature.append(self.DC_CAPACITY_REQUIREMENTS[r])
            request_feature.append(self.BW_REQUIREMENTS[r])
            request_feature.append(self.DELAY_REQUIREMENTS[r])
            request_features.append(request_feature)

        return request_features
