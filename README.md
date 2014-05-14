# Project MPP website

This is based on a subset the [template](https://github.com/douglaslab/templates/tree/master/project) we use for projects in the lab. We've omitted experiments, paper, and protocols.

## directory structure

* **code**
* **data**
	* **images**
	* **json**
* **meetings**
* *outline.md*
* **slides**
* **website**


## content description

### code

Source code lives here!

### data

Data lives here. Whenever possible, structure as json (your code should read and write json), or in its original raw format (e.g. tiff).

### meetings

What's happened recently? What's our plan?

### *outline.md*

This is bullet-point outline of the project. It can be considered a rough outline of the paper, but of course things can change before things get to the manuscript-writing phase, so this document should be the primary home of all the project ideas and questions until it's clear that it's time to write the paper.

### slides

Summary slides of the project that could be used for introducting the project, teaching, etc.


### website

Every project should ultimately be able to serve its own website. The site (e.g. jekyll, etc) should live here.

If you're working on a blog post and it isnt finished you can name it 'something-title.md'; and commit it to the repository. When it's ready you can 'pubish' it by prepending the date to the name. Alternatively you can add:
    published: true
to that file's yaml frontmatter.

## Template Particulars.

### SCSS and CSS

The /assets/css/main.scss is really the important file here. It just imports a list of .scss files - jekyll knows where those are located (/assets/_sass), we tell it in the _config.yml file in the root dir.

Jekyll parses all the files imported in the '/assets/css/main.scss' file, and generates it into one, single, compressed file ucalled /_site/assets/css/main.css.
