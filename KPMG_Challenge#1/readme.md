1. resource group 
2. Subnet and Vnet
3. azurerm_availability_set each for web, app and DB
4. strage account
5. 2VMs(1 linux  and 1 window)
6. 1 server(DB)

Note: 
    1. 3 tier environment common setup.png
    2. Reference taken for terraform and Azure : https://github.com/mofaizal/Azure-Terraform
    3. Terraform code sample : https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_host_pool
    4. Terrafrom code sample from terraform documents area. : https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs

Challenge #1 statement.
    A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources.