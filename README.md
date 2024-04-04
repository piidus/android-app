# android-app
android app using kivy and kivymd 
using MVC model and Auto reload

- install
```
pip install kivymd

```
- upgrade
```
pip install https://github.com/kivymd/KivyMD/archive/master.zip
```
- install watchdog
```
pip install watchdog
```

- To create a MVC prototype with hotreload function
```
python -m kivymd.tools.patterns.create_project MVC . <APPNAME> python3 3.12.2 --use_hotreload yes
```
```
kivymd.create_project MVC . DEMO2 python3.12 2.3.0 --use_hotreload yes
```

kivymd.create_project \
    MVC \
    /Users/macbookair/Projects \
    MyMVCProject \
    python3.10 \
    2.1.0 \
    --use_hotreload yes

- For Responsive
kivymd.create_project \
    name_pattern \
    path_to_project \
    name_project \
    python_version \
    kivy_version \
    --name_screen FirstScreen SecondScreen ThirdScreen \
    --use_responsive FirstScreen SecondScreen
```
kivymd.create_project MVC <PATH> <PROJECTNAME> python3.12 2.3 --name_screen FirstScreen SecondScreen ThirdScreen --use_responsive FirstScreen SecondScreen --use_hotreload yes
```
- example 1
```
kivymd.create_project MVC E:\code\collection\android-app  ResposiveApp 3.12 2.3 --name_screen FirstScreen SecondScreen ThirdScreen --use_responsive FirstScreen SecondScreen --use_hotreload yes
```
- Example 2 
```
kivymd.create_project MVC E:\code\collection\android-app  MYProject 3.12 2.3 --name_screen FirstScreen SecondScreen ThirdScreen  --use_hotreload yes
```
### Now From the new project folder except venv file move all to main file or just install all from my github code download and delete MYProject folder and Run and test