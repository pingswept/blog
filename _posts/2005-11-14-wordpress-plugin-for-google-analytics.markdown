--- 
wordpress_id: 34
layout: post
title: Wordpress plugin for Google Analytics
wordpress_url: http://www.betsymattox.com/pingswept/2005/11/14/wordpress-plugin-for-google-analytics/
---
I wrote a Wordpress plug-in for the Google Analytics script. After I wrote it, I found that someone else had <a href="http://blog.thedt.net/2005/11/14/google-analytics-plugin/">written a better one</a> a few hours earlier.
Anyway, here's mine. Cut and paste it into a file in your plugins directory with some name that ends in .php. Sign up for an account with Google, and paste your account string where indicated below. Then go to the plugins admin page and click "activate."
<code><br />
/*<br />
Plugin Name: Google Analytics<br />
Plugin URI: http://pingswept.org/index.php/wp_plugins<br />
Description: Adds Javascript instrumentation to main page for Google Analytics<br />
Version: 0.1<br />
Author: Brandon Stafford<br />
Author URI: http://pingswept.org<br />
*/
function call_google_script() {<br />
        echo '
type="text/javascript"&gt;<br />
<br />
<br />
_uacct = "PUT YOUR ACCOUNT STRING HERE";<br />
urchinTracker();<br />
';<br />
}
add_action('wp_head', 'call_google_script');
?&gt;</code>

