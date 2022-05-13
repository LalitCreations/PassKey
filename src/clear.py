import json
import os

#######################################
# NOT TO BE ADDED TO GIT STAGING AREA #
#######################################

file_path = "src/data.json"

reset = {
      "user_data": {
            "username": None,
            "password": None
      }
}

print("starting cleanup")
with open(file_path, "w") as file:
    json.dump(reset, file,indent=6)
    print("data.json file has been reset")
    file.close()

if os.path.exists("src/encryption_keys.key"):
  os.remove("src/encryption_keys.key")
  print("deleted encryption files")
else:
  print("The encryption_keys.key file does not exist") 
print("cleanup has been done")