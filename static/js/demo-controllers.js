var DemoControllers = angular.module('DemoControllers', ['SwampDragonServices']);

DemoControllers.controller('DemoCtrl', ['$scope', 'dataService', function($scope, dataService) {
    $scope.channel = 'odds';
    $scope.datasource = [];

    $scope.$on('dragonReady', function() {
        dataService.subscribe('odds-route', $scope.channel, {}).then(function(data) {
            this.dataMapper = new DataMapper(data);
        });
        dataService.get_list('odds-route', {}).then(function(data) {
            $scope.datasource = data
        });
    });

    $scope.$on('handleChannelMessage', function(e, channels, message) {
        console.log(message);
        if (indexOf.call(channels, $scope.channel) > -1) {
            this.dataMapper.mapData($scope.datasource, message);
            $scope.$apply();
        }
    });
}]);
