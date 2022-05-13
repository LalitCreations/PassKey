import json

#TO DO: load functions in class

# Save/dump format
#
# "datatitle":{
#     "username": "",
#     "password": ""
# }

file_path = "src/data.json"



def json_save(title,user,pswd):

    save_dict= {"datatitle":""}
    dump_dict = {"username":"","password":""}

    save_dict[title]=save_dict.pop("datatitle")
    dump_dict["username"] = user
    dump_dict["password"] = pswd
    save_dict[title]=dump_dict



    with open(file_path,"r") as file:
        data = json.load(file)

    
    data.update(save_dict)
    with open(file_path, "w") as file:
        json.dump(data, file,indent=6)

    file.close()
    


def json_retrieve(datatitle):
    try:
        with open(file_path,"r") as file:
            data = json.load(file)
        
        data =  data[datatitle]
        username = data["username"]
        password= data["password"]
        file.close()    
        return username,password
    except:
        text = "NotFound"
        return text



def check_occupancy():
    with open(file_path,"r") as file:
        data = json.load(file)
    data = data["user_data"]
    if data["username"] == None and data["password"] == None:
        file.close()
        return True
    else:
        file.close()
        return False



def create_new_acc(username,password):
    with open(file_path,"r") as file:
        dict_data = json.load(file)
    data = dict_data["user_data"]
    data["username"] = username
    data["password"] = password
    with open(file_path, "w") as file:
        json.dump(dict_data, file,indent=6)

