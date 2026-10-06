import os
from fabric_cicd import (
    FabricWorkspace,
    publish_all_items,
    unpublish_all_orphan_items
)
from azure.identity import ClientSecretCredential


# Use Azure CLI credential to authenticate
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
tenant_id = os.environ["TENANT_ID"] 
token_credential = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

target_workspace = FabricWorkspace(
    workspace_id=f"{os.environ['WORKSPACE_ID']}",
    repository_directory="./workspace",
    item_type_in_scope=["Notebook", "Pipeline", "Dataset", "Model", "Deployment"],
    token_credential=token_credential

)


publish_all_items(target_workspace)

unpublish_all_orphan_items(target_workspace)