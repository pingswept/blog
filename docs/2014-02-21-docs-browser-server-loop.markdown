---
title: "docs browser server loop"
slug: docs-browser-server-loop
author: Brandon Stafford
lastmod: 2014-02-22T01:31:32.000Z
date: 2014-02-21T21:46:47.000Z
source: rascalmicro.com
---
## How data travels back and forth between your browser and the Rascal ##

The Rascal runs a webserver that can execute Python code on your behalf. The main user interface to the Rascal is your web browser, which talks to the Rascal's webserver.

Let's suppose you want to send some data out the serial port to, for example, an LCD that you had plugged into the Rascal. You'd start by creating a short HTML page that contains a form where you can type in whatever you want to send, along with a button that submits the form to the Rascal. (The form could also be submitted asynchronously, without reloading the page, by using a Javascript library like jQuery, but let's keep it simple for now-- you press the button; the data gets sent to the Rascal.)

Here's what that might look like, roughly speaking:

```language-markup
<html>
<head>
    <title>Rascal demo</title>
</head>
<body>
    <form id="serial_form" method="POST" action="send-to-lcd">
        <textarea id="serial_text" name="serial_text" type="textarea"></textarea>
        <button type="submit" alt="Send serial data">
            Send data
        </button>
    </form>
</body>
</html>
```

Notice that in the opening HTML form tag, we wrote `method="POST" action="/send-to-lcd"`. These two attributes tell the Rascal what to do with the data it finds in the form. When you press the button, it submits a POST request back to the Rascal with the URL set to `/send-to-lcd`.

## What happens on the Rascal ##

The Rascal is running a webserver that is set up to execute Python for you. If you look in `/public/server.py`, you'll see this:

```language-python
@public.route('/send-to-lcd', methods=['POST'])
def send_to_lcd():
    pytronics.send_serial(request.form['serial_text'], 9600)
    return render_template('/lcd.html')
```

This snippet defines the Python function `send_to_lcd`. The first line tells the Rascal to call the subsequent function whenever someone POSTs to the URL `/send-to-lcd`, which is what happened when you pressed the button on your form. The names of the function and the URL are almost identical (underscores vs. hyphens), but they don't have to be.

Inside the Python function above, we have access to the data from the form as `request.form`. If you look back at the HTML we wrote earlier, you'll see that the textarea has the attribute `id="serial_text"`, so to stick the data from the textarea into a variable we can use, we use `message = request.form['serial_text']`.

Once we've assigned our text to `message`, we can send the message out the serial port with the `pytronics.send_serial()` function from the Rascal's Pytronics library. You can imagine that you could do all sorts of fun stuff here-- count the number of letters in the message and flash an LED that number of times, send a message to something on the I<sub>2</sub>C bus, send a tweet, or whatever.

## Finishing the loop ##

The last line of the Python function sends data back to your browser. Let's suppose that you create a response page on the Rascal called serial.html that looks like this:

```language-markup
<html> 
<head> 
    <title>Rascal demo</title>
</head> 
<body> 
    The Rascal just sent this message out the serial port: {{ message }}
</body> 
</html>
```

This will get sent back to your browser, but the Rascal's templating engine will stick the value of the variable ```message``` in for the template tag ```{{ message }}```. Sending the same message back to the browser is kind of lame, given that you wrote the message in the first place, but you could send other data instead-- maybe a something you read from the serial port, or results of a Google search, or a reading from a sensor.

## More information ##

That's the end of the description of the basic loop, but you might want more details about what you can do with the templates or how URLs are mapped to Python functions.

  * More information on the [Jinja2 template engine][1].
  * More information on the [Flask web framework][2], which does the URL mapping

[1]: http://jinja.pocoo.org/docs/templates/
[2]: http://flask.pocoo.org/docs/quickstart/