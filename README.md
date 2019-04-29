# SBPredictor

Predictor de pico y placa [ Pico y Placa Predictor ]

In order to excecute the predictos you have to use the command line, first you move to the folder that contains the predictor, for example: 

```python
cd ~/Python/SBPredictor/
```

and the excecute the commad:

```bash
python main.py -d <date> -t <time> -p <plate>
```

in order to validate if the predictor will work over your system you need to run the test, that you can run in the same way you run the predictor, with the commans:

```python
python Predictor.spec.py
python Plate.spec.py
```

if the test are OK then the predictor will work correctly in your system, otherwise, will not.

The code has been developed using the version 2.7.13 the python, and tested, both in the 2.7.13 and 3.5.3 versions of python.
