# Quixel-Megascans-Miner

Description: Automatically adds 10250 assets to your account

Demo video: https://www.youtube.com/watch?v=umhsmPZbEME (the one shown in the video differs from this current one because it used to build the index dynamically but it was easier to build up an index once)

Note: I have intentionally added a delay to the acquisition process to prevent overwhelming Quixel's API. If you plan to modify the script to send requests faster than recommended, please be aware that this may introduce risks, such as rate-limiting or API access issues. In that case proceed with caution.

*PLEASE GIVE THIS A STAR ⭐ IF YOU LIKED IT! THANKS!*

Step 1: Get your account token

1) go to: https://quixel.com/megascans/home/
2) right click on the page -> inspect element then navigate to the "Network" tab
3) download a random asset (it's not needed for it to fully download)
4) in the "Name" tab click on "extended"
5) scroll down till you find this seen in the image below copy and paste it into the variable token of the script
   ![tut](https://github.com/user-attachments/assets/381ba5f7-059c-4d29-b817-ad288dcbc1fd)

![image](https://github.com/user-attachments/assets/770c4782-5408-43a0-bb65-2bf9d9229622)




Step 2: Install dependencies 

1) run "install dependencies.bat" from the folder

Step 3: Run the script

run "quixelminer.py" and wait till all of the 10k assets from the quixel.index get added to your account!





