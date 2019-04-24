My website, started in 2006 in Mediawiki, now ported to Jekyll in 2018 using https://github.com/peterjc/mediawiki_to_git_md

Most of this is rather buried history :)

h1. Set up a dev environ

```
sudo apt install ruby-bundler ruby-dev make
bundle install --path vendor/bundle
```

h1. Make changes

```
bundle exec jekyll serve --livereload [--incremental]
# hack hack hack
```

h1. Publish

```
bundle exec jekyll build
./push
# preview changeset from rsync
./push --real
```
