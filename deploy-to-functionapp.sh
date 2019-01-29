#!/usr/bin/env bash
FUNCTION_APP_NAME="yourAppName"
FUNCTION_APP_FOLDER="yourAppFolder"


echo "--> Install Azure Functions Core Tools"
wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install azure-functions-core-tools -y

echo "--> Assign rights to execute the virtual environment"
find . -type d -exec chmod +rx {} \;

echo "--> Activate Python Virtual environment in drop folder"
source .env/bin/activate

echo "--> Publish the function app to Azure Functions"
cd $FUNCTION_APP_FOLDER
func azure functionapp fetch-app-settings $FUNCTION_APP_NAME
func azure functionapp publish $FUNCTION_APP_NAME --build-native-deps 