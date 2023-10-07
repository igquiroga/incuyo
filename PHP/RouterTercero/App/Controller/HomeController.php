<?php 
namespace App\Controller;

class HomeController extends Controller{

	public function home($view, $params = ""){
		return $this->view($view);
	}

}


?>