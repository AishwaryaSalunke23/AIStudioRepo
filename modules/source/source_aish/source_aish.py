import random
from interface.node_interface import Src

class source_aish(Src):
    def run(self, Ain=None, Aout=None, argCfg=None):
        # Example: generates a random number based on `argCfg` settings and stores it in Output Accumulator (Aout)
        # Customize to read data from various sources (e.g., blob storage, filesystem, datastream, etc.) and place it in Aout.
        # Description:
        # - `Ain`: Input accumulator (not typically used in source nodes, but passed for consistency)
        # - `Aout`: Output accumulator where generated data is stored
        # - `argCfg`: Configuration dictionary containing parameters specific to the node's operation
        
        acc_key =  argCfg.get("data_key", "default_data_key")
        
        # Generate random data - range can be configured in argCfg
        data_min = argCfg.get("data_min", 1)
        data_max = argCfg.get("data_max", 100)
        random_number = random.randint(data_min, data_max)
        
        # Store generated data in the output accumulator with configured key
        Aout.write(acc_key, random_number)
        print(f"Source node generated and stored data: {random_number} in {acc_key}")