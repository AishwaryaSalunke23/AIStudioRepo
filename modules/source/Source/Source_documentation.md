# Source Node Documentation

The **`Source`** node is used to fetch files from different storage systems (e.g., **Blob Storage** or **Local Filesystem**) and make them available to downstream pipeline components.

## Usage

### 1. Input & Output

* **`Ain`** → Not required in this node (source only).
* **`Aout`** → Output object used to resolve the target path where files will be stored.
* **`argCfg`** → Configuration that specifies which storage instances to pull data from.

### 2. Configuration (`argCfg`)

Pass a dictionary with an `instances` list.
Each instance must define:

| Key                 | Required        | Description                                        |
| ------------------- | --------------- | -------------------------------------------------- |
| `instance_name`     | ✅               | Unique name for this storage instance.             |
| `storage_type`      | ✅               | `"blobstorage"` or `"filesystem"`.                 |
| `acc_key`           | ✅               | Key to map output paths in `Aout`.                 |
| `connection_params` | ✅ (blobstorage) | Connection details for the blob storage.           |
| `container_path`    | ✅ (blobstorage) | Path/container inside blob storage to fetch files. |
| `filesystem_path`   | ✅ (filesystem)  | Local directory path to fetch files from.          |

### 3. Example Configurations

#### a) Using Blob Storage

```python
argCfg = {
    "instances": [
        {
            "instance_name": "blob1",
            "storage_type": "blobstorage",
            "acc_key": "data_key",
            "connection_params": "",
            "container_path": "my-container/path"
        }
    ]
}
```

#### b) Using Local Filesystem

```python
argCfg = {
    "instances": [
        {
            "instance_name": "local1",
            "storage_type": "filesystem",
            "acc_key": "local_data",
            "filesystem_path": "/tmp/input_files"
        }
    ]
}
```

### 4. Running

```python
src = Source()
src.run(Ain=None, Aout=my_output, argCfg=argCfg)
```

### 5. Behavior

* **Blob Storage:**

  * Lists files in the given container path.
  * Downloads each file to the output path.

* **Filesystem:**

  * Reads all files from the given local directory.
  * Moves them to the output path.
  * Uploads them into the storage instance for tracking.

### 6. Errors You Might See

* Missing `instance_name` → `"Each storage instance must have an 'instance_name'."`
* Unsupported storage type → `"Unsupported storage type: ..."`
* Empty folders/paths → `"No files found in the specified path: ..."`

---
