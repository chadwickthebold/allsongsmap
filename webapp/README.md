

Allsongsmap Frontend
====================

## Backbone-Boilerplate Info ###

### Documentation ###

See the backbone boilerplate wiki with any questions about the template that backs this project: [Backbone Boilerplate Wiki](https://github.com/backbone-boilerplate/backbone-boilerplate/wiki)


### Getting started ###

The easiest way to get started is to install Git and clone the repository:

``` bash
# Using Git, fetch only the latest commits.  You won't need the full history
# for your project.
git clone --depth 1 https://github.com/backbone-boilerplate/backbone-boilerplate

# Move the repository to your own project name.
mv backbone-boilerplate my-project
```

You will need to download and install [Node.js](http://nodejs.org/) if you want
to use the commands in the following sections.

### Updating dependencies ###

Third party packages may update independently from this main repo, so it's a
good idea to update after fetching.

``` bash
# Install global dependencies.  Depending on your user account you may need to
# gain elevated privileges using something like `sudo`.
npm install -g grunt-cli bower

# Optionally install coveralls (integration is baked in with Travis CI).
npm install -g coveralls

# Install NPM dependencies.
npm install

# Install Bower dependencies.
bower install
```

### Build process ###

The build process consists of numerous Grunt plugin tasks that work together
to optimize your application.

``` bash
# To run the build process, run the default Grunt task.
grunt

# Run a build and test the now optimized assets.
grunt default server:release
```

### Running tests ###

To run tests, simply add `.spec.js` files throughout your application and they
will be automatically picked up by the runner.  You can find example test specs
in the `test` directory.

To run Karma as a daemon:
*Which will automatically run your tests after you save.*

``` bash
grunt karma:daemon
```

To run Karma tests once and output the results:

``` bash
grunt karma:run
```

After either above command is run, code coverage reports will be available in
the `test/coverage` folder.

By default, the test runner is Mocha and Chai.  You can easily change this by
editting the commented regions of the karma configuration in `Gruntfile.js`.

### License ###
Copyright © 2014 Tim Branyen (@tbranyen)  
Licensed under the MIT license.
