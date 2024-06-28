# Author: Michael McDowall

`docker-compose up -d`
`docker logs colab`

# How to copy files to image for conversion

`docker cp /path/on/host/to/folder/of/pdfs colab:/content/sample_data`
`docker exec -it colab /bin/bash`
`ls /content/sample_data`

# How to run the pipeline overview (colab version)

1. `docker compose up -d`
   1. `docker logs colab`
   2. Load the colab kernel
   3. `docker cp ./ALLPDF colab:/content/sample_data`
2. Run ExtractPaper
3.

# Running ExtractPaper

You can locally many ways. There are two ways to run listed below.

## Run locally with VSCode

0. Prerequisites

   1. Download and test that Docker runs locally.
   2. Download and install VSCode.

1. Open the repo

   1. Clone the repo in desired directory (This may require you to autheticate to GitHub):
   2. $ `git clone https://github.com/andym1125/ExtractPaper.git`
   3. $ `cd ExtractPaper`
   4. $ `code .`

2. Run the Docker images

   1. $ `docker-compose up -d` (or Windows equivalent)
   2. To get the url needed for future steps, copy the url that looks like `http://127.0.0.1:9000/?token=abcd1234` from this command:
   3. $ `docker logs colab | grep http://127.0.0.1:9000` (or Windows equivalent)

3. Connect the VSCode kernel to the docker image
   1. In vscode, navigate to ExtractPaper.ipynb
   2. Change the kernel. In the top right, it may say `python 3.12.2` or something similar. Click that text.
   3. Select another kernel... > Existing Jupyter Server > Enter the URL of the running Jupyter Server...
   4. Paste the URL copied from step 2.2, and hit enter.
   5. Give the server a name.
   6. Select the server as your kernel. You should be set!

## How to Run with Google Colab

0. Prequisites

   1. Login to GitHub
   2. Login to Colab
   3. Download and test that Docker runs locally.
   4. Ensure you're using Firefox or a Websocket-compatible browser.

1. Open the .ipynb in Colab

   1. File > Open Notebook > Github
   2. Include private repos
   3. Hit the dropdown to find andym1125/ExtractPaper
   4. Ensure the branch you want to work on is selected. **Do not work off of main, you won't be allowed to push**

2. Locally, run the docker images

   1. Ensure Docker is running.
   2. Clone the repository in a desired directory (This may require you setting up authentication to Github on your machine.):
   3. $ `git clone https://github.com/andym1125/ExtractPaper.git`
   4. $ `cd ExtractPaper`
   5. Run the docker instances:
   6. $ `docker-compose up -d`
   7. To get the url needed for future steps, copy the url that looks like `http://127.0.0.1:9000/?token=abcd1234` from this command:
   8. $ `docker logs colab | grep http://127.0.0.1:9000`

3. Connect Colab to your local instance:
   1. In your Colab browser instance:
   2. Connect > Connect to a local runtime
   3. Paste the url you copied earlier into the box labelled "Backend URL".
   4. "Connect"
4. Processing files
   1. On the left, click the "Files" icon.
   2. Upload the .PDFs you want to process. Note there is only 15 GB of space.
      1. Upload them into the `sample_data` folder.
   3. Run the .ipynb cells from top to bottom. Note the last cell may take some time.
   4. Your .XML files are now in the `sample_data` folder. Be sure to download them, as when the Colab instance is closed they may be deleted.
