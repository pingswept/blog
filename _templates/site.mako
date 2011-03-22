<%inherit file="base.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    ${self.head()}
  </head>
  <body>
    <div id="column">
      ${self.header()}
      <div id="content">
          ${next.body()}
      </div> <!-- End Content -->
      <div id="sidebar"> 
          <ul> 
              <li> 
                  Static pages
                  <ul> 
                      <li><a href="http://pingswept.org/static/about.html">About</a></li> 
                      <li><a href="http://pingswept.org/static/projects.html">Projects</a></li> 
                      <li><a href="http://pingswept.org/static/commute-data.html">Commute data</a></li> 
                      <li><a href="http://pingswept.org/static/pcb-checklist.html">PCB checklist</a></li> 
                      <li><a href="http://pingswept.org/static/quotes-from-a-former-career.html">Quotes from a former career</a></li> 
                      <li><a href="http://pingswept.org/static/the-four-commandments-of-github.html">The four commandments of Github</a></li> 
                      <li><a href="http://pingswept.org/static/tools.html">Tools</a></li> 
                      <li><a href="http://pingswept.org/files/xorgconf-for-xubuntu-on-g3-imac.txt">xorg.conf for Xubuntu on G3 iMac</a></li> 
                  </ul> 
              </li> 
          </ul> 
      </div> <!-- End Sidebar -->
      <div id="footer">
        ${self.footer()}
      </div> <!-- End Footer -->
    </div> <!-- End Column -->
  </body>
</html>
<%def name="head()">
  <%include file="head.mako" />
</%def>
<%def name="header()">
  <%include file="header.mako" />
</%def>
<%def name="footer()">
  <%include file="footer.mako" />
</%def>
