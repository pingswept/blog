--- 
wordpress_id: 34
layout: post
title: Wordpress plugin for Google Analytics
wordpress_url: http://www.betsymattox.com/pingswept/2005/11/14/wordpress-plugin-for-google-analytics/
---
	I wrote a Wordpress plug-in for the Google Analytics script. After I wrote it, I found that someone else had <a href="http://blog.thedt.net/2005/11/14/google-analytics-plugin/">written a better one</a> a few hours earlier.
	Anyway, here&#8217;s mine. Cut and paste it into a file in your plugins directory with some name that ends in .php. Sign up for an account with Google, and paste your account string where indicated below. Then go to the plugins admin page and click &#8220;activate.&#8221;
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
_uacct = &#8220;PUT YOUR ACCOUNT STRING HERE&#8221;;<br />
urchinTracker();<br />
&#8216;;<br />
}
	add_action(&#8217;wp_head&#8217;, &#8216;call_google_script&#8217;);
	?&gt;</code>

