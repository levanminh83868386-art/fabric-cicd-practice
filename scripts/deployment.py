import os
from fabric_cicd import (
    FabricWorkspace,
    publish_all_items,
    unpublish_all_orphan_items
)
from azure.identity import AzureCliCredential


token_credential = AzureCliCredential()
target_workspace = FabricWorkspace(
    workspace_id=os.environ["WORKSPACE_ID"],
    repository_directory="./workspace",
    item_type_in_scope=["Notebook", "Pipeline", "Dataset", "Model", "Deployment"],
    token_credential=token_credential

)


publish_all_items(target_workspace)

unpublish_all_orphan_items(target_workspace)