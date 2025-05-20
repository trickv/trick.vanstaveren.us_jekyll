My website, started in 2006 in Mediawiki, now ported to Jekyll in 2018 using https://github.com/peterjc/mediawiki_to_git_md

Most of this is rather buried history :)

# Set up a dev environ

```
sudo apt install ruby-bundler ruby-dev make
bundle config set --local path 'vendor/bundle'
bundle install
# mess it up
cd vendor/bundle/ruby/*/gems/jekyll-last-modified-at-1*/lib/jekyll-last-modified-at
curl https://github.com/trickv/jekyll-last-modified-at/commit/ae8f326499c59c485b47833991a1bc849f70e6ae.patch | patch -p3
```

# Make changes

```
bundle exec jekyll serve --livereload [--incremental]
# hack hack hack
```

# Publish

```
./build # uses a container
./push
# preview changeset from rsync
./push --real
```

# Maintenance

Learn bundler: https://bundler.io/v1.3/rationale.html#a-simple-bundler-workflow
