<%inherit file="site.mako" />
% for post in posts:
  <%include file="post.mako" args="post=post" />
% if bf.config.disqus_enabled:
  <div class="after_post"><a href="${post.permalink}#disqus_thread">Read and Post Comments</a></div>
% endif
  <hr class="interblog" />
% endfor
% if prev_link:
 <a href="${prev_link}">« Newer posts</a>
% endif
% if prev_link and next_link:
  --  
% endif
% if next_link:
 <a href="${next_link}">Older posts »</a>
% endif
