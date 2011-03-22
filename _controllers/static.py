import os
from blogofile.cache import bf

config = {"name"        : "Static",
          "description" : "Static page renderer",
          "priority"    : 40.0}

static_dir = os.path.join("_static")

def run():
    static = read_pages()
    write_pages(static)

def read_pages():
    return [p for p in os.listdir(static_dir) if p.lower().endswith(".markdown")]

def write_pages(static):
    for page in static:
        print 'Writing static page based on ' + page
        f = open(os.path.join(static_dir, page), 'r')
        bf.writer.materialize_template(
            "static.mako",
            ("static",os.path.splitext(page)[0]+".html"),
            {"page":f.read()}
        )
