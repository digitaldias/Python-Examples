# Python-Examples
This is a collection of scripts and other useful stuff that I'm collecting for my journey in learning Python. 

| Things I've struggled with that are now resolved | 
| ---------------- |
| [FunctionApp Build Script for Azure Devops](https://github.com/digitaldias/Python-Examples/blob/master/build-and-test.yaml) |
| [FunctionApp Release Script for Azure Devops](https://github.com/digitaldias/Python-Examples/blob/master/deploy-to-functionapp.sh) |


Look below for a brief explanation of the rationale behind each of the solutions I've found

-----

### Build script for Azure FunctionApp written in Python
Well, Python does NOT produce a build output as it is an interpreted language, so what is the reasoning for looking at this as a "Build"?
The answer is simple, during build, what we aim to do is two things:
* Create a virtual execution environment for Python to operate in, so that if the host changes versions, the function will not be affected
* Execute all unit-tests within the function space, so we can rely on the logic not having changed as a cause of the commit

The output of this "build" is therefore a drop folder where the virtual environment is part of the items that will be deployed. 

### Release script for the Azure Function app
The scripts as well as the virtual environment are now deployed to a drop folder that can be picked up by a bash script in the release pipeline. The steps here are simply: 
* Install the Azure Functions Core tools in order to be able to publish the functionapp
* Activate the virtual environment produced during build
* Retrieve all settings from the existing function app in azure (this step is required as the settings are encrypted)
* Calling "publish" to transfer the code into a working python FunctionApp in Azure
