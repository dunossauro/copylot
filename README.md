# Copylot
Your copilot to studies and work (Pomodoro-timer, Translate and Notes app) 


Copylot are three applications in one:
- [ ] Pomodoro
- [ ] Translate
- [ ] Notes


Copilot is supported in:
- [ ] Windows
- [ ] Linux
- [ ] OSX
- [ ] Android
- [ ] iOS
- [ ] Python file


### How to run this project?

```bash
pip install poetry  # If you don't already have poetry 
poetry install
poetry run main.py
```

### How to run tests?
```bash
poetry run pytest
```

### How to build android app?

To create debug app (ARM version)

```bash
poetry run buildozer debug
```

this command will create a `Copylot-0.1-armeabi-v7a-debug.apk` on `bin` path.

If you want dolpy this app in your android phone you can use:

```bash
poetry run buildozer deploy
```
