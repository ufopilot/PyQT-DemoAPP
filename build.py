import json, os
import subprocess
import locale

locale.setlocale(locale.LC_ALL,'en-US')

with open("gui/settings/app_settings.json", "r", encoding='utf-8') as reader:
    settings = json.loads(reader.read())

app_name = settings['app_name']
icon = settings['icon']['ico']     

command = ('pyinstaller.exe',
            '--onefile',
            '--windowed',
            '--icon',  icon,
            '--name', app_name,
            '--hidden-import', 'requests',
            '--hidden-import', 'bs4',
            '--hidden-import', 'pyperclip', 
            '--hidden-import', 'cloudscraper',
            '--hidden-import', 'webbrowser',
            '--add-data', 'resources_rc.py;.',
            '--add-data', 'qt_core.py;.',
            '--add-data', 'gui;gui/',
            'main.py')
            
process = subprocess.Popen(command, 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output.strip())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output 
        for output in process.stdout.readlines():
            print(output.strip())
        break
exit()
os.system("C:\\Users\aldor\AppData\Local\Programs\Python\Python39\Scripts\pyinstaller.exe \
             --onefile --windowed \
              --icon '{icon}' \
              --name '${app_name}' \
              --hidden-import 'requests' \
              --hidden-import 'bs4' \
              --hidden-import 'pyperclip' \
              --hidden-import 'cloudscraper' \
              --hidden-import 'webbrowser' \
              --add-data 'resources_rc.py;.' \
              --add-data 'qt_core.py;.' \
              --add-data 'gui;gui/' main.py ")