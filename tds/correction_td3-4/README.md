# Correction TD3 & TD4

## curl

Voici des exemples de commande `curl` pour accéder aux différentes route dans [app.py](./app.py)

```python
@app.route("/dictionary", methods=['GET'])
def get_dict():
	...
```

```bash
curl -X GET http://localhost:5000/dictionary
```


```python
@app.route("/dictionary/<value>", methods=['POST'])
def add(value):
  ...
```

```bash
curl -X POST http://localhost:5000/dictionary/valeur_de_test
```

```python
@app.route("/", methods=['GET', 'POST'])
def hello_world():
  ...
```

```bash
curl -X GET http://localhost:5000/
```

```bash
curl -X POST -d "key=value" http://localhost:5000/ 
```
