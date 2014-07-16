#!/usr/bin/env python
# encoding: utf-8
"""
json_to_markdown.py

Created on 2014-07-13.

The MIT License (MIT)

Copyright (c) 2014. Shawn Douglas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import sys
import os
import json

filename = "../data/json/2014-07-13_pubmed_result.json"


post_template = """---
layout: post
published: true
title: "%s"
date: %s 12:00:00
pmid: %s
authors: "%s"
firstauthor: "%s"
journalname: "%s"
journalvolume: %s
journalissue: %s
journalpages: %s
---

%s

"""

with open(filename) as json_data:
    d = json.load(json_data)
    articles = d["PubmedArticleSet"]["PubmedArticle"]
    for article in articles:
        citation = article["MedlineCitation"]
        pmid = citation["PMID"]["#text"]
        print pmid
        date = citation["DateCreated"]
        dateStr = "%s-%s-%s" % (date["Year"], date["Month"], date["Day"])

        journal = citation["Article"]["Journal"]
        journalname = journal["ISOAbbreviation"]
        journalvolume = ""
        journalissue = ""
        journalpages = ""
        pubdate = journal["JournalIssue"]["PubDate"]
        
        if "Month" in pubdate and "Day" in pubdate:
            pubdateStr = "%s %s %s" % (pubdate["Year"], pubdate["Month"], pubdate["Day"])
        else:
            pubdateStr = pubdate["Year"]

        ji = journal["JournalIssue"]
        vipStr = ""
        if "Volume" in ji and "Issue" in ji:
            vipStr = "<b>%s</b>(%s)" % (ji["Volume"], ji["Issue"])
            journalvolume = ji["Volume"]
            journalissue = ji["Issue"]
            if "Pagination" in citation["Article"]:
                vipStr += ":%s" % citation["Article"]["Pagination"]["MedlinePgn"]
                journalpages = citation["Article"]["Pagination"]["MedlinePgn"]
            citeStr = "*%s %s;%s*" % (journalname, pubdateStr, vipStr)
        else:
            citeStr = "*%s %s*" % (journalname, pubdateStr)

        # print citeStr
        title = citation["Article"]["ArticleTitle"].replace('"', "'")
        print title
        abstract = citation["Article"]["Abstract"]["AbstractText"]
        authorCount = len(citation["Article"]["AuthorList"]["Author"])
        authors = citation["Article"]["AuthorList"]["Author"]
        if type(authors) is dict:
            authors = [authors]
        authorList = []
        for author in authors:
            authorList.append("%s %s" % (author["LastName"], author["Initials"]))
        authorStr = ", ".join(authorList)
        firstAuthorLN = authors[0]["LastName"]
        mdFilename = "%s-%s.md" % (dateStr, firstAuthorLN.lower())
        mdContent = post_template % (title, dateStr, pmid, authorStr, authorList[0], journalname, journalvolume, journalissue, journalpages, abstract)
        mdContent = mdContent.encode("utf-8")
        print mdFilename
        print mdContent
        f = open("../data/markdown/"+mdFilename, 'w')
        f.write(mdContent)
        f.close()
