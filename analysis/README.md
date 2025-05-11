Changes in key naming conventions:

Initial: 
```
re.sub("[^A-Za-z0-9]+", "", "{}vol{}".format(name, vol)).lower()
```

- Need to change as 1 and -1 gave same key
- Issue names with just symbol (∞, ½) had empty issue in key
- Replace space with word space because "Wild Thing" and "WildThing"
- Slash with word because Avengers/X-men, for firestore this means diff document