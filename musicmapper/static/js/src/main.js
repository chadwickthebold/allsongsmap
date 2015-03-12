//Application namespace
var asm = asm || {};

(function() {
	'use strict'

	Backbone.history.start();

	asm.Story = Backbone.Model.extend({
		defaults: {
			id : 0,
			title : '',
			description : '',
			date : '',
			image : '',
			artists : []
		}
	});

	asm.StoryCollection = Backbone.Collection.extend({
		model : asm.Story,
		url : '/api/stories'
	});

	asm.stories = new asm.StoryCollection();
	asm.stories.fetch();

})();