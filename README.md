osx-screen-capture
==================

Screen capture and upload tool for OS X.

Install
-------

```
git clone https://github.com/noraesae/osx-screen-capture.git
cd osx-screen-capture
```

Needs [PyImgur](https://github.com/Damgaard/PyImgur).

```
$ pip install pyimgur
```

And should create `imgur_client_id` file of which content is imgur client id in the project directory.

```
$ # When the client id is '123456789abcdef'
$ echo '123456789abcdef' > imgur_client_id
```

How To Use
----------

```
$ python capture.py
```

And the link will be copied to clipboard with an OS X notification after the upload's done.

License
-------

MIT
