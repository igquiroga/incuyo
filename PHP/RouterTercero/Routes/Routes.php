<?php 

use Libs\Router;
use App\Controller\Controller;
use App\Controller\PerfilController;
use App\Controller\HomeController;
use App\Controller\ProductController;

Router::get('/', [HomeController::class, 'home']);

Router::get('/productos', [ProductController::class, 'productos']);

Router::get('/productos/:marca', [ProductController::class, 'productos']);

Router::get('/productos/:marca/:id', [ProductController::class, 'productos']);

Router::get('/perfil/:nombre', [PerfilController::class, 'perfil']);

Router::get('/acerca',function(){
	echo "ACERCA";
});

Router::render();
?>