terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 4.0" }
    vault = {
        source = "hashicorp/vault"
        version = "~> 3.0" }
  }
}

# 1. Configuración de Vault (Apunta a tu Docker)
provider "vault" {
  address = "http://127.0.0.1:8200"
  token   = "root"
}

# 2. Pedimos las credenciales dinámicas a Vault
data "vault_aws_access_credentials" "creds" {
  backend = "aws"
  role    = "consul-lab"
}

# 3. Configuramos AWS usando los datos que nos dio Vault
provider "aws" {
  region     = "us-east-1"
  access_key = data.vault_aws_access_credentials.creds.access_key
  secret_key = data.vault_aws_access_credentials.creds.secret_key
}
