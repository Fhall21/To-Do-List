var app = angular.module('toDo', []).config(function($httpProvider){
	$httpProvider.defaults.xsrfCookieName = 'csrtoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CRSFToken'
});
app.controller('toDoController', function($scope, $http){
	//$http = accepts http service 
	//make a request to the url and then get the data from the response there
	$http.get('/todo/api/').then(function(response){
		$scope.todoList = [];
		for (var i = 0; i < response.data.length; i++){
			// creating a new dictionary for each object in the data set

			var todo = {};
			//apending renamed data to todo {}
			todo.todoText = response.data[i].text;
			todo.done = response.data[i].done;
			todo.id = response.data[i].id;
			$scope.todoList.push(todo);
		}
	});


	$scope.saveData = function() {
		console.log('why?');
		//puts to link, data = data you're passing to api
		var data = {text: $scope.todoInput, done: false};
		$http.put('/todo/api/', data);
	};

	$scope.deleteData = function() {
		// get pk value
		var pk = 1;
		var path = '/todo/api/' + String(pk);
		$http.delete(path);

	}

	//$scope.todoList = [{todoText: 'Finish this app', done: false}];
	$scope.todoAdd = function(){
		//when toDoAdd gets called
		$scope.todoList.push({todoText: $scope.todoInput, done: false});
		// add the data from scope.todoInput into the todoList dictionary
		$scope.todoInput = '';
		//clears input


	};
	$scope.remove = function(){
		// old list
		var oldList = $scope.todoList;
		//empty the list
		$scope.todoList = [];
		//repopulate with all entries which have done as not True (False)
		angular.forEach(oldList, function(item){
			if (!item.done) $scope.todoList.push(item);
			else{
				$http.get('/todo/api/').then(function(response){
				id_list = [];
				for (var i = 0; i < response.data.length; i++){
					if (response.data[i].text == item.text){
						var pk = response.data[i].id;
					}
				var path = '/todo/api/' + String(pk);
				$http.delete(path);
			};
			});
		};
		// get pk value
		});
	};

});


