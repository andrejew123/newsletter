# HOWTO

### Install on a local machine

 1. Clone repository.
    ```
    cd <projects_folder>
    git clone https://github.com/andrejew123/newsletter.git
    cd newsletter
    ```
 2. Create virtualenv and install requirements.
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
### Setup for ChromeDriver

 1. Download [ChromeDriver](http://chromedriver.chromium.org/downloads). (chrome-driver version should be compatible 
    with Chrome version) and extract from zip
 2. Copy chromedriver to /usr/bin
    ```
    cd /home/user/Download
    sudo cp chromedriver /usr/bin
    ```
 3. Add the path to the folder /usr/bin. Example:
    ```
    export PATH=$PATH:/usr/bin
    ```
    
### Run
 1. Create run_test.sh file in newsletter folder
 2. Add there code as below where BASE_URL should be testing environment
    ```
    #!/usr/bin/env bash

    export BASE_URL='http://qa-recruitment-newsletter.s3-website-eu-west-1.amazonaws.com/'

    behave --tags=-skip

    ```
    "-skip"  will skip scenarios with tag @skip which are for further development
    
 2. Add executive permission for this script

    ```
    sudo chmod +x run_test.sh

    ```

 3. Run tests

    ```
    ./run_test.sh
    ```
