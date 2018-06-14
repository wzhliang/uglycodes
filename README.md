A tool that's meant to be used in a docerized pipeline for enforcing code formatting.

Run it like this:

`docker run -v $PWD:/code  nouglycode python /tools/main.py go /code`

It just uses `black`, or `google-java-formatter`, or `gofmt` on the last commit and see if everyting is in order.
