#!/usr/bin/env python3

import os
import re
import sys
from bs4 import BeautifulSoup
from glob import glob

here = os.path.dirname(os.path.abspath(__here__))


def read_file(filepath, mode="r"):
    """return content from a file"""
    with open(filepath, mode) as filey:
        content = filey.read()
    return content


def write_file(filepath, lines, mode="w"):
    """return content from a file"""
    with open(filepath, mode) as filey:
        for line in lines:
            filey.write(line + "\n")


def parse_comments():

    comment_file = os.path.join("export", "comments.html")
    content = read_file(content_file)

    soup = BeautifulSoup(content, "lxml")
    elements = soup.find_all(class_="pam")
    comments = [
        re.sub("Natacha Sochat replied to her own comment.", "", x) for x in comments
    ]
    comments = [
        re.sub("Natacha Sochat commented on her own post.", "", x) for x in comments
    ]
    comments = [
        re.sub("Natacha Sochat commented on (.+) (photo|post).", "", x)
        for x in comments
    ]
    comments = [
        re.sub(r"[A-Za-z]{3} [0-9]+, \d{4}, [0-9]+:\d{2} (AM|PM)", "", x)
        for x in comments
    ]
    comments = [
        re.sub("Natacha Sochat replied to (.+) comment.", "", x) for x in comments
    ]
    comments = [
        re.sub(
            "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",
            "",
            x,
        )
        for x in comments
    ]
    comments = [re.sub("Group: .", "", x) for x in comments]
    comments = [x for x in comments if x.strip()]
    return comments


def parse_posts():

    posts = []
    post_files = glob("%s/export/post*.html" % here)
    for post_file in post_files:
        content = read_file(post_file)
        soup = BeautifulSoup(content, "lxml")
        elements = soup.find_all(class_="pam")
        posts = posts + [e.text for e in elements]

    posts = [
        re.sub("Natacha Sochat added a new photo to (.+) timeline.", "", x)
        for x in posts
    ]
    posts = [re.sub("Natacha Sochat added a new photo.", "", x) for x in posts]
    posts = [re.sub("^Natacha Sochat", "", x) for x in posts]
    posts = [
        re.sub(r"[A-Za-z]{3} [0-9]+, \d{4}, [0-9]+:\d{2} (AM|PM)", "", x) for x in posts
    ]
    posts = [re.sub("updated her status.", "", x) for x in posts]
    posts = [
        re.sub(
            "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",
            "",
            x,
        )
        for x in posts
    ]
    posts = [re.sub("Updated", "", x) for x in posts]
    posts = [re.sub("wrote on", "", x) for x in posts]
    posts = [
        x
        for x in posts
        if not x.startswith("You tagged") and not x.startswith("Place:")
    ]
    posts = [x for x in posts if "followed a person on" not in x]
    posts = [x for x in posts if x.strip()]
    return posts


def main():

    # Input file should be text file with sentences
    input_file = os.path.join(here, "input.txt")
    posts = parse_posts()
    comments = parse_comments()
    lines = posts + comments
    # len(lines)
    # 17380
    write_file("input.txt", lines)


if __name__ == "__main__":
    main()
