describe ('asmApp', function() {

	describe ('Artist List view', function() {

		beforeEach(function() {
			browser.get('index.html');
		});

		it('should filter the artist list as the user types in the search box', function() {

			var artistList = element.all(by.repeater('artist in artists')),
					query = element(by.model('query'));

					expect(artistList.count()).toBe(3);

					query.sendKeys('Maipei');
					expect(artistList.count()).toBe(1);

					query.clear();
					query.sendKeys('Indie');
					expect(artistList.count()).toBe(2);
		});
	});
});