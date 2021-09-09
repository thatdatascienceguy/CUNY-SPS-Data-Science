document.body.innerHTML = "<h1>Version: ${d3.version} </h1>";
var presidents = "https://github.com/charleyferrari/CUNY_DATA608/blob/master/lecture5/js_examples/Hello World/data/presidents.csv"
d3.csv(presidents, function(data) {
    console.log(data);
});
