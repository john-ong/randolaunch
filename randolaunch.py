import subprocess,time,random,os,site
instance=0
list = ['revit','acad','mbox']
cont=0

print('''Welcome to the application launch randomizer. 

You would need to have Autocad, Revit, Mudbox installed in their default directories for this to work.
This application will randomly launch an app, keep it open for a random amount of time between 
15 mins and 30mins, close it and repeat.

If you would like to cancel, simply close the application. 
''')

#Request input from the user

print('How many times would you like the application to cycle?')
repeat = int(input())


print('Would you like to play a game? Y/N')
response = input()
if response == 'Y':
    while instance < repeat:
        choice=random.choice(list)
        if choice =='acad':
            rand = random.randrange(900,1500)
            print('The cycle will last '+ str(rand/60) + ' minutes.')
            subprocess.Popen('C:\\Program Files\\Autodesk\\AutoCAD 2021\\acad.exe')
            time.sleep(rand)
            os.system("TASKKILL /F /IM acad.exe")
        elif choice =='revit':
            rand = random.randrange(900,1500)
            print('The cycle will last '+ str(rand/60) + ' minutes.')
            subprocess.Popen('C:\\Program Files\\Autodesk\\Revit 2021\\Revit.exe')
            time.sleep(rand)
            os.system("TASKKILL /F /IM revit.exe")        
        else:
            rand = random.randrange(900,1500)
            print('The cycle will last '+ str(rand/60) + ' minutes.')
            subprocess.Popen('C:\\Program Files\\Autodesk\\Mudbox 2020\\mudbox.exe')
            time.sleep(rand)
            os.system("TASKKILL /F /IM mudbox.exe")
        instance+=1
elif response == 'N':
    print('goodbye!')
    quit
    cont+=1
else:
    print('Please enter a valid response!')


