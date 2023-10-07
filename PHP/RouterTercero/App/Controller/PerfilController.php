<?php 
namespace App\Controller;

class PerfilController extends Controller{

	public function perfil($view, $nombre = ""){
		return $this->view($view);
	}

	
}


?>