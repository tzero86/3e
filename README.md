# 3e (tree) - a tree command replacement

![Imgur](https://i.imgur.com/OdPfSld.gif)


Annoyed by Windows' native tree command not supporting "skip some directories" functionality, ended up doing my own cli tree command. 3e (pronounced tree) is just that a replacement for tree, an ascii directories tree generator.
just use the exe provided or generate your own with pyinstaller and add it to system $PATH:

```
pyinstaller --onefile 3e.py
```

enjoy! '.git'


Once added to the path simply use it:

```
3e . --skip 'node_modules' 'dist' 'etc' --only-dirs 
```


@tzero86
