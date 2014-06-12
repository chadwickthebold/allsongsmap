describe('ArtistListControl', function() {

	beforeEach(module('asmApp'));

	it('should create "artists" model with 3 artists', inject(function($controller) {
		var scope = {},
				ctrl = $controller('ArtistListControl', {$scope:scope});

		expect(scope.artists.length).toBe(3);
	}));
});