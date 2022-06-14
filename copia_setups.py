import os
import json
import sys
import shutil

# Um comentário!
# Um segundo comentário!

CURRENT_PATH = os.getcwd()

with open(os.path.join(CURRENT_PATH, "config.json")) as json_file:
    config = json.load(json_file)
    json_file.close()


version = "2022.3"#str(sys.argv[1])
versions_list = config['VERSIONS']
setups_folder = config['SETUPS_PATH']
destination_folder = config['DESTINATION_FOLDER']

def log(message_dict):
    keys = message_dict.keys()
    for key in keys:
        print(key + ": " + message_dict[key])

for folder in os.listdir(setups_folder):
    setup_found = True
    if "Setups" in folder:
        product_folder = os.path.join(setups_folder, folder)
        product_version_folder = os.path.join(product_folder, version)
        actual_search_version = version
        log({"NOME DO PRODUTO": folder, "VERSÃO": version, "PASTA VERSÃO PRODUTO": product_version_folder})
        while (not os.path.exists(product_version_folder)):
            log({"INFO": f"PASTA DA VERSÃO {actual_search_version} DESTE PRODUTO NÃO EXISTE. PROCURANDO VERSÃO ANTERIOR..."})
            if(versions_list.index(actual_search_version)-1 < 0):
                log({"INFO":"NÃO EXISTE VERSÃO DESTE PRODUTO, PARA AS VERSÕES CADASTRADAS NO ARQUIVO CONFIG.JSON"})
                setup_found = False
                break
            previous_version = versions_list[versions_list.index(actual_search_version)-1]
            log({"VERSÃO ANTERIOR": previous_version})
            actual_search_version = previous_version
            product_version_folder = os.path.join(product_folder, previous_version)
            setup_found = True
        
        if(setup_found):
            for file in os.listdir(product_version_folder):
                if(file.endswith(".msi")):
                    log({"SETUP ENCONTRADO": file})
                    file_path = os.path.join(product_version_folder, file)
                    destination_path = os.path.join(destination_folder, file)
                    log({"CAMINHO ATUAL SETUP": file_path, "CAMINHO DE DESTINO DO SETUP": destination_path})
                    if (not os.path.exists(destination_path)):
                        shutil.copy2(file_path, destination_path)
                        log({"SUCCESS": "SETUP COPIADO!"})
                    else:
                        log({"INFO": "ESTE SETUP JÁ EXISTE NA PASTA DE DESTINO"})



