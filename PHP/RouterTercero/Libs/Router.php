<?php 

namespace Libs;

class Router{
	
	private static $routes=[];

	public static function get($path,$callback){
		$path = trim($path,"/");
		self::$routes['GET'][$path] = $callback;
	}
	public static function getView($uri){
		#producto/samsung
		//0 => producto, 1 => samsung
		$view = explode('/', $uri);
		$view = $view[0] === '' ? 'Home' : $view[0];
		$ruta = "App/View/".$view.".php";
		return $ruta;
	}
	public static function render(){
		$uri = $_SERVER['REQUEST_URI'];
		$uri = trim($uri,"/");
		$method = $_SERVER['REQUEST_METHOD'];

		foreach (self::$routes[$method] as $path => $callback) {
			
			if (strpos($path,':')) {
				$path = preg_replace("#:[a-zA-Z0-9]+#", '([a-zA-Z0-9]+)', $path);
			}

			if(preg_match("#^{$path}$#", $uri,$matches)){
				$view = self::getView($uri);
				$params = array_slice($matches, 1);
				if(is_callable($callback)){
					$response = $callback(...$params);
				}
				if(is_array($callback)){
					$controller = new $callback[0];
					$response = $controller->{$callback[1]}($view,...$params);
				}
				echo $response;
				return;
			}
		}
		echo "404 PAGE NOT FOUND";
	}	
}

?>