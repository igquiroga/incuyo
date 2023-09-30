<?php 

require_once('Router.php');
Router::get('/',function(){
	require_once('home.php');
});
Router::get('/productos',function(){
	require_once('productos.php');

});
Router::get('/productos/:category/:id',function($category,$id){
	echo "<br>Productos<br>";
	echo "Category: {$category}<br>";
	echo "ID: {$id}<br>";
});

Router::render();

?>