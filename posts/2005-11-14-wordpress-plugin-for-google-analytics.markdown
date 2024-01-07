---
date: 2005-11-14T00:00:00.000Z
format: markdown
title: Wordpress plugin for Google Analytics
---

I wrote a Wordpress plug-in for the Google Analytics script. After I wrote it, I found that someone else had <a href="http://blog.thedt.net/2005/11/14/google-analytics-plugin/">written a better one</a> a few hours earlier.
Anyway, here's mine. Cut and paste it into a file in your plugins directory with some name that ends in .php. Sign up for an account with Google, and paste your account string where indicated below. Then go to the plugins admin page and click "activate."

```(lang=javascript)
/*
Plugin Name: Google Analytics
Plugin URI: http://pingswept.org/index.php/wp_plugins
Description: Adds Javascript instrumentation to main page for Google Analytics
Version: 0.1
Author: Brandon Stafford
Author URI: http://pingswept.org
*/
function call_google_script() {
        echo '
type="text/javascript">
_uacct = "PUT YOUR ACCOUNT STRING HERE";
urchinTracker();
';
}
add_action('wp_head', 'call_google_script');
?>
```
