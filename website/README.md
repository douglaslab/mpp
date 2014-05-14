mpp
===



## A Little About Jekyll
Jekyll is a static website generator that makes websites:

- SAFE from Denial of Service Attacks
- SAFE from caving under heavy traffic (if served from github pages or a CDN like cloudfront)
- SAFE from MySQL injection attacks (because it doesn't use a database)
- It needs NO security patches or updates.
- It doesn't need any special server script software (like php,python or ruby or perl etc)
- And there's no need for you to create or remember a password. You can make changes via git or the github account.


## where is the content ?

1. The front page of the site is in the root dir -> index.html file.
2. The static pages are all found under root dir -> about.md, contact.md etc.
3. The news page can be edited in the root dir too.
3. The news page pulls/sorts blog posts from inside the /_posts
4. Many settings are found in the root dir -> _config.yml



## More about content pages

There are only two types of content in the MPP site: posts and pages. The posts are all (in our site) YAML files under _/posts.

The thing to remember about posts is to mimic the format of them, particularly the 'yaml frontmatter'/xml stuff at the top of each file.
You can add categories etc and customize these to your hearts content, and then use ruby to sort the files with those fields. The documentation on that is very easy to find at http://jekyllrb.com.

Remember, it's crucial that you include the correct date as a prefix in filename of the post. Example of a correctly named post.

    2014-03-05-title-of-blog.md

If you're working on a blog post and it isnt finished you can name it 'something-title.md'; and commit it to the repository. When it's ready you can 'pubish' it by prepending the date to the name. Alternatively you can add:
    published: true
to that file's yaml frontmatter.

## Template Particulars.

### SCSS and CSS

The /assets/css/main.scss is really the important file here. It just imports a list of .scss files - jekyll knows where those are located (/assets/_sass), we tell it in the _config.yml file in the root dir.

Jekyll parses all the files imported in the '/assets/css/main.scss' file, and generates it into one, single, compressed file ucalled /_site/assets/css/main.css.


#### Grid

The grid we use is [Bourbon's Neat](http://neat.bourbon.io/). It's a semantic grid, so we style elements directly, not fill our html up with classes like 'article class="etc"'. The documentation is pretty easy.

The grid is only invoked in two places: assets/_sass/layout.scss and /assets/_sass/grid-settings.scss

We don't mention the grid anywhere else, not in styles or typography or anywhere else.

#### Typography

We use [Typlate](http://typeplate.com/) to set some basicly proper typographical proportions. They're loaded in /assets/_sass/typelate-scss/*
