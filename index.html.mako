<%inherit file="_templates/site.mako" />
% for post in bf.posts[:5]:
  <%include file="post.mako" args="post=post" />
% if bf.config.disqus_enabled:
  <div class="after_post"><a href="${post.permalink}#disqus_thread">Read and Post Comments</a></div>
% endif
  <hr class="interblog" />
% endfor
<a href="page/2/">Older posts »</a>
