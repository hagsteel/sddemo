var DemoApp = angular.module('DemoApp', [
    'SwampDragonServices',
    'DemoControllers'
]);

DemoApp.config(function($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{$').endSymbol('$}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
