<p>
    Brandon Stafford<br />
    Renewable energy engineer at <a href="http://www.mysticriverengineering.com/">Mystic River Engineering</a><br />
    brandon at pingswept.org
</p>
<p>
    <a href="http://github.com/pingswept/">github.com/pingswept</a><br />
    <a href="http://twitter.com/pingswept/">twitter.com/pingswept</a><br />
    <a href="http://flickr.com/photos/pingswept/">flickr.com/photos/pingswept</a>
</p>
<a href="http://pingswept.org/atom.xml">
<img src="/images/rss.png" alt="Subscribe to feed" />
</a>
<p id="credits">
Powered by <a href="http://www.blogofile.com">Blogofile</a>.<br/>
<br/>
RSS feeds for <a href="${bf.util.site_path_helper(bf.config.blog_path,'feed')}">Entries</a>
% if bf.config.disqus_enabled:
 and <a
href="http://${bf.config.disqus_name}.disqus.com/latest.rss">Comments</a>.
% endif
<br>
</p>
% if bf.config.disqus_enabled:
<script type="text/javascript">
//<![CDATA[
(function() {
		var links = document.getElementsByTagName('a');
		var query = '?';
		for(var i = 0; i < links.length; i++) {
			if(links[i].href.indexOf('#disqus_thread') >= 0) {
				query += 'url' + i + '=' + encodeURIComponent(links[i].href) + '&';
			}
		}
		document.write('<script charset="utf-8" type="text/javascript" src="http://disqus.com/forums/${bf.config.disqus_name}/get_num_replies.js' + query + '"></' + 'script>');
	})();
//]]>
</script>
% endif

<script type="text/javascript">
    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
    var pageTracker = _gat._getTracker("UA-96134-2");
    pageTracker._trackPageview();
</script>