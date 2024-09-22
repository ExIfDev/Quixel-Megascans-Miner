import os
import time
import requests


token = "Bearer <YOUR_TOKEN>"  # Replace with your token

def read_index(index_path):
    index = {}
    with open(index_path, 'r') as file:
        for line in file:
            asset_id = line.split()[0]
            owned = '[OWNED]' in line
            index[asset_id] = owned
    return index

def update_index(index_path, index):
    with open(index_path, 'w') as file:
        for asset_id, owned in index.items():
            file.write(f"{asset_id} {'[OWNED]' if owned else ''}\n")
    print(f"Index updated in {index_path}")

def acquire_non_owned_assets_from_index(index, index_path, timeout_seconds=4):
    total_assets = len(index)
    acquired_count = 0

    for asset_id, owned in index.items():
        acquired_count += 1
        progress = (acquired_count / total_assets) * 100  
        print(f"Progress: {progress:.2f}% [{acquired_count} out of {total_assets}]")

        if not owned:  
            try:
                print(f"Acquiring asset {asset_id}...")
                
                success = acquire_asset_with_timeout(asset_id, index, timeout_seconds)

                if success:
                   
                    update_index(index_path, index)
                else:
                    print(f"Retrying acquisition for asset {asset_id}...")
                    success = acquire_asset_with_timeout(asset_id, index, timeout_seconds)

                if not success:
                    print(f"Skipping asset {asset_id} after two failed attempts. Api didn't respond in the expected time")
                
                time.sleep(0.5)

            except Exception as e:
                print(f"Failed to acquire asset {asset_id}. Error: {e}")

def acquire_asset_with_timeout(asset_id, index, timeout_seconds):
    try:
        url = "https://quixel.com/v1/acl"
        payload = {"assetID": asset_id}
        headers = {
            "Authorization": token,  
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers, timeout=timeout_seconds)
        
        print(f"Server response for asset {asset_id}: {response.status_code} - {response.text}")

        if response.status_code == 200:
            print(f"\033[92mSuccessfully acquired asset {asset_id}\033[0m")
            index[asset_id] = True  
            return True
        elif response.status_code == 400 and "USER_ALREADY_OWNS_ASSET" in response.text:
            print(f"User already owns asset {asset_id}")
            index[asset_id] = True  
            return True
        elif "TOKEN" in response.text and "EXPIRED" in response.text:
            ctypes.windll.user32.MessageBoxW(0, "Process aborted because your token has expired! Please update the token and restart the process. Progress has been saved.", "Token Expired", 0)
            print("Token expired. Stopping asset acquisition process.")
            exit()  
        else:
            print(f"Failed to acquire asset {asset_id}. Status code: {response.status_code} - {response.text}")
            return False

    except requests.exceptions.Timeout:
        print(f"Request for asset {asset_id} timed out after {timeout_seconds} seconds. Api may be overloaded!")
        return False  
    except Exception as e:
        print(f"Error acquiring asset {asset_id}: {e}")
        return False

script_directory = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(script_directory, 'quixel.index')


index = read_index(index_path)


acquire_non_owned_assets_from_index(index, index_path)

print("Process completed.")
