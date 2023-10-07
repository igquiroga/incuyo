<?php 

spl_autoload_register(function($clase){
	// Libs\Router => Libs/Router.php
	$ruta = str_replace("\\", "/", $clase).".php";
	if(file_exists($ruta)){
		require_once($ruta);
	}else{
		die("No se pudo cargar: {$clase}");
	}
});


?>