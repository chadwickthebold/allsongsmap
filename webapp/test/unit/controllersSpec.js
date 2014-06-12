describe('asm Controllers', function() {

	describe('ArtistListControl', function() {
		var scope, control, $httpBackend

		beforeEach(module('asmApp'));

		beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
			$httpBackend = _$httpBackend_;
			jasmine.getJSONFixtures().fixturesPath='base/test/mock';

			$httpBackend.expectGET('json/artistSample.json').respond(
				getJSONFixture('artistMock.json')
			);

			scope = $rootScope.$new();
			ctrl = $controller('ArtistListControl', {$scope: scope});
		}));

		it('should create "artists" model with 3 artists fetched from xhr', function() {
			expect(scope.artists).toBeUndefined();
			$httpBackend.flush();

			expect(scope.artists).toEqual(
				getJSONFixture('artistMock.json')
			);
		});
	});
});