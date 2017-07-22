var app = angular.module("my_app", []);

app.controller("my_ctrl", function ($scope, $http, $sce, $interval, $compile) {



    $scope.getAllVideo = function (camname) {

        $http({
            method: "get",
            url: "photoinfo?name="+camname,
            data: {}
        }).then(function (response) {
            var el =angular.element(document.getElementById(response.data.cam_name));
            el.attr('src', '/static'+response.data.path);

            var el =angular.element(document.getElementById(response.data.person.id));
            el.attr('src', '/static'+response.data.person.photopath);


        });
    }
    //$scope.getAllVideo();
    $interval(function () {
        $scope.getAllVideo('cam1')
    },150);
    $interval(function () {
        $scope.getAllVideo('cam2')
    },150);
    $interval(function () {
        $scope.getAllVideo('cam3')
    },150);


});