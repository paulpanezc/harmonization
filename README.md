Example how to extract comments and suggestions from Google Docs document

- Create a project in Google Cloud Platform (https://console.cloud.google.com/)
- Enable a Google Drive API and Google Docs API
- Create an ID Oauth client
- Create a service account with permissions to:
    - drive
    - drive.file
    - drive.readonly
    - documents
- Download credentials.json file
- Move credentails.json file into harmonization/google
- Return to project root
- Install requirements in an  environment using poetry
> poetry install --no-root 
- Execute main script
> python main.py
