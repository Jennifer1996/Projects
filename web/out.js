var x = 100;
console.log(x);
function myFunc() {
	x = x + 1;
	console.log(x);
	var x = document.getElementById('test');
	x.innerHTML = '我被点了';
	var y={
		'name':'Miss思',
		'age':21
	};
	for(var key in y){
		console.log(key + ',' + y[key]);
	}
	var y=[1,2,3,4,5];
	y.push(6);
	console.log(y);
	for (var i = 0; i < y.length; i++) {
		console.log(y[i])
	};
}
console.log(x);
console.log("Hello World");
// document.write('<h1>你好</h1>')