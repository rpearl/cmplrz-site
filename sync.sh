#!/bin/sh

jekyll
rsync -vaz --exclude='*.sh' --exclude='project-writings/*' _site/ cmplrz@www.endofunctor.org:~/public_html/
