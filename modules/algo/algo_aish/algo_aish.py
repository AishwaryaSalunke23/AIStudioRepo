from interface.node_interface import Algo

class algo_aish(Algo):
    def run(self, Ain=None, Aout=None, argCfg=None):
        # Example: Algo node performs a mathematical operation on Ain data
        # Customize to apply specific algorithms on input data from Ain, process it, and store it in Aout.
        # Description:
        # - `Ain`: Input accumulator containing data to be processed
        # - `Aout`: Output accumulator where processed data will be stored
        # - `argCfg`: Configuration dictionary specifying algorithmic operations
        
        acc_key = argCfg.get("data_key", "default_data_key")
        # Get data from Ain (it should have the necessary data)
        data = Ain.read(acc_key)
        if data is None:
            raise ValueError(f"No data found in Ain for key: {acc_key}")
 
        # Perform the operation
        processed_data = data ** 2  # Example operation: square
 
        # Store the processed data in Aout
        acc_key = argCfg.get("data_key", "default_data_key")
        Aout.write(acc_key, processed_data)
        print(f"Algo node processed data (square): {data} to {processed_data}")
