var asmApp = angular.module('asmApp', []);

asmApp.controller('ArtistListControl', function ($scope, $http) {
	$http.get('json/artistSample.json').success(function(data) {
		$scope.artists = data;
	});
});