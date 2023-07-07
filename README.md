# ReNet
A network environment to test reinforcement learning techniques.

The environment includes:

- NETWORK:

    - CLASS: ./network/NETWORK.py

    - Implemented following https://ieeexplore.ieee.org/abstract/document/10001109/

    - How to run: ./main_network.py

    - How to config: ./network/config.py

- REQUEST:

    - CLASS: ./request/REQUEST.py

    - How to run: ./main_request.py

    - How to config: ./request/config.py

- SERVICE: 

    - CLASS: ./service/SERVICE.py

    - How to run: ./main_service.py

    - How to config: ./service/config.py

- ENVIRONMENT: The primary environmental class. You can get the state, update it by passing action, and reset the environment from here. It contains NETWORK, SERVICE, and REQUEST.

    - CLASS: ./service/ENVIRONMENT.py

    - How to run: ./main_environment.py
