#!/bin/sh

jekyll
rsync -vaz --exclude='*.sh' _site/ cmplrz@bellerophon:~/public_html/
