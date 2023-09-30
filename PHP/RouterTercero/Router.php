<?php 
class Router{
	private static $routes = [];

	public static function get($path, $callback){
		$path = trim($path,'/');
		self::$routes['GET'][$path] = $callback;
	}

	public static function render(){
		$uri = $_SERVER['REQUEST_URI'];
		//localhost, poner su carpeta
		$uri = ltrim($uri,'/incuyo/');
		$uri = ltrim($uri,'RouterTercero');
		$uri = trim($uri, '/');
		///
		$method = $_SERVER['REQUEST_METHOD'];
		foreach(self::$routes[$method] as $path => $callback){
			if(strpos($path,':')){
				$path = preg_replace('#:[a-zA-Z0-9]+#','([a-zA-Z0-9]+)',$path);
			}
			if(preg_match("#^{$path}$#",$uri,$matches)){
				$params = array_slice($matches,1);
				$response = $callback(...$params);
				return $response;
			}
		}
		echo "404 PAGE NOT FOUND";
		
	}
}


?>