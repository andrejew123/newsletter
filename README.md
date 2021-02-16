# HOWTO

## Install on a local machine

 1. Clone repository.
    ```
    cd <projects_folder>
    git clone 
    ```
 2. Create virtualenv and install requirements.
    ```
    python3 -m venv venv
    source venv/bin/activate
    cd newsletter
    pip install -r requirements.txt
    ```
#### Setup for ChromeDriver

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
 4. Add URL of system under testing to run_test.sh (if it's not already set).
    ```
    export BASE_URL='http://qa-recruitment-newsletter.s3-website-eu-west-1.amazonaws.com/'
    ```
    
### Run
```
    cd newsletter
    ./run_test.sh
```
