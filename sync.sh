#!/bin/sh

jekyll
rsync -vaz --exclude='*.sh' _site/ cmplrz@www.endofunctor.org:~/public_html/
