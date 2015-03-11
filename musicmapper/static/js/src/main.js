Backbone.history.start();

var Story = Backbone.Model.extend({
	defaults: {
		id : 0,
		title : '',
		description : '',
		date : '',
		image : '',
		artists : []
	}
});

var StoryCollection = Backbone.Collection.extend({
	model : Story,
	url : '/api/stories'
});

var stories = new StoryCollection();
stories.fetch();