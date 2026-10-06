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

print(f"Deploying artifacts to workspace '{os.environ['WORKSPACE_ID']}'...")
target_workspace = FabricWorkspace(
    workspace_id=os.environ['WORKSPACE_ID'].strip(),
    repository_directory="./workspace",
    item_type_in_scope=["Notebook","DataPipeline"],
    token_credential=token_credential,
    environment="TEST"
)


publish_all_items(target_workspace)

unpublish_all_orphan_items(target_workspace)

print(f"Deployment completed successfully to workspace '{os.environ['WORKSPACE_ID']}'")