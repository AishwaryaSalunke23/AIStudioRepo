from interface.node_interface import Sink

class sink_aish(Sink):
    def run(self, Ain=None, Aout=None, argCfg=None):
        # Example: Sink node outputs data based on `argCfg` settings.
        # Customize this to save data to various destinations (e.g., blob storage, filesystem).
        # Description:
        # - `Ain`: Input accumulator holding processed data
        # - `Aout`: Output accumulator (not typically used in sink nodes, but passed for consistency)
        # - `argCfg`: Configuration dictionary specifying output settings, such as filesystem,blobstorage etc.
        
        output_type =  "console"  # Options: console, file, etc.
        acc_key = argCfg.get("data_key", "default_data_key")     
        data = Ain.read(acc_key)
        if data is None:
            raise ValueError(f"No data found in Ain for key:{acc_key}")
        
        # Output data based on specified output type
        if output_type == "console":
            print(f"FileSink received and output data: {data}")
