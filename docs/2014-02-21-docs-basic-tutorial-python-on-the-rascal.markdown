---
title: "docs basic tutorial python on the rascal"
slug: docs-basic-tutorial-python-on-the-rascal
author: Brandon Stafford
lastmod: 2014-02-22T02:05:53.000Z
date: 2014-02-21T21:37:19.000Z
source: rascalmicro.com
---
## Getting started with Python on the Rascal ##

The Rascal ships with a built-in webserver. It serves HTML and images like a normal webserver, but it can also execute Python code in response to web requests.

The file `server.py` contains all the functions that control how the Rascal reacts to requests from the web. The functions are organized by URL, and you can add your own functions to make the Rascal react to a new URL. You can edit `server.py` using the Rascal's built-in web editor, which you can find at `http://your.rascal's.address/editor/`.

## A minimal example ##

As an example, here's the basic structure of a function in `server.py`.

```language-python
@public.route('/path', methods=['POST'])
def function_name():
    do_something()
    return render_template('/page.html')
```

 * `'/path'` specifies what URL should trigger this function. For example, if you made the path `'/detonate'` and your Rascal had IP address `192.168.1.101`, the function would be triggered by a POST request to `http://192.168.1.101/detonate`.
 * `function_name` is just a unique identifier for the function. You can pick whatever you want, but make sure it's unique, or the Rascal will get confused.
 * `do_something()` is where you put the code that does the real work. You can control the Rascal's hardware with the [Pytronics library][1] or use other Python libraries to do whatever you want-- tweet something, solve a differential equation, generate an image, whatever.
 * `'/page.html'` is the name of the page that you want to send back to the browser afterwards. Sometimes, you don't need to send back a response, so you can leave this line blank or send back a diagnostic message like "It worked."

Here's what the example function might look like filled in.

```language-python
@public.route('/send-to-lcd', methods=['POST'])
def send_to_lcd():
    data = request.form['serial_text']
    pytronics.serialWrite(data, 9600)
    return render_template('/lcd.html')
```

Assuming the same IP address as before, if you sent an HTTP POST request containing form data `serial_text: Hamilton` to `http://192.168.1.101/send-to-lcd`, the `send_to_lcd()` function would be executed. It would retrieve the word "Hamilton" from the request and send it out the Rascal's serial port at a rate of 9600 bits per second. Then, it would send back a copy of the `lcd.html` template to your browser.

Note the two bits of magic that occurred here. The Rascal knew what Python code to execute because your POST request went to `/send-to-lcd`, and it also magically pulled whatever data was included in the POST into a structure called `request.form`, so you could retrieve it with `request.form['serial_text']`.

## More detail ##

If you want more detail, you can start by looking at all the functions that are already in server.py. Try copying and pasting one and changing it to do something new. (When you copy and paste, remember to make the URL and function name unique, or you'll end up in trouble.)

If you want still more detail, you can look at the documentation for [Flask][4], the web framework that the Rascal uses, and [Werkzeug][5], the utility library that Flask uses behind the scenes. The [routing section][2] of the [Flask quickstart][3] page is a good starting point.

[1]: /docs/rascal-api.html
[2]: http://flask.pocoo.org/docs/quickstart/#routing
[3]: http://flask.pocoo.org/docs/quickstart/
[4]: http://flask.pocoo.org
[5]: http://werkzeug.pocoo.org/