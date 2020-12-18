# instance

```
Usage: instance [OPTIONS] COMMAND [ARGS]...

  This script will work on instances

Options:
  --help  Show this message and exit.

Commands:
  start   starts an instance
  status  prints and running instances
  stop    stops an instance
```

## Tricks

```bash
pinstance status | grep -A2 butzer
```

### pip install --editable .
allows editing the instance.py without having to continually re-istall the instance command

run
```
pip3 install --editable .

or 
make
```

```
[tony@bastion instance]$ instance --help
Usage: instance [OPTIONS] COMMAND [ARGS]...

  This script will work on instances

Options:
  --help  Show this message and exit.
```

# myssh and myrdp

### Customize these shell scripts and you can login to your instance by AWS tag name


[https://www.youtube.com/watch?v=kNke39OZ2k0](https://www.youtube.com/watch?v=kNke39OZ2k0)
