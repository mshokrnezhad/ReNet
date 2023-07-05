REQUEST_INIT = {  # The default configuration of the NETWORK class.
    "NUM_REQUESTS": 10,
    "FIRST_TIER_NODES": [0, 1],
    "SEED": 4,
    "DC_CAPACITY_REQUIREMENT_MU": 8,  # Supposing that DC_CAPACITY_REQUIREMENT has a normal distribution, DC_CAPACITY_REQUIREMENT_MU is the mean.
    "DC_CAPACITY_REQUIREMENT_SIGMA": 2,  # Representing the standard deviation of DC_CAPACITY_REQUIREMENT supposing it has a normal distribution.
    "BW_REQUIREMENT_MU": 3,  # Supposing that BW_REQUIREMENT has a normal distribution, BW_REQUIREMENT_MU is the mean.
    "BW_REQUIREMENT_SIGMA": 1,  # Representing the standard deviation of BW_REQUIREMENT supposing it has a normal distribution.
    "DLY_REQUIREMENT_MU": 10,  # Supposing that DLY_REQUIREMENT has a normal distribution, DLY_REQUIREMENT_MU is the mean.
    "DLY_REQUIREMENT_SIGMA": 1,  # Representing the standard deviation of DLY_REQUIREMENT supposing it has a normal distribution.
    "BURST_SIZE_MU": 2,  # Supposing that BURST_SIZE has a normal distribution, BURST_SIZE_MU is the mean.
    "BURST_SIZE_SIGMA": 1,  # Representing the standard deviation of BURST_SIZE supposing it has a normal distribution.
    "SAMPLE": ""  # Representing the sample code. It should be one of the objects of REQUEST_SAMPLE.
}

REQUEST_SAMPLE = {
    "REQ1": {
        "NUM_REQUESTS": 10,
        "FIRST_TIER_NODES": [0],
        "SEED": 4,
        "DC_CAPACITY_REQUIREMENT_MU": 8,
        "DC_CAPACITY_REQUIREMENT_SIGMA": 2,
        "BW_REQUIREMENT_MU": 3,
        "BW_REQUIREMENT_SIGMA": 1,
        "DLY_REQUIREMENT_MU": 10,
        "DLY_REQUIREMENT_SIGMA": 1,
        "BURST_SIZE_MU": 2,
        "BURST_SIZE_SIGMA": 1,
        "SAMPLE": "REQ1",
        "ENTRY_NODES": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
}
