# About

Crawlers needed to add more groups into the project database. And this one is only a simple temporary project.Feel free to upadate and improve.

- [x] [Garage48](http://garage48.org/hackthecrisis/?fbclid=IwAR2B8USw8Vf99Nemf3kqDA1PG8gDzRYqUXQb_gmkiwPERJgvhzrSGCIgiwQ)

### Garage48

Is one of the similar project and this one is simple tool to get a quick data.

### Install
> Mac os, just run `make install` && `make run` then the data will be updated int the `output/group_list.json`

Install dependencies:
```bash
pip install -r rrequirements.txt
```

Run main command:
```bash 
python main.py
```

Check the new list at `output/group_list.json`

### Output structure
Currently data structure is like this one below, but we can always change as we need:

```json
[
  {
    "name":"Some Group",
    "logo_url": "http://example.org/img.jpg",
    "country_id": 1
  }
]
```

