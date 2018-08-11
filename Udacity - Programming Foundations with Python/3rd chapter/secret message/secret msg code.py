"Rename Files"
import os
# 1. Read all the files
def rename_files ():
     F = os.listdir("/media/hp/Timepass/Udamy/2nd chapter/secret message/prank")
     #print (F)
     path_folder = os.getcwd()
     print("Current working folder is"+path_folder)
     os.chdir("/media/hp/Timepass/Udamy/2nd chapter/secret message/prank")#to give os exact path of files whose names to be changed
     # 2. rename files with no numbers in their names
     for F_name in F:
         print("Old name:"+F_name)
         print("New name:"+F_name.translate(None, "0123456789"))
         os.rename(F_name, F_name.translate(None, "0123456789"))
     os.chdir(path_folder)#to set os back to its original path
rename_files()    