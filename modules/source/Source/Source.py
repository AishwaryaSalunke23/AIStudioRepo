from interface.node_interface import Src
import os
import shutil
from ai_forge_common.DataManagement.data_manager.datamanager import DataManager
from plib.utilities.env import getEnvCfg

cfg = getEnvCfg()

class Source(Src):
    def run(self, Ain=None, Aout=None, argCfg=None):
        # Initialize DataManager for this instance
        manager = DataManager(cfg)
        
        for config in argCfg.get("instances", []):
            instance_name = config.get("instance_name")
            storage_type = config.get("storage_type")
            acc_key = config.get("acc_key")
            
            if not instance_name:
                raise ValueError("Each storage instance must have an 'instance_name'.")
            
            if storage_type == "blobstorage":
                connection_params = config.get("connection_params")
                container_path = config.get("container_path")
                
                storage_instance = manager.create_storage_instance(storage_type, instance_name, connection_params, True)
                download_path = Aout.get_path(acc_key)
                
                blob_names = storage_instance.list(container_path)
                if not blob_names:
                    raise ValueError(f"No files found in the specified path: {container_path}")
                
                for blob_name in blob_names:
                    file_object = storage_instance.get(f"{container_path}/{blob_name}")
                    file_object.download_path = download_path
                    with file_object.open(file_object.object_id, 'r') as file_obj:
                        pass  # Placeholder for file processing logic
                
                print(f"Source node processed blob storage data for instance: {instance_name}")
            
            elif storage_type == "filesystem":
                filesystem_path = config.get("filesystem_path")
                
                if not os.path.exists(filesystem_path):
                    raise ValueError(f"Local directory does not exist: {filesystem_path}")
                
                container_path = os.path.basename(filesystem_path)
                connection_params = os.path.dirname(filesystem_path)
                storage_instance = manager.create_storage_instance(storage_type, instance_name, connection_params, True)
                
                download_path = Aout.get_path(acc_key)
                os.makedirs(download_path, exist_ok=True)
                
                files = os.listdir(filesystem_path)
                if not files:
                    raise ValueError(f"No files found in the specified path: {filesystem_path}")
                
                for file_name in files:
                    file_path = os.path.join(filesystem_path, file_name)
                    if not os.path.isfile(file_path):
                        continue
                    
                    dest_path = os.path.join(download_path, file_name)
                    shutil.move(file_path, dest_path)
                    
                    file_object = storage_instance.get(os.path.join(container_path, file_name))
                    with file_object.open(file_object.object_id, 'wb') as file_obj:
                        with open(dest_path, "rb") as local_file:
                            file_obj.write(local_file.read())
                    
                    print(f"Moved and uploaded file: {file_name}")
                
                print(f"Source node processed filesystem data for instance: {instance_name}")
            else:
                raise ValueError(f"Unsupported storage type: {storage_type}")