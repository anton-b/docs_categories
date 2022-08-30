# Simple texts categorisation engine

Implemented without heavy libraries for machine learning in order to be able to understand the underlying principles better.

#### Usage

* add some text files into `data` subdirectories, each directory should be the name of a category of the texts you put there, for example `scientific`

* run `learn.py` to create models. Models is nothing but words frequencies in a given category of files. 


#### How this works

Input file is normalised and tokenised, we get words and their frequencies, then cosine similarity comparison is applied to the vectors(list of word frequencies) for example:

model, called "progamming":
```
{"developers": 1, "nice": 2, "guys": 3}
```

input text:
```
Developers are all really nice guys, we are all like them a lot.
```

would be tokenized into:
```
{"developers": 1, "really": 1, "nice": 1, "guys": 1, "like": 1, "them": 1}
```

compared vectors would look like:

```
[1, 1, 1]
[1, 2, 3]
```

and 
```
1 - spatial.distance.cosine(a, b)
0.9258200997725514
```
means that these are very similar. 


If we have multiple models categories we can compare our text against each and choose the most matching one, therefore tag unknown text with the category. 