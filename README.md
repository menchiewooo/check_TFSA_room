## How to run the code
1. Make sure the Chrome Webdriver is installed, and put the location of it in config file   
2. Place config in the same directory as the code, and fill in the account credentials  
3. 'cd' into the directory where scripts are located and run script from the terminal  
    ```
    python check_TFSA_room
    ```

## Features
1. When there's an authentication code required, the user will be asked to enter the code received from email or text message
2. Enable calling from command line hence the program can be run conviniently  
Sample output from terminal  
```
##### Getting balance for Wealth Simple #####  
[WDM] - Current google-chrome version is 87.0.4280
[WDM] - Get LATEST driver version for 87.0.4280
[WDM] - Driver [/Users/M/.wdm/drivers/chromedriver/mac64/87.0.4280.88/chromedriver] found in cache
##### Check email for authentication code... 
Enter authentication code: 948885
##### Balance of Wealth Simple: 5259.47 #####

##### Getting balance for Sunlife #####
...
```
     
## Limitation
1. For chrome driver only
2. The script is only set up for checking Wealth Simple, Sunlife and Questrade
 


