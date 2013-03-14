Posse.js
--------
Posse.js is a lightweight wrapper around modern browsers' EventSource API.


EventSource?
------------
Yes, EventSource (also known as Server-Sent Events, SSE, or HTML5 push notifications) is a method by which a web server
can send arbitrary data to a listening client over a standard HTTP connection.  It's like a browser-managed long-poll.

MDN has some [basic documentation](https://developer.mozilla.org/en-US/docs/Server-sent_events) on the API.


Posse?
------
Yes, Posse (short for Plain Old SSE).  While using EventSource directly isn't hard, there are a few things about it that
could be nicer.  For example:

 - Posse verifies that the message you got was from the server you expected.
 - Posse attempts to parse the message data as JSON.
 - Posse is chainable.


Usage
-----
To use Posse, call it's constructor method, (optionally) passing in a config mapping.  If you omit the config,
Posse will try to connect to `/sse/` by default, though no handlers will be setup.  So minimal usage
would look like:

	<script src="/path/to/posse.js"></script>
	<script>
	    conn = new Posse().on('message', console.log.bind(console));
	</script>

...which would simply bind to the `/sse/` endpoint and dump all received messages to the console.  The `.on()` method
is chainable, so you can add multiple handlers in one fell swoop:

    conn = new Posse({url: '/my_sse_endpoint/'})
    				.on('my_event', function(data){
    					alert("My event just gave me: " + data);
    				})
    				.on('message', function(data){
    					alert("Message received: " + data)
    				});

The `'message'` event is special in that it is called when an event arrives that is *not* otherwise handled.  Besides `url`,
the config mapping accepts the following keys:

	{
		url: "/sse/",
		verify_origin: true,
		allowed_origins: [window.location.origin],
		origin_checker: self.origin_matches,
		data_formatter: self.format_data,
		handlers: {}
	}

You can override just a single config variable at any time by calling `conn.set(<name>, <value>)`.  If you have multiple 
variables to override at a time, you can pass a mapping instead (`conn.set(<config_mapping>)`).

Finally, to forcibly close a posse connection, call `conn.disconnect()`.


MIT License
-------
Copyright (c) 2013 Don Spaulding II <donspauldingii@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Contact
-------
Feel free to get in touch by email at: <donspauldingii@gmail.com>